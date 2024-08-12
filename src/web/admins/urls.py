from django.urls import path
from .views import (
    DashboardView,
    UserListView, UserPasswordResetView, UserDetailView, UserUpdateView, SocialsView
)


app_name = 'admins'
urlpatterns = [

    path('', DashboardView.as_view(), name='dashboard'),

    path('user/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/change/', UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/password/reset/', UserPasswordResetView.as_view(), name='user-password-reset-view'),

    path('socials/', SocialsView.as_view(), name='social-accounts'),

]
