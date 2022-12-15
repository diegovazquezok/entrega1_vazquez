from django.urls import path
from .views import MyPasswordChangeView, MyPasswordResetDoneView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'AppAuth'

urlpatterns = [
    path('change_password/', MyPasswordChangeView.as_view(), name='password_change_view'),
    path('change_password/done/', MyPasswordResetDoneView.as_view(), name='password_change_done_view'),
 ]
