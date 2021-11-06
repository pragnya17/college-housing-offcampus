import django_filters
from .models import Property


class PropertyFilter(django_filters.FilterSet):

    sorting_options = (
        ('total_price', 'Ascending price'),
        ('-total_price', 'Descending price'),
        ('-furnished', 'Furnished'),
        ('furnished', 'Unfurnished'),
        ('-parking', 'Parking availability'),
    )

    sort = django_filters.ChoiceFilter(label='Sort by', choices=sorting_options, method='sort_by_option')

    class Meta:
        model = Property

        fields = {'title': ['icontains'],
        'total_price': ['lte'],
        'distance': ['lte'],
        'bedrooms': ['exact'],
        'bathrooms': ['exact'],
        }
    
    def sort_by_option(self, queryset, name, value):
        return queryset.order_by(value)