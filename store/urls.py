from django.urls import path
from . import views
from .views import SearchResultsView


app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('website/<int:website_id>/', views.website, name='website'),
    path('about-us/', views.about_us, name='about_us'),
    path('search-results/', SearchResultsView.as_view(), name='search_results'),
]