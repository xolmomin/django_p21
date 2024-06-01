from django.template import Library

register = Library()


@register.filter()
def count_chars(value, arg=None):
    return len(value)


@register.filter()
def current_path(path, menu):
    return path.startswith(f'/{menu}')
