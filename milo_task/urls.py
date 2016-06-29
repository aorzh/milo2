from django.conf.urls import url
from milo_task import views

urlpatterns = [
    url(r'^$', views.users_list, name='milo'),
    url(r'^user/(\d+)/', views.current_user, name='user'),
]
