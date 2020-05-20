from django.urls import path
from api.views import RegistrationAPIView,LoginAPIView,LogoutAPIView, TaskList,TaskDetails, Execution

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('todo/', TaskList.as_view()),
    path('todo/<int:pk>', TaskDetails.as_view()),
    path('execution/', Execution.as_view())
]