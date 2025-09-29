
from django.contrib import admin
from django.urls import path
from twoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main, name='web_register'),
    path('register/',views.register, name= 'data_register' ),
    path('login/',views.login, name= 'login')
]
