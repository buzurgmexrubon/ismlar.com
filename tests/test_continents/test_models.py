from django.test import TestCase

from apps.continents.models import Continent


class ContinentModelTest(TestCase):
    def setUp(self):
        self.continent = Continent.objects.create(name="Europe")

    def test_continent_creation(self):
        self.assertEqual(self.continent.name, "Europe")
        self.assertEqual(str(self.continent), "Europe")
