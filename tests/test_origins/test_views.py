# from django.test import TestCase
# from django.urls import reverse
# from apps.names.models import Name
# from apps.origins.models import Origin
# from apps.continents.models import Continent
#
#
# class NameViewTest(TestCase):
#     def setUp(self):
#         self.continent = Continent.objects.create(name="Asia")
#         self.origin = Origin.objects.create(name="Japan")
#         self.name_instance = Name.objects.create(
#             name="Hiro",
#             meaning="Generous",
#             continent=self.continent,
#             origin=self.origin,
#         )
#
#     def test_name_list_view(self):
#         response = self.client.get(reverse("name_list"))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Hiro")
#
#     def test_name_detail_view(self):
#         response = self.client.get(reverse("name_detail", args=[self.name_instance.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Hiro")
#         self.assertContains(response, "Generous")
#         self.assertContains(response, "Asia")
#         self.assertContains(response, "Japan")
