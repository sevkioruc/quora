from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "question"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('add/', views.addQuestion, name="addquestion"),
    path('<str:category>', views.getSingleCategory, name="get"),
    path('detail/<int:id>', views.getQuestion, name="detail"),
    path('answer/<int:id>', views.addAnswer, name="answer")
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
