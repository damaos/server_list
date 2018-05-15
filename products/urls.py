from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^login/$', views.auth_login, name='authentication'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout' ),
    url(r'^$', views.ServerList.as_view(), name='index'),
    # url(r'^servidor/(?P<pk>[0-9]+)/$', views.ServerDetail.as_view(), name='detail'),
    url(r'^servidor/new', views.new_product, name="new"),
   # url(r'^crear-servidor$', views.ServerCreateView.as_view(),  name='new'),
	url(r'^update_servidor/(?P<id>\d+)/$', views.ServerEditView.as_view(), name='update'),
	url(r'^(?P<pk>\d+)/delete-servidor$', views.ServerDeleteView.as_view(), name='delete'),
    
]