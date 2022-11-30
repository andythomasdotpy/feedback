from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import ReviewForm
from .models import Review

# Create your views here.

def reviews(request):
    if request.method == "POST":
        existing_data = Review.objects.get(pk=2) # assign variable to entry which should be updated
        print(existing_data)
        form = ReviewForm(request.POST, instance=existing_data) # to update data entry include instance keyword and pass in entry to update

        # form = ReviewForm(request.Post) # to add a new entry

        if form.is_valid():  # is_valid will do 3 things.. 1) validiate the inputs (by default verifies not empty) 2) then will return True if valid 3) if data is valid it populates another field with valide data
            print(form)
            form.save()

            
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
