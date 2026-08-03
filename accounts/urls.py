from django.urls import path
from .views import login_view, logout_view, dashboard, register_view, create_admin

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register_view, name='register'),
    path("create-admin/", create_admin),
]