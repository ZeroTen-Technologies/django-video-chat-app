from django.urls import path
from .views import video_view


urlpatterns = [
	path('', video_view, name='video_view'),
]