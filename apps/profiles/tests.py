from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

# from apps.lettings.models import Letting, Address
from apps.profiles.models import Profile


class ProfilesTests(TestCase):
    @classmethod
    def setUpClass(cls):

        # Create User
        u1 = User.objects.create(username="Test User Name")

        # Create Profile
        cls.profile1 = Profile.objects.create(favorite_city="Test City", user=u1)

    @classmethod
    def tearDownClass(cls):
        Profile.objects.all().delete()

    def test_happy_index(self):
        url = reverse("profiles:index")
        response = self.client.get(url)
        self.assertContains(response, "<h1>Profiles</h1>", status_code=200)
        count = 3  # [Home] + [Lettings] + 1 Profile = 3
        self.assertContains(response, "href", count=count, status_code=200)

    def test_happy_details(self):
        url = reverse("profiles:profile", args=[self.profile1])
        response = self.client.get(url)
        self.assertContains(response, f"<h1>{self.profile1}</h1>", status_code=200)

    def test_sad_details(self):
        fake_username = "Wrong User Name"
        url = reverse("profiles:profile", args=[fake_username])
        response = self.client.get(url)
        self.assertContains(
            response, f"Profile '{fake_username}' doesn't exist", status_code=404
        )


class ProfilesEmptyTests(TestCase):
    def test_happy_index(self):
        url = reverse("profiles:index")
        response = self.client.get(url)
        self.assertContains(response, "<h1>Profiles</h1>", status_code=200)
        self.assertContains(response, "No profiles are available", status_code=200)

    def test_sad_details(self):
        fake_username = "Wrong User Name"
        url = reverse("profiles:profile", args=[fake_username])
        response = self.client.get(url)
        self.assertContains(
            response, f"Profile '{fake_username}' doesn't exist", status_code=404
        )
