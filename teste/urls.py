from django.contrib import admin

from django.urls import path, include

from Blog.views import chiclete, jujuba

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('jujuba/', jujuba),
    path('chiclete/', chiclete),
]
