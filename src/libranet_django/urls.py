"""
libranet_django.urls.

URL configuration for libranet_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

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

import django.contrib.admin as django_contrib_admin
import django.urls as django_urls
import django.views as django_views

# from django.contrib import admin
# from django.urls import path
# from django.views.generic.base import RedirectView

favicon_view = django_views.generic.base.RedirectView.as_view(url="/static/favicon.png", permanent=True)

urlpatterns = [
    # django_urls.re_path(r"^favicon\.ico$", favicon_view),
    django_urls.path("admin/", django_contrib_admin.site.urls),
]
