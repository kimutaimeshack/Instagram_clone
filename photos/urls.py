from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from photos import views
from .views import BlogCreateView

urlpatterns =[
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    url(r'^one/', views.postdetail, name='postdetail'),
    url(r'^todays/', views.news_today, name = 'newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^article/(\d+)',views.article,name ='article'),
    url(r'^$', views.index, name='index'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    