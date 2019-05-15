from django import template

register = template.Library()

@register.filter
def number_to_asterisks(value):
    return value*'★'