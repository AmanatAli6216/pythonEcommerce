from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        # print(id, product.id)
        # print(type(id), type(product.id))
        if int(id) == product.id:
            return True
    # print(product, cart)
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        # print(id, product.id)
        # print(type(id), type(product.id))
        if int(id) == product.id:
            return cart.get(id)
    # print(product, cart)
    return 0
@register.filter(name='price_total')
def price_total(product, cart):
    return int(product.price) * int(cart_quantity(product, cart))


@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += int(price_total(p, cart))
    return sum