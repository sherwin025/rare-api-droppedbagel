from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rareapi.views import register_user,  login_user, CategoryView
from rest_framework import routers
from rareapi.views import TagView

from rareapi.views.post import PostView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'categories', CategoryView, 'category')
router.register(r"posts", PostView, "post")
router.register(r'tags', TagView, 'tag')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
