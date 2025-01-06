from django.contrib import admin
from django.urls import path, include
from api.views import index  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Root URL points to the index view
    path('api/', include('api.urls')),  # Include API URLs
]
