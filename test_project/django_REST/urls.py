# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'account', AccountViewSet)

# specify URL Path for rest_framework
urlpatterns = [
	path('', include(router.urls)),
	path('account/', include('rest_framework.urls'))
]
