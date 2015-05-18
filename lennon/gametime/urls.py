from django.conf.urls import url, include

router = routers.DefaultRouter()

urlpatterns = [
	url(r'^', include(router.urls)),
]