from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  url(r'^$', views.index, name='homepage'),
  url(r'register', views.register_user, name='register'),
  url(r'login', views.login_user, name='login'),
  url(r'logout', views.logout_user, name='logout'),
  url(r'^profile/(?P<user_id>\d+)', views.profile, name='profiles'),
  url(r'update_profile', views.update_profile, name='update_profile')
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)