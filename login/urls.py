from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^check_email/$', views.check_email, name='check_email'),
    url(r'add_log/$', views.add_log, name='add_log'),
    url(r'goal_edit/$', views.goal_edit, name='goal_edit')

]