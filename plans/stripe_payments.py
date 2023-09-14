import stripe
from decouple import config

stripe.api_key = config("STRIPE_API_SECRET")

stripe.Product.create(name="Gold Special")