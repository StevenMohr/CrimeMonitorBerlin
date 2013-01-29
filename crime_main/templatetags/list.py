__author__ = 'steven'

from django.template import Library

register = Library()

@register.simple_tag
def pretty_list(item_list):
    return_string = ""
    for item in item_list:
        return_string += unicode(item) + ", "
    return return_string[:-2]
