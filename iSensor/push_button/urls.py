from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iSensor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

                       url(r'^add$', 'push_button.views.AboutView')
)
