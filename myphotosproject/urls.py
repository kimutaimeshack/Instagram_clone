
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('photos.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
 
]