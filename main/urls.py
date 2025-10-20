from django.urls import path
from .views import (
    home_page_view, 
    blog, 
    contact, 
    about, 
    single_blog,
    listings,
    single_listing,
)

urlpatterns = [
    path('', home_page_view),
    path('contact/', contact),
    path('about/', about),
    path('listings/', listings),
    path('listings/<int:id>', single_listing),
]
