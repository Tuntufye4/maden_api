from django.contrib import admin   
from django.conf import settings   
from django.urls import path, include
from django.conf.urls.static import static
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/document/', include('document.urls')), 
    path('api/favourite/', include('favourite.urls')),       
    path('api/message/', include('message.urls')),     
    path('api/property/', include('property.urls')),     
    path('api/reservation/', include('reservation.urls')),  
    path('api/viewingRequest/', include('viewingRequest.urls')),  
    path('api/auth/', include('users.urls')),                          
]           
   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)                               
               
#if settings.DEBUG:
 #   import debug_toolbar  
 #   urlpatterns += [                  
 #       path('__debug__/', include(debug_toolbar.urls)),
 #   ]             _  