from django.contrib import admin
from django.conf.urls import url
from sampleapp import views

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^create/',views.create_apicall,name="creationapi"),
url(r'^show/',views.show_apicall,name="showapi"),

]