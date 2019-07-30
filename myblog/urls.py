
from django.urls import path
from . import views

urlpatterns = [
    path('blog/<int:blog_id>/', views.detail, name='detail'),
    path('blog/writing/', views.writing, name='writing'),
    path('blog/submit/', views.submit, name='submit'),
]
