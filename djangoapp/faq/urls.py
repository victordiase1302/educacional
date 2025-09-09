from django.urls import path
from faq import views

app_name = "faqs"

urlpatterns = [
    path('', views.all_faqs, name='all-faqs')
]
