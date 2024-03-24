from django.urls import path
from .views import SignUpView, LoginView, ProfileDetailView, ProfileUpdateView, logout_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'), 
    path('profile/edit/<int:pk>/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/edit/<int:pk>/', ProfileUpdateView.as_view(), name='update_profile'),
    path('logout/', logout_view, name='logout'),
]








    
   
    



    
    
    
    
    
    
