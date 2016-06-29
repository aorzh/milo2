from django import template
from datetime import date

register = template.Library()


@register.simple_tag()
def eligible(birthday):
    el = 'blocked'
    if calculate_age(birthday) > 13:
        el = 'allowed'
    return el


@register.simple_tag()
def bizzfuzz(rand):
    value = rand
    if rand % 5 == 0:
        value = 'Fuzz'
    elif rand % 3 == 0:
        value = 'Bizz'
    elif rand % 3 == 0 and rand % 5 == 0:
        value = 'BizzFuzz'
    return value


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

