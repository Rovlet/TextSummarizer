from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    path(r'summarize_text/', views.PostTextView.as_view(), name='post_text'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

urlpatterns.append(path('', include('cms.urls')))


admin.site.enable_nav_sidebar = False
