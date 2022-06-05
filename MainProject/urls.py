from django.contrib import admin
from django.urls import path, include
from blog import urls as blog_urls
from blog.views import home
from account import urls as account_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blog_urls)),
    path('account/', include(account_urls),name='account'),
    path('', home, name="index"),
]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)