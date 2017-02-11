from django.conf.urls import url

from . import views

app_name = 'licenciatarios'
urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.licencia_edit, name='licencia-edit'),
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.licencia_nueva, name='licencia-nueva'),
    url(r'^print/(?P<id>\d+)/$', views.show_licencia, name='print-licencia'),
    # url(r'^print/(?P<userid>\d+)$', views.print_licencia, name='print_licencia'),
]


# url(r'^User/(?P<userid>\d+)/$', 'search.views.user_detail', name='user_details'),
