from django.urls import path
from .views import (
    home_page_view, 
    blog, 
    contact, 
    about, 
    single_blog,
    listings,
)

urlpatterns = [
    path('', home_page_view),
    path('contact/', contact),
    path('about/', about),
    path('listings/', listings),
]
