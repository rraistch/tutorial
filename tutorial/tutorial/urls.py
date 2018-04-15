from django.conf import settings
from django.urls import include, path
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'blog/', include('blog.urls', namespace='blog')),
    path(r'', TemplateView.as_view(template_name="home.html"),
        name='homepage'),
    path(r'comments/', include('django_comments_xtd.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()



