import  django_filters
from  .models import *


class TimeFilter(django_filters.filterset):
    class Meta:
        model = Reader
        fields = '__all__'