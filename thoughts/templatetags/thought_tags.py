__author__ = 'PRITHVIRAJ'

from django import template
from thoughts.forms import ThoughtForm


register = template.Library()
@register.inclusion_tag('thoughts/thoughts_form.html')

def thought_form():
    form = ThoughtForm()
    return {'form': form}
