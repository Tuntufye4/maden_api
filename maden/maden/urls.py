from django.contrib import admin   
from django.conf import settings   
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/document', include('document.urls')), 
    path('api/favourite/', include('favourite.urls')),
    path('api/location/', include('location.urls')),        
    path('api/message/', include('message.urls')),
    path('api/offer/', include('offer.urls')),
    path('api/payment/', include('payment.urls')),   
    path('api/property/', include('property.urls')),
    path('api/propertyImage/', include('propertyImage.urls')),    
    path('api/reservation/', include('reservation.urls')),  
    path('api/viewingRequest/', include('viewingRequest.urls')),  
    path('api/user/', include('user.urls')),     
]        
                    
        
#if settings.DEBUG:
 #   import debug_toolbar
 #   urlpatterns += [
 #       path('__debug__/', include(debug_toolbar.urls)),
 #   ]          