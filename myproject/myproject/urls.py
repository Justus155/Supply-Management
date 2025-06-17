"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# Importing the views module from the supply app is not necessary here
# since we are not using any views directly in this file.
# from supply import views  # This import is not needed in this file
# The above import is not used in this file, so it can be removed.
# The views module is typically used in the supply app's urls.py file
# to define the views for the URLs in that app.
# The import statement for views is not needed in this file
# as we are only defining the URL patterns for the project.

# The urlpatterns list routes URLs to views.
# For more information please see:


# https://docs.djangoproject.com/en/5.2/topics/http/urls/

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('supply.urls')),
]
