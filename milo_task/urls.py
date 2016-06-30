from django.conf.urls import url
from milo_task import views

urlpatterns = [
    url(r'^$', views.users_list, name='index'),
    url(r'^user/(?P<username>\w+)/$', views.current_user, name='user'),
    url(r'^to_csv/', views.export_users, name='csv'),
    url(r'^del/(?P<username>\w+)/$', views.del_user, name='del'),
    url(r'^add/', views.add_user, name='add'),
    url(r'^edit/(?P<username>\w+)/$', views.edit_user, name='edit'),
]
