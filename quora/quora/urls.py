from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('question/', include('blog.urls')),
    path('categories/', views.categories, name="categories"),
]
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
