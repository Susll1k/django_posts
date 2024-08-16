from app.views import home, DeletePost, CreatePost, create_review
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('create/', CreatePost.as_view(), name='create'),
    path('delete/<int:id>', DeletePost.as_view(), name='delete'),
    path('create_review/', create_review, name='create_review')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
