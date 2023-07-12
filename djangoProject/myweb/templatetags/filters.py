from django import template
from myweb.views import get_context

register = template.Library()

@register.filter
def get_person_info(person, info_type):
    context = get_context(person.name)
    if info_type:
        return context[info_type]
    else:
        return ''
