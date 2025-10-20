from django.urls import path
from .views import blog_view, single_blog_view, blog_category_view

urlpatterns = [
    path('', blog_view),
    path('category/<int:id>', blog_category_view),
    path('<int:id>', single_blog_view),     
]