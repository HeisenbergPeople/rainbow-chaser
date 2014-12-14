from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iSensor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

                       url(r'^add/(?P<name>.*)/(?P<state>True|False)/(?P<datetime>.*)$', views.AddButtonEventView.as_view()),
                       url(r'^view/$', views.ListEventsView.as_view()),

)
