from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Profile


def index(request):
    """
    Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed
    consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
    massa dolor cursus neque, quis dictum lacus d
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet
    neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed
    tincidunt, dolor id facilisis fringilla, eros leo tristique lacus, it. Nam
    aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et
    netus et males
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {"profile": profile}
        return render(request, "profiles/profile.html", context)
    except Profile.DoesNotExist:
        return HttpResponseNotFound(f"Profile '{username}' doesn't exist")
