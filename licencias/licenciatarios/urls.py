from django.conf.urls import url
from .views import  *
from django.contrib.auth import views as auth_views

from . import views

app_name = 'licenciatarios'
urlpatterns = [
    # url(r'^(?P<id>\d+)/$', views.licencia_edit, name='licencia-edit'),
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.licencia_nueva, name='licencia-nueva'),
    url(r'^print/(?P<id>\d+)/$', views.show_licencia, name='print-licencia'),
    # url(r'^print/(?P<userid>\d+)$', views.print_licencia, name='print_licencia'),
    url(r'^add/$', LicenciaCreate.as_view(), name='licencia-add'),
    url(r'^(?P<pk>[0-9]+)/$', LicenciaUpdate.as_view(), name ='licencia-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', LicenciaDelete.as_view(), name='licencia-delete'),
    url(r'^config/$', ConfigUpdate.as_view(), name='config'),

    url(r'^usr/$', UsuarioList.as_view(), name='usuario'),
    url(r'^usr/add/$', UsuarioCreate.as_view(), name='usuario-add'),
    url(r'^usr/(?P<pk>[0-9]+)/$', UsuarioUpdate.as_view(), name ='usuario-update'),
    url(r'^usr/(?P<pk>[0-9]+)/delete/$', UsuarioDelete.as_view(), name='usuario-delete'),

    url(r'^login/$', auth_views.login, name='login-view'),
    url(r'^logout/$', auth_views.logout, name='logout-view'),

]


# url(r'^User/(?P<userid>\d+)/$', 'search.views.user_detail', name='user_details'),
