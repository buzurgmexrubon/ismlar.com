from django.test import TestCase

from apps.names.models import Name
from apps.origins.models import Origin
from apps.continents.models import Continent


class NameModelTest(TestCase):
    def setUp(self):
        self.continent = Continent.objects.create(name="Europe")
        self.origin = Origin.objects.create(name="France", continent=self.continent)
        self.name_instance = Name.objects.create(
            name="Pierre", meaning="Stone", origin=self.origin
        )

    def test_name_creation(self):
        self.assertEqual(self.name_instance.name, "Pierre")
        self.assertEqual(self.name_instance.meaning, "Stone")
        self.assertEqual(self.name_instance.origin.name, "France")
        self.assertEqual(self.name_instance.origin.continent.name, "Europe")

    def test_name_str_method(self):
        self.assertEqual(str(self.name_instance), "Pierre")
