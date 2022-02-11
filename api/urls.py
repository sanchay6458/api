from django.urls import path
from .views import BlogAPIView,BlogDetailAPIView,BlogCreateAPIView,BlogDetailAPIView

urlpatterns = [
    path('', BlogAPIView.as_view()),
    path('<int:pk>/', BlogDetailAPIView.as_view()),
    path('create/', BlogCreateAPIView.as_view()),
    path('detail/<int:pk>/', BlogDetailAPIView.as_view()),
]
