from django.conf.urls import include, url
from django.views.generic import ListView, DateDetailView
from django.conf.urls.static import static
from django.conf import settings
from blog.models import Post


app_name = 'blog'


urlpatterns = [
    url(r'^$', ListView.as_view(model=Post, paginate_by=3), name='post-list'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        DateDetailView.as_view(date_field="publish", model=Post),
        name='post-detail'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
