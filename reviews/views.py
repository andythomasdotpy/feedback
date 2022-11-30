from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import ReviewForm
from .models import Review

# Create your views here.

def reviews(request):
    if request.method == "POST":
        existing_data = Review.objects.get(pk=2)
        print(existing_data)
        form = ReviewForm(request.POST, instance=existing_data)

        if form.is_valid():  # is_valid will do 3 things.. 1) validiate the inputs (by default verifies not empty) 2) then will return True if valid 3) if data is valid it populates another field with valide data
            # data = form.cleaned_data
            # print(data['user'], data['review'], data['rating'])
            form.save()
            # temp_review_data = Review(
            #     user=data['user'], 
            #     review=data['review'], 
            #     rating=data['rating'])
            # temp_review_data.save()
            
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
