from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import UsersViewSet, retrieve_token, sign_up
from django.contrib import admin

router = SimpleRouter()

router.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/auth/signup/', sign_up, name='sign_up'),
    path('v1/auth/token/', retrieve_token, name='retrieve_token'),
    path('v1/', include(router.urls))
]
