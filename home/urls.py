from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home_view"),
    path('contact-us/', views.ContactView.as_view(), name="contact_view"),
    path('about-us/', views.AboutView.as_view(), name="about_view"),
    # path('review/', views.ReviewView.as_view(), name="review_view"),
    path('legal-documentation/', views.LegalDocumentationView.as_view(), name="legal_view"),
    path('faqs/', views.FaqsView.as_view(), name="faqs_view"),
]
