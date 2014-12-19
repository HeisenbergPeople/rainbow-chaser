from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iSensor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

                       url(r'^add/(?P<name>.*)/(?P<state>True|False)/(?P<datetime>.*)$', views.AddButtonEventView.as_view()),
                       url(r'^list/$', views.ListEventsView.as_view(), name='button_list'),
                       url(r'^list/(?P<name>.*)/$', views.ListEventsView.as_view(), name='button_list'),
                       url(r'^(?P<name>[A-Za-z_][A-Za-z0-9_]*)$', views.ButtonDetail.as_view(), name='button_detail'),
                       url(r'^$', views.MainView.as_view(), name='button_index'),

)
