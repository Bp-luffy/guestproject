from django.conf.urls import url
from sign.views import views
from sign.views import viewsforapi

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^$', views.index),
    url(r'^login_action/$', views.login_action),
    url(r'^event_manage/$', views.event_manage),
    url(r'^search_name/$', views.search_name),
    url(r'^guest_manage', views.guest_manage),
    url(r'^sign_index/(?P<eid>[0-9]+)/$', views.sign_index),
    url(r'^sign_index_action/(?P<eid>[0-9]+)/$', views.sign_index_action),
    url(r'^logout/$', views.login_action),
    url(r'^add_event/$',viewsforapi.add_event),
    url(r'^get_evebt_list$',viewsforapi.get_evebt_list),
    url(r'^add_guest$',viewsforapi.add_guest),
]
