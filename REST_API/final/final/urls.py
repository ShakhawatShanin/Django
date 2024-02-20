from django.contrib import admin
from django.urls import path, include

from django.conf import settings  # for media
from django.conf.urls.static import static

from final import views  # for html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage), # for interface path 
    path('api/', include('apprun.urls'))  # for api path
]
# for media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

