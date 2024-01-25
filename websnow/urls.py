from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('incidentdown.urls')),    
    path('report/', include('generatereport.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
