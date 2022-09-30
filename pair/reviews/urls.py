from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.main, name="main"),
    path("review/", views.review, name="review"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
]
