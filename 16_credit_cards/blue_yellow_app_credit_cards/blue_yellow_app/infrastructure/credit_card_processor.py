import stripe


class CreditCardProcessor:
    stripe_public_key = None
    __stripe_api_key = None

    @staticmethod
    def global_init(stripe_api_key, stripe_public_key):
        CreditCardProcessor.__stripe_api_key = stripe_api_key
        CreditCardProcessor.stripe_public_key = stripe_public_key

    @staticmethod
    def complete_stripe_purchase(stripe_token: str, desc: str, price_in_usd: float):
        price_in_cents = int(round(price_in_usd * 100, 10))

        stripe.api_key = CreditCardProcessor.__stripe_api_key
        charge = stripe.Charge.create(
            amount=price_in_cents,
            currency='USD',
            source=stripe_token,
            description=desc
        )

        return charge
