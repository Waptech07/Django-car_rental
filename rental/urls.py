
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('cars/', views.car_list, name='car_list'),
    path('rent/', views.rent_car, name='rent_car'),
    path('return/', views.return_car, name='return_car'),
    path('rent_history/', views.rent_history, name='rent_history'),
    path('guest_user/', views.guest_user, name='guest_user'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change_password/', views.change_password, name='change_password'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)