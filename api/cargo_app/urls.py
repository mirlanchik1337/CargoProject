from django.urls import path

from api.cargo_app import views

urlpatterns = [
    path('trackcode/create/', views.TrackCodeCreate.as_view(), name='create TrackCode'),
    path('trackcode/get/all/', views.TrackCodeList.as_view(), name='create TrackCode'),
    path('trackcode/get/<int:id>/', views.TrackCodeGet.as_view(), name='get TrackCode'),
    path('trackcode/update/<int:id>/', views.TrackCodeUpdate.as_view(), name='update TrackCode'),
    path('trackcode/delete/<int:id>/', views.TrackCodeDelete.as_view(), name='delete TrackCode'),
    path('status/delete/<int:id>/', views.StatusDelete.as_view(), name='delete status'),
    path('status/list/', views.StatusList.as_view(), name='List Status'),
    path('check/trackcode/', views.CheckTrackCodeView.as_view(), name='check TrackCode'),
    path('group/trackcode/delete/', views.GroupTrackCodeDelete.as_view(), name='delete trackcode from group'),
    path('group/list/', views.GroupListApiView.as_view(), name='List Group'),
    path('group/create/', views.GroupUpdateApiView.as_view(), name='create Group'),
    path('group/get/<int:id>/', views.GroupGet.as_view(), name='get Group'),
    path('group/update/<int:id>/', views.GroupUpdate.as_view(), name='update Group'),

]