from django.urls import path
from userauth import views
app_name='userauth'
urlpatterns = [
    path('/login/',views.login_view,name='login')
]
