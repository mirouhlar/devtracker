from django import template

register = template.Library()

@register.filter(name='attr')
def add_attribute(field, value):
    """Adds or modifies HTML attributes of a form field."""
    attrs = field.field.widget.attrs
    splitted_value = value.split(':')
    if len(splitted_value) == 2:
        attr_name, attr_value = splitted_value
        attrs[attr_name] = attr_value
    return field