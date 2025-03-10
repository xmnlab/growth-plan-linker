# type: ignore
import pytest

from rest_framework.test import APIRequestFactory

from growth_plan_linker.users.api.views import UserViewSet
from growth_plan_linker.users.models import User


class TestUserViewSet:
    @pytest.fixture()
    def api_rf(self) -> APIRequestFactory:
        return APIRequestFactory()

    def test_get_queryset(self, user: User, api_rf: APIRequestFactory) -> None:
        view = UserViewSet()
        request = api_rf.get('/fake-url/')
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, api_rf: APIRequestFactory) -> None:
        view = UserViewSet()
        request = api_rf.get('/fake-url/')
        request.user = user

        view.request = request

        response = view.me(request)  # type: ignore[call-arg, arg-type, misc]

        assert response.data == {
            'url': f'http://testserver/api/users/{user.pk}/',
            'name': user.name,
        }
