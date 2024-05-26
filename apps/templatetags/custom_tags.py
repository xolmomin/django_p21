from django.template import Library

register = Library()


@register.filter()
def count_chars(value, arg=None):
    return len(value)
