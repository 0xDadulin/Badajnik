from django.urls import path, re_path
from .views import upload_files, LaboratoryListCreate, LaboratoryRetrieveUpdateDestroy
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Twoje inne url tutaj
    path('upload/', upload_files, name='upload_files'),
    path('api/laboratories/', LaboratoryListCreate.as_view(), name='laboratory-list-create'),
    path('api/laboratories/<int:pk>/', LaboratoryRetrieveUpdateDestroy.as_view(), name='laboratory-retrieve-update-destroy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Upewnij się, że to jest ostatnie w urlpatterns
urlpatterns += [re_path(r'^.*$', TemplateView.as_view(template_name='index.html'))]
