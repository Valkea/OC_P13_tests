from django.urls import reverse
from django.test import TestCase

from apps.lettings.models import Letting, Address


class LettingTests(TestCase):
    @classmethod
    def setUpClass(cls):

        # Create Address
        a1 = Address.objects.create(
            number=11,
            street="test street",
            city="test city",
            state="test state",
            zip_code=12345,
            country_iso_code="FR",
        )

        # Create Letting
        cls.letting1 = Letting.objects.create(title="Letting Test 01", address=a1)

    @classmethod
    def tearDownClass(cls):
        Address.objects.all().delete()
        Letting.objects.all().delete()

    def test_happy_index(self):
        url = reverse("lettings:index")
        response = self.client.get(url)
        self.assertContains(response, "<h1>Lettings</h1>", status_code=200)
        count = 3  # [Home] + [Profiles] + 1 Letting = 3
        self.assertContains(response, "href", count=count, status_code=200)

    def test_happy_details(self):
        url = reverse("lettings:letting", args=[self.letting1.id])
        response = self.client.get(url)
        self.assertContains(
            response, f"<h1>{self.letting1.title}</h1>", status_code=200
        )

    def test_sad_details(self):
        url = reverse("lettings:letting", args=[0])
        response = self.client.get(url)
        self.assertContains(response, f"Letting ID:0 doesn't exist", status_code=404)


class LettingEmptyTests(TestCase):
    def test_happy_index(self):
        url = reverse("lettings:index")
        response = self.client.get(url)
        self.assertContains(response, "<h1>Lettings</h1>", status_code=200)
        self.assertContains(response, "No lettings are available", status_code=200)

    def test_sad_details(self):
        url = reverse("lettings:letting", args=[0])
        response = self.client.get(url)
        self.assertContains(response, f"Letting ID:0 doesn't exist", status_code=404)
