from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import ReviewForm

# Create your views here.

def reviews(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():  # is_valid will do 3 things.. 1) validiate the inputs (by default verifies not empty) 2) then will return True if valid 3) if data is valid it populates another field with valide data
            print(form.cleaned_data['user_name'])
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
