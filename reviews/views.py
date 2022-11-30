from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():  # is_valid will do 3 things.. 1) validiate the inputs (by default verifies not empty) 2) then will return True if valid 3) if data is valid it populates another field with valide data
            print(form)
            form.save()

            return HttpResponseRedirect("/thank-you")
        
        return render(request, "reviews/review.html", {
            "form": form
        })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
