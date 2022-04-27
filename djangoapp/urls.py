from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('details/<st_id>', views.show, name='show'),
    path('del/<st_id>', views.del_St, name='del'),
    path('add', views.addStudent, name='add'),
    path('edit/<st_id>', views.editStudent, name='edit'),

    # rest_framework urls
    path('api-list', views.api_all_students, name='api-list'),
    path('api-st/<st_id>', views.api_student_details, name='api-st'),
    path('api-add', views.api_student_create, name='api-add'),
    path('api-edit/<st_id>', views.api_student_edit, name='api-edit'),
    path('api-del/<st_id>', views.api_student_delete, name='api-del'),

    # auth urls
    path('login', views.loginPg, name='login'),
    path('signup', views.signupPg, name='signup'),
    path('signout', views.signoutPg, name='signout')

]
