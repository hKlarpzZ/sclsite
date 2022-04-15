from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)