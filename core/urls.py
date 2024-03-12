from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from lessons.views import template_lesson_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('lessons.urls')),
    path('', template_lesson_list),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
