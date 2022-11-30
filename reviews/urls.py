from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),    # need to add as_view() since we are calling "View" class in views when creating out class
    path("thank-you", views.thank_you, name="thank-you"),
]