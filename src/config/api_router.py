from django.conf import settings
from growth_plan_linker.users.api.views import UserViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register('users', UserViewSet)


app_name = 'api'
urlpatterns = router.urls
