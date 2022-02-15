from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from rareapi.views import register_user,  login_user, CategoryView, CommentView, UserView

from rest_framework import routers
from rareapi.views.subscriptions import SubscriptionView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'subscriptions', SubscriptionView, 'subscription')

from rareapi.views import TagView
from rareapi.views.post import PostView
router.register(r'categories', CategoryView, 'category')
router.register(r'comments', CommentView, 'comment')
router.register(r"posts", PostView, "post")
router.register(r'tags', TagView, 'tag')
router.register(r'users', UserView, 'user')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
