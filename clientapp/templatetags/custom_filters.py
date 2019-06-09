from django import template

register = template.Library()

@register.filter
def number_to_asterisks(value):
    return value*'★'

@register.filter
def price_qty(value, arg):
    return value*arg
