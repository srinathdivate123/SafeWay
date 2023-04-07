from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import auth
@api_view(['PUT'])
def RegistrationView(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    if not User.objects.filter(username=username).exists():
        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.is_active = True
            user.save()
            return Response({'reg_response':'Account Successfully Created'})
        return Response({'reg_response':'This email is in use. Choose another one!'})
    return Response({'reg_response':'This username is in use. Choose another one!'})




@api_view(['PUT'])
def LoginView(request):
    email = request.data['email']
    password = request.data['password']
    try:
        user_name = User.objects.get(email=email).username
    except Exception as a:
        return Response({'login_response':'This username does not exist!'})
    
    user = auth.authenticate(username = user_name,password=password)
    if user:
        auth.login(request, user)
        return Response({'login_response': True})
    else:
        return Response({'login_response':'Your credentials are wrong!'})


@api_view(['GET'])
def LogoutView(request):
    auth.logout(request)
    return Response({'logout_response':'Logged out successfully'})