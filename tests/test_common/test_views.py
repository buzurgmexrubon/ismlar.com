from django.test import TestCase
from django.urls import reverse


class HomePageViewTest(TestCase):
    def test_home_page_renders_home_template(self):
        response = self.client.get(reverse("common:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
