from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def main(request):
    return render(request, "reviews/main.html")


def review(request):
    reviews_ = Review.objects.all()
    context = {
        "reviews": reviews_,
    }

    return render(request, "reviews/index.html", context)


def new(request):
    return render(request, "reviews/new.html")


def create(request):
    title_ = request.POST.get("title")
    star_ = request.POST.get("star")
    content_ = request.POST.get("content")

    Review.objects.create(title=title_, content=content_, star=star_)

    return redirect("reviews:review")
