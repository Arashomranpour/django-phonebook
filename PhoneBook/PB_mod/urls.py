from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    
    path("home",views.home,name="home"),
    path("signup",views.signup,name="signup"),
    path("logout", views.Logoout, name="logout"),
    path("create", views.create, name="create"),
    path('add/', views.AddRecordView.as_view(), name='add_record'),
    path('edit/<int:pk>/', views.RecordUpdateView.as_view(), name='Record'),
     path('delete/<int:pk>/', views.RecordDeleteView.as_view(), name='delete_record'),

]
