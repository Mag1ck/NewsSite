from django import template
from django.utils.safestring import mark_safe  # Import mark_safe

register = template.Library()

@register.filter(name='split_paragraphs')
def split_paragraphs(value):
    lines = value.split('\n')
    wrapped_lines = ['<p>{}</p>'.format(line) for line in lines if line]  # Skip empty lines
    return mark_safe(''.join(wrapped_lines))  # Mark the output as safe