from django.conf.urls import patterns, include, url

from Question_paper.views import PostAdPage

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mysite.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )


urlpatterns = patterns('',
                       url(r'^postad/', PostAdPage.as_view()),
                       )
