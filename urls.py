"""
URL dispatcher of package
"""

from django.conf.urls import url
from . import views

app_name = 'ayase-blog'
urlpatterns = [
    url(r'^$', views.home_page, name='index'),
    url(r'^category/(?P<category_url>[\w]+)/$', views.category, name='category'),
    url(r'^about/$', views.about, name='about'),
    url(r'^post/(?P<postId>[0-9]+)/$', views.post, name='post'),
    url(r'^expr/', views.expr)
]
