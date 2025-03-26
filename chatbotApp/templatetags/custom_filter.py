# registrationapp/mytags/custom_filters.py
from django import template

register = template.Library()
@register.filter(name='zip_lists')
def zip_lists(list1, list2):
    return zip(list1, list2)