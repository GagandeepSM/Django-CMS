from django.urls import path
from . import views
from .views import ContentListView, ContentDetailView, ContentCreateView, ContentUpdateView, ContentDeleteView, UserContentListView

urlpatterns = [
    path('', ContentListView.as_view(), name = 'basic-cms-home'),
    path('user/<str:username>', UserContentListView.as_view(), name = 'user-content'),
    path('about/', views.about_page, name = 'basic-cms-about'),
    path('content/new/', ContentCreateView.as_view(), name='content-create'),
    path('content/<int:pk>/', ContentDetailView.as_view(), name = 'content-detail'),
    path('content/<int:pk>/update/', ContentUpdateView.as_view(), name = 'content-update'),
    path('content/<int:pk>/delete/', ContentDeleteView.as_view(), name = 'content-delete'),
] 
