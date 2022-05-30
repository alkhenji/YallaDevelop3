from django.urls import include, path
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
               path('', include('yalladevelop.urls')),
               path('admin/', admin.site.urls),
               ]
