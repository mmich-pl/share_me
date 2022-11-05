from rest_framework.routers import SimpleRouter

from .views import LoginViewSet

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')

urlpatterns = [
    *routes.urls
]
