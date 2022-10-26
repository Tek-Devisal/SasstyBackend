from rest_framework.routers import DefaultRouter
from .views import CreateUserView
from constants import api_version


router = DefaultRouter()
router.register(api_version + 'createUser', CreateUserView)

urlpatterns = router.urls