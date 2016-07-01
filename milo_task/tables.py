import django_tables2 as tables
from .models import CustomUser
import itertools
from django.utils.safestring import mark_safe


class CustomUserTable(tables.Table):
    eligible = tables.TemplateColumn('{% load milo_tags %} {% eligible record.birthday %}')
    bizzfuzz = tables.TemplateColumn('{% load milo_tags %} {% bizzfuzz  record.random_number %}')

    def __init__(self, *args, **kwargs):
        super(CustomUserTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_username(self, value):
        return mark_safe(
            '<a href="/user/%s"> %s</a>'
            % (value, value)
        )

    class Meta:
        model = CustomUser
        exclude = ['last_login', 'is_active', 'is_admin', 'password', 'id']
        template = 'django_tables2/bootstrap.html'
        orderable = False
        attrs = {'class': 'paleblue'}
