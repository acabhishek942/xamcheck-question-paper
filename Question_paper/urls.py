from django.conf.urls import patterns, include, url
from Question_paper.views import PostAdPage

urlpatterns = patterns('',
                       url(r'^postad/', PostAdPage.as_view()),
                       )
