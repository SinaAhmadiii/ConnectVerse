from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('info/', include('info.urls')),
    path('post/', include('post.urls')),
    path('comment/', include('comment.urls')),
    path('reply/', include('reply.urls')),
    path('bookmark/', include('bookmark.urls')),

]
