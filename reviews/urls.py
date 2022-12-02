from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    
    path("", views.ReviewView.as_view()),    # need to add as_view() since we are calling "View" class in views when creating out class
    # path("thank-you", views.ThankYouListView.as_view()),
    # path("thank-you", TemplateView.as_view(template_name="reviews/thank_you.html")),
    path("thank-you", views.ThankYouTemplateView.as_view()),
    # path("reviews", views.ReviewListView.as_view()),
    path("reviews/", views.ReviewsListView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view(), name="single_review"),
]