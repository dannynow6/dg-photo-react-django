from backend_api.views import PhotoViewSet
from rest_framework.routers import DefaultRouter
from backend_api import views

router = DefaultRouter()
router.register(r"photos", views.PhotoViewSet, basename="photo")
urlpatterns = router.urls
