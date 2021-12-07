from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user, get_user_model
from .models import Property, Review

class GoogleLoginTest(TestCase):

    # Create a user for testing
    # Custom user model references adapted from https://docs.djangoproject.com/en/3.2/topics/auth/customizing/
    @classmethod
    def setUp(cls):
        user_model = get_user_model()
        cls.test_user = user_model.objects.create(email='test@example.com')
        cls.test_user.set_password('Abcdefg1!')
        cls.test_user.save()
    
    # Test login credentials
    # User auth attributes found in https://docs.djangoproject.com/en/3.2/ref/contrib/auth/
    # Client login code adapted from https://docs.djangoproject.com/en/3.2/topics/testing/tools/
    def test_login(self):
        c = Client()
        c.login(email='test@example.com', password='Abcdefg1!')
        user = get_user(c)
        self.assertTrue(user.is_authenticated)
    
    # Test logging out
    def test_logout(self):
        c = Client()
        c.force_login(self.test_user)
        self.assertTrue(get_user(c).is_authenticated)
        
        c.logout()
        self.assertFalse(get_user(c).is_authenticated)
    
    # Test incorrect email
    def test_wrong_email(self):
        c = Client()
        c.login(email='example@test.com', password='Abcdefg1!')
        self.assertFalse(get_user(c).is_authenticated)
    
    # Test incorrect password
    def test_wrong_password(self):
        c = Client()
        c.login(email='test@example.com', password='abcdefg1!')
        self.assertFalse(get_user(c).is_authenticated)

class PropertyModelTests(TestCase):
    def test___str__(self):
        # equivalence
        p1 = Property(title="property 1")
        self.assertEqual(Property.__str__(p1), 'property 1')

        #boundary 
        p2 = Property()
        self.assertEqual(Property.__str__(p2), 'This property has no title')

        #exception
        with self.assertRaises(AttributeError):
            Property.__str__(None)

class PropertiesListViewTests(TestCase):

    # If no properties are found, an appropriate message is displayed.
    def test_no_properties(self):
        response = self.client.get(reverse('properties'), secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No properties were found.")
        self.assertQuerysetEqual(response.context['properties_list'], [])
    
    # Test to make sure properties are automatically displayed on the listings page
    def test_single_property(self):
        property1 = Property.objects.create(title="The Flats", description="desc", monthly_rent=1000, distance=1.0)
        response = self.client.get(reverse('properties'), secure=True)
        self.assertQuerysetEqual(response.context['properties_list'], [property1])
        self.assertQuerysetEqual(response.context['filter'].qs, [property1])
    
    def test_two_properties(self):
        property1 = Property.objects.create(title="The Flats", description="desc1", monthly_rent=1000, distance=1.0)
        property2 = Property.objects.create(title="Jefferson Commons", description="desc2", monthly_rent=750, distance=0.7)
        response = self.client.get(reverse('properties'), secure=True)
        self.assertQuerysetEqual(response.context['properties_list'], [property1, property2], ordered=False)
        self.assertQuerysetEqual(response.context['filter'].qs, [property1, property2], ordered=False)

class PropertyFilterTests(TestCase):

    def setUp(self):
        Property.objects.create(
            title="The Flats", 
            description="desc1", 
            monthly_rent=1000, 
            distance=1.2,
            furnished="Yes",
            parking="No",
            bedrooms=4,
            bathrooms=4)
        Property.objects.create(
            title="Jefferson Commons", 
            description="desc2", 
            monthly_rent=750, 
            distance=0.6,
            furnished="No",
            parking="Yes",
            bedrooms=4,
            bathrooms=3)
        Property.objects.create(
            title="Montebello Pointe", 
            description="desc3", 
            monthly_rent=800, 
            furnished="No",
            parking="No",
            bedrooms=3,
            bathrooms=2,
            distance=1.0)

    # Test a filter that should only select for one of two properties based on the title
    def test_single_filter_by_title(self):
        response = self.client.get(reverse('properties'), {'title__icontains': 'flats'}, secure=True)
        self.assertQuerysetEqual(response.context['filter'].qs, ['<Property: The Flats>'])
    
    # When a filter selects for no properties, make sure none are displayed
    def test_no_filter_results_by_title(self):
        response = self.client.get(reverse('properties'), {'title__icontains': 'asdfghi'}, secure=True)
        self.assertQuerysetEqual(response.context['filter'].qs, [])
    
    # Test filtering by price
    def test_filter_by_price(self):
        response = self.client.get(reverse('properties'), {'monthly_rent__lte': 999}, secure=True)
        self.assertQuerysetEqual(response.context['filter'].qs, ['<Property: Jefferson Commons>', '<Property: Montebello Pointe>'], ordered=False)
    
    # Test filtering by number of bedrooms
    def test_filter_by_bedrooms(self):
        response = self.client.get(reverse('properties'), {'bedrooms': 4}, secure=True)
        self.assertQuerysetEqual(response.context['filter'].qs, ['<Property: The Flats>', '<Property: Jefferson Commons>'], ordered=False)
    
    # # Test filtering by number of bathrooms
    def test_filter_by_bathrooms(self):
        response = self.client.get(reverse('properties'), {'bathrooms': 2}, secure=True)
        self.assertQuerysetEqual(response.context['filter'].qs, ['<Property: Montebello Pointe>'])
    
    # # Test filtering for furnished properties
    def test_filter_by_furnished(self):
        response = self.client.get(reverse('properties'), {'furnish_choice': 'Yes'}, secure=True)
        self.assertQuerysetEqual(response.context['filter'].qs, ['<Property: The Flats>'])

    # Test filtering for unfurnished properties
    def test_filter_by_unfurnished(self):
        response = self.client.get(reverse('properties'), {'furnish_choice': 'No'}, secure=True)
        self.assertQuerysetEqual(response.context['filter'].qs, ['<Property: Jefferson Commons>', '<Property: Montebello Pointe>'], ordered=False)
    
    # Test sorting properties by ascending price
    def test_sort_by_ascending_price(self):
        response = self.client.get(reverse('properties'), {'sort': 'monthly_rent'}, secure=True)
        self.assertQuerysetEqual(response.context['filter'].qs, ['<Property: Jefferson Commons>', '<Property: Montebello Pointe>', '<Property: The Flats>'])

    # Test sorting properties by descending price
    def test_sort_by_descending_price(self):
        response = self.client.get(reverse('properties'), {'sort': '-monthly_rent'}, secure=True)
        self.assertQuerysetEqual(response.context['filter'].qs, ['<Property: The Flats>', '<Property: Montebello Pointe>', '<Property: Jefferson Commons>'])

    # Test sorting properties by parking availability
    def test_sort_by_parking(self):
        response = self.client.get(reverse('properties'), {'sort': '-parking'}, secure=True)
        self.assertQuerysetEqual(response.context['filter'].qs, ['<Property: Jefferson Commons>', '<Property: The Flats>', '<Property: Montebello Pointe>'])

    # Test sorting properties by shortest dist. to grounds
    def test_sort_by_ascending_price(self):
        response = self.client.get(reverse('properties'), {'sort': 'distance'}, secure=True)
        self.assertQuerysetEqual(response.context['filter'].qs, ['<Property: Jefferson Commons>', '<Property: Montebello Pointe>', '<Property: The Flats>'])

class ReviewModelTests(TestCase):
    def test___str__(self):
        # equivalence of property id's
        r1 = Review(property_id=1)
        self.assertEqual(r1.property_id, 1)

        #boundary
        r2 = Review(property_id=-1)
        response = self.client.get(reverse('properties:property'))
        self.assertEqual(r2.property_id, -1)
