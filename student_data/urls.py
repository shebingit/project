from student_data import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.loginpage,name='loginpage'),
    path('login/',views.login,name='login'),
    path('home_page',views.home_page,name='home_page'),
    path('home_page_load',views.home_page_load,name='home_page_load'),
    path('show_data',views.show_data,name='show_data'),
    path('course_data_add',views.course_data_add,name='course_data_add'),
    path('student_add',views.student_add, name='student_add'),
    path('logout/',views.logout,name="logout")
]

