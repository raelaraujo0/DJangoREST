from rest_framework.routers import DefaultRouter
from App.views import BooksViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', BooksViewSet)

urlpatterns = router.urls