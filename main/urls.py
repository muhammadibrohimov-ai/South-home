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
    path('blog/', blog),
    path('contact/', contact),
    path('about/', about),
    path('single-blog/', single_blog),
    path('listings/', listings),
]
