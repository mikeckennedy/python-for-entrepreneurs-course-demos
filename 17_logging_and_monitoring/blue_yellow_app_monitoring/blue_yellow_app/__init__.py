import datetime
import pkg_resources
import os
import sys
from pyramid.config import Configurator
# noinspection PyUnresolvedReferences
import blue_yellow_app
import blue_yellow_app.controllers.home_controller as home
import blue_yellow_app.controllers.albums_controller as albums
import blue_yellow_app.controllers.account_controller as account
import blue_yellow_app.controllers.admin_controller as admin
import blue_yellow_app.controllers.newsletter_controller as news
import blue_yellow_app.controllers.store_controller as store
from blue_yellow_app.data.dbsession import DbSessionFactory
from blue_yellow_app.email.template_paser import EmailTemplateParser
from blue_yellow_app.infrastructure.credit_card_processor import CreditCardProcessor
from blue_yellow_app.services.email_service import EmailService
from blue_yellow_app.services.log_service import LogService
from blue_yellow_app.services.mailinglist_service import MailingListService

dev_mode = False


def main(_, **settings):
    config = Configurator(settings=settings)

    init_logging(config)  # runs first
    init_mode(config)
    init_includes(config)
    init_routing(config)
    init_db(config)
    init_mailing_list(config)
    init_smtp_mail(config)
    init_email_templates(config)
    init_credit_cards(config)

    return config.make_wsgi_app()


def init_logging(config):
    settings = config.get_settings()
    log_level = settings.get('log_level')
    log_filename = settings.get('log_filename')

    LogService.global_init(log_level, log_filename)

    log_package_versions()


def init_email_templates(_):
    EmailTemplateParser.global_init()


def init_smtp_mail(config):
    global dev_mode
    unset = 'YOUR_VALUE'

    settings = config.get_settings()
    smtp_username = settings.get('smtp_username')
    smtp_password = settings.get('smtp_password')
    smtp_server = settings.get('smtp_server')
    smtp_port = settings.get('smtp_port')

    local_dev_mode = dev_mode

    if smtp_username == unset:
        log = LogService.get_startup_log()
        log.warn("SMTP server values not set in config file. "
                 "Outbound email will not work.")
        local_dev_mode = True  # turn off email if the system has no server.

    EmailService.global_init(smtp_username, smtp_password, smtp_server, smtp_port, local_dev_mode)


def init_db(_):
    top_folder = os.path.dirname(blue_yellow_app.__file__)
    rel_folder = os.path.join('db', 'blue_yellow.sqlite')

    db_file = os.path.join(top_folder, rel_folder)
    DbSessionFactory.global_init(db_file)


def init_mode(config):
    global dev_mode
    settings = config.get_settings()
    dev_mode = settings.get('mode') == 'dev'
    log = LogService.get_startup_log()
    log.notice('Running in {} mode.'.format('dev' if dev_mode else 'prod'))


def init_mailing_list(config):
    unset = 'ADD_YOUR_API_KEY'

    settings = config.get_settings()
    mailchimp_api = settings.get('mailchimp_api')
    mailchimp_list_id = settings.get('mailchimp_list_id')

    if mailchimp_api == unset:
        log = LogService.get_startup_log()
        log.warn("Mailchimp API values not set in config file. "
                 "Mailing list subscriptions will not work.")

    MailingListService.global_init(mailchimp_api, mailchimp_list_id)


def init_credit_cards(config):
    unset = 'ADD_YOUR_API_KEY'

    settings = config.get_settings()
    stripe_private_key = settings.get('stripe_private_key')
    stripe_public_key = settings.get('stripe_public_key')

    if stripe_public_key == unset:
        log = LogService.get_startup_log()
        log.warn("Stripe API values not set in config file. "
                 "Credit card purchases will not work.")

    CreditCardProcessor.global_init(stripe_private_key, stripe_public_key)


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_handler('root', '/', handler=home.HomeController, action='index')

    add_controller_routes(config, home.HomeController, 'home')
    add_controller_routes(config, albums.AlbumsController, 'albums')
    add_controller_routes(config, account.AccountController, 'account')
    add_controller_routes(config, admin.AdminController, 'admin')
    add_controller_routes(config, news.NewsletterController, 'newsletter')
    add_controller_routes(config, store.StoreController, 'store')

    config.scan()


def add_controller_routes(config, ctrl, prefix):
    config.add_handler(prefix + 'ctrl_index', '/' + prefix, handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl_index/', '/' + prefix + '/', handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl', '/' + prefix + '/{action}', handler=ctrl)
    config.add_handler(prefix + 'ctrl/', '/' + prefix + '/{action}/', handler=ctrl)
    config.add_handler(prefix + 'ctrl_id', '/' + prefix + '/{action}/{id}', handler=ctrl)


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
    config.include('rollbar.contrib.pyramid')


def log_package_versions():
    startup_log = LogService.get_startup_log()

    # update from setup.py when changed!
    # This list is the closure of all dependencies,
    # taken from: pip list --format json
    requires = [{"name": "Chameleon"},
                {"name": "docopt", "version": "0.4.0"},
                {"name": "html2text", "version": "2016.9.19"},
                {"name": "hupper", "version": "0.4.1"}, {"name": "Logbook", "version": "1.0.0"},
                {"name": "mailchimp", "version": "2.0.9"}, {"name": "mailer", "version": "0.8.1"},
                {"name": "Mako", "version": "1.0.6"}, {"name": "MarkupSafe", "version": "0.23"},
                {"name": "passlib", "version": "1.7.0.post20170103083911"}, {"name": "PasteDeploy", "version": "1.5.2"},
                {"name": "pip", "version": "9.0.1"}, {"name": "Pygments", "version": "2.1.3"},
                {"name": "pyramid", "version": "1.8a1"}, {"name": "pyramid-chameleon", "version": "0.3"},
                {"name": "pyramid-debugtoolbar", "version": "3.0.5"}, {"name": "pyramid-handlers", "version": "0.5"},
                {"name": "pyramid-mako", "version": "1.0.2"}, {"name": "repoze.lru", "version": "0.6"},
                {"name": "requests", "version": "2.12.4"}, {"name": "setuptools", "version": "28.8.0"},
                {"name": "SQLAlchemy", "version": "1.1.4"}, {"name": "stripe", "version": "1.46.0"},
                {"name": "translationstring", "version": "1.3"}, {"name": "venusian", "version": "1.0"},
                {"name": "waitress", "version": "1.0.1"}, {"name": "WebOb", "version": "1.7.0"},
                {"name": "zope.deprecation", "version": "4.2.0"}, {"name": "zope.interface", "version": "4.3.3"}]

    requires.sort(key=lambda d: d['name'].lower())
    t0 = datetime.datetime.now()
    startup_log.notice('---------- Python version info ------------------')
    startup_log.notice(sys.version.replace('\n', ' ').replace('  ', ' '))
    startup_log.notice('---------- package version info ------------------')
    for rec in requires:
        try:
            version = pkg_resources.get_distribution(rec['name']).version
            if version:
                startup_log.notice('{} v{}'.format(rec['name'], version))
            else:
                startup_log.notice("WHERE IS IT? {}.".format(rec['name']))
        except Exception as x:
            startup_log.notice('{} UNKNOWN VERSION ({})'.format(rec['name'], x))

    dt = datetime.datetime.now() - t0

    startup_log.notice('Package info gathered in {} sec'.format(dt.total_seconds()))
    startup_log.notice('--------------------------------------------------')
