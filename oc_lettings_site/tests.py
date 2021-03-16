from django.urls import reverse
from django.test import TestCase


class OcLettingsSiteTests(TestCase):
    def test_happy_index(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertContains(
            response, "<h1>Welcome to Holiday Homes</h1>", status_code=200
        )
