import django_filters
from .models import Property


class PropertyFilter(django_filters.FilterSet):

    furnish_options = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    furnish_choice = django_filters.ChoiceFilter(
        label='Furnished', choices=furnish_options, method='filter_by_furnished')

    sorting_options = (
        ('monthly_rent', 'Ascending price'),
        ('-monthly_rent', 'Descending price'),
        ('-parking', 'Parking availability'),
        ('distance', 'Distance to grounds (mi)')
    )

    sort = django_filters.ChoiceFilter(
        label='Sort by', choices=sorting_options, method='sort_by_option')

    class Meta:
        model = Property

        fields = {'title': ['icontains'],
                  'monthly_rent': ['lte'],
                  'bedrooms': ['exact'],
                  'bathrooms': ['exact'],
                  }

    def sort_by_option(self, queryset, name, value):
        return queryset.order_by(value)

    def filter_by_furnished(self, queryset, name, value):
        return queryset.filter(furnished=value)
