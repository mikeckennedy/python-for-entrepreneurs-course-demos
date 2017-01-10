class CreditCardProcessor:
    __stripe_api_key = None
    __stripe_public_key = None

    @staticmethod
    def global_init(stripe_api_key, stripe_public_key):
        CreditCardProcessor.__stripe_api_key = stripe_api_key
        CreditCardProcessor.__stripe_public_key = stripe_public_key

    @staticmethod
    def complete_stripe_purchase(stripe_token: str, desc: str, price_in_usd: float):
        pass
