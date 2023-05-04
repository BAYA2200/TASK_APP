import django_filters
from django_filters.rest_framework import filterset

from CRM.models import Task


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Task
        fields = ['title', 'description', ]
