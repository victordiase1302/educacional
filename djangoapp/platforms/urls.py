from django.urls import path
from platforms import views

app_name = 'platforms'

urlpatterns = [
    path('search/', views.search_platform, name='search-platform'),
    path('search-term/', views.search_for_term, name='search-for-term'),
    path('<slug:slug>/', views.platform, name='platform'),
    path('', views.all_platforms, name='platforms'),
    # path('', views.index, name='index'),
    # path('get-platform/<int:id>/', views.get_platform, name='get_platform')
]
