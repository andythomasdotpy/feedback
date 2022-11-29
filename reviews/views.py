from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import ReviewForm

# Create your views here.

def reviews(request):
    # if request.method == "POST":
    #     usernamesss = request.POST["username_1"]
    #     print(usernamesss)

    #     if len(usernamesss) < 8:
    #         return render(request, "reviews/review.html", {
    #             "has_error": True 
    #         })

    #     return HttpResponseRedirect("/thank-you")

    form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
