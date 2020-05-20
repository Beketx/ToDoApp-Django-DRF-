from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from api.models import Task
from api.serializers import TaskSerializer
from api.models import User
from api.serializers import LoginSerializer, RegistrationSerializer
from api.tasks import send_email_task

class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'token':serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LogoutAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def get(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=False)
        return Response(status=status.HTTP_200_OK)

# @api_view(['POST'])
# @permission_classes([AllowAny,])
# def authenticate_user(request):
#     try:
#         email = request.data['email']
#         password = request.data['password']
#
#         user = User.objects.get(email=email, password=password)
#         if user:
#             try:
#                 payload = jwt_payload_handler(user)
#                 token = jwt.encode(payload, settings.SECRET_KEY)
#                 user_details = {}
#                 user_details['email'] = "%s" % (
#                     user.email
#                 )
#                 user_details['token'] = token
#                 user_logged_in.send(sender=user.__class__,
#                                     request=request, user=user)
#                 return Response(user_details, status=status.HTTP_200_OK)
#             except Exception as e:
#                 raise e
#             else:
#                 res = {
#                     'error': 'can not authenticate with the given credentials'
#                 }
#                 return Response(res, status=status.HTTP_403_FORBIDDEN)
#     except KeyError:
#         res = { 'error': 'please provide a email and a password'}
#         return Response(res)


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class Execution(APIView):
    queryset = Task.objects.all()
    # serializer_class = TaskSerializer
    def get(self,request):
        send_email_task.delay()
        res = {
            'email': 'send'
        }
        return Response(res,status=status.HTTP_200_OK)