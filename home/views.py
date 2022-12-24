from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Review
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        # logout(request)
        # all_review = Review.objects.all().exclude(review="").order_by("-updated")[:2]
        # user_no = User.objects.all().count()
        # if all_review.count() == 2:
        #     context = {
        #         "all_review":all_review,
        #         "user_no":user_no
        #     }
        #     return render(request, "home/index.html", context)
        # else:
        return render(request, "home/index.html")


class AboutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, "home/about.html")


class ContactView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, "home/contact.html")

    def post(self, request, *args, **kwargs):
        messages.success(request, "Your Message was sent succesfully. Pipsgod will get back to you as soon as possible")
        #Send mail
        return redirect("home:contact_view")


class LegalDocumentationView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, "home/legal-documentation.html")


class FaqsView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, "home/faqs.html")


class ReviewView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            user_review = Review.objects.get(user=request.user)
        except:
            user_review = ""
        context = {
            "user_review":user_review
        }
        return render(request, "home/review.html", context)

    def post(self, request, *args, **kwargs):
        user_review = request.POST.get("user_review")
        try:
            review  = Review.objects.get(user=request.user)
        except:
            review  = None

        if review != None:
            review.review = user_review
            review.save()
        else:
            messages.success(request, "Your review was updated successfully")
            review  = Review.objects.create(user=request.user, review=user_review)
        return redirect("home:review_view")