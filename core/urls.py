from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ClientViewSet, InterventionViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
# On ajoute basename='intervention' et basename='client'
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'interventions', InterventionViewSet, basename='intervention')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
