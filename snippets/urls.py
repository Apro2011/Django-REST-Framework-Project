from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from snippets.views import SnippetViewSet, UserViewSet
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({
    "get": "list",
    "post": "create",
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    "get": "highlight",
}, renderer_classes = [renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    "get": "list",
})

user_detail = UserViewSet.as_view({
    "get": "retrieve",
})


router = routers.SimpleRouter()
router.register(r'', SnippetViewSet, basename="snippets")
router.register(r'', UserViewSet, basename="users")


urlpatterns = [
    path('', include(router.urls)),
    path('snippets/', snippet_list, name="snippet-list"),
    path('snippets/<int:pk>/', snippet_detail, name="snippet-detail"),
    path('users/', user_list, name="user-list"),
    path('users/<int:pk>/', user_detail, name="user-detail"),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name="snippet-highlight"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
