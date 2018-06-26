from django.conf.urls import include,url
from blogpost import views
from django.contrib import admin


urlpatterns= [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index,name='index'),
    url(r'^formpage/',views.form_name_view,name='form_name')

]