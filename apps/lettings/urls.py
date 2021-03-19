from django.urls import path

from . import views

app_name = "lettings"

urlpatterns = [
    path("lettings/", views.index, name="index"),
    path("lettings/<int:letting_id>/", views.letting, name="letting"),

    path('sentry-debug/', views.trigger_error, name="sentry-debug"),
    path('extra-branch-test/', views.trigger_error, name="sentry-debug"),
]
