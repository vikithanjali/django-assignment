from django.urls import path

from .views import HomePageView,conformemail,filehandler,get_skill_search,admin_login
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('conformemail',conformemail,name='conformmail'),
    path('filehandler',filehandler,name='filehandler'),
path('get_skill_search',get_skill_search,name='get_skill_search'),
path('admin_login',admin_login,name='admin_login'),

]