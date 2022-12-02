from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "thank-you"

class ThankYouTemplateView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=3) # Now we can query for ratings above 3
        return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review            # Django uses Review but lowercase review to access data in html file