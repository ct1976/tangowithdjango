from django.conf.urls import url
from django.contrib import admin
from rango.views import index,category,add_category,add_page,register,user_login,restricted,user_logout,about

urlpatterns = [
    url(r'^$', index, name='index'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$',category,name='category'),
        url(r'^add_category/$',add_category,name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',add_page,name='add_page'),
    # url(r'^register/$',register,name='register'),
    # url(r'^login/$', user_login, name='login'),
    url(r'^restricted/', restricted, name='restricted'),
    # url(r'^logout/$', user_logout, name='logout'),
    url(r'^about/$', about, name='about'),
        ]