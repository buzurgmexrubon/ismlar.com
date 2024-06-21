from django.test import TestCase

from apps.continents.models import Continent
from apps.origins.models import Origin


class OriginModelTest(TestCase):
    def setUp(self):
        self.continent = Continent.objects.create(name="Europe")
        self.origin = Origin.objects.create(name="France", continent=self.continent)

    def test_origin_creation(self):
        self.assertEqual(self.origin.name, "France")
        self.assertEqual(str(self.origin), "France")
