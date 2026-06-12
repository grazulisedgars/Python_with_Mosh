# One way how to import packages
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# Second way how to import package

# from ecommerce.shipping import calc_shipping

# calc_shipping()

# Third way to import would be the whole shipping package

from ecommerce import shipping

shipping.calc_shipping()
