from django.contrib import admin
from django.urls import path,include
from django.conf import  settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("app_pages.urls")),
    path("",include("users.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("",include("admin_app.urls")),
    path("group/",include("chat.urls"),name='group')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

