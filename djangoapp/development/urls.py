from development import views
from django.urls import path

app_name = 'development'

urlpatterns = [
    path('profile/', views.index, name='profile'),
    path('search/', views.search, name='search'),
    path('job-detail/', views.job_detail, name='job-detail'),
    path('apply-form/', views.apply_form, name='apply-form'),
    path('company-detail/', views.company_detail, name='company-detail'),
    path('notification/', views.notification, name='notification'),
]
