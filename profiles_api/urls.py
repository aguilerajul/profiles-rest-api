from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

ROUTER = DefaultRouter()
ROUTER.register('profile', views.UserProfileViewSet)
ROUTER.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(ROUTER.urls)),
]
