from django import template
from datetime import date, datetime

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
    rand = int(rand)
    if rand % 3 == 0 and rand % 5 == 0:
        return 'BizzFuzz'
    elif rand % 3 == 0:
        return 'Bizz'
    elif rand % 5 == 0:
        return 'Fuzz'
    return value


def calculate_age(born):
    today = date.today()
    # born = datetime.strptime(born, "%Y-%d-%m")
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

