from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import * 
from . token import get_token
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse


class GodLoginView(APIView):
    

    def post(self, request, *args, **kwargs):
        try:
            email     =  request.data.get('email')
            password  =  request.data.get('password')

            if not email or not password:
             return JsonResponse({'error': 'Email and password are required'}, status=400)

            try:
                user = God.objects.get(email = email)
            except God.DoesNotExist:
                return JsonResponse({'error': 'No user found with this email'}, status=404)
            except Exception as e:
             return JsonResponse({'error': 'An unexpected error occurred: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            if check_password(password, user.password):


                admin_token = get_token(user , user_type='god')
                return JsonResponse({'message': 'Login successful','token' : admin_token })
            
            else:

                return JsonResponse({'error': 'Invalid email or password'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class AdminLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('emailid')
        password = request.data.get('password')

        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=400)

        try:
            user = Admin.objects.get(emailid=email)
        except Admin.DoesNotExist:
            return JsonResponse({'error': 'No admin found with this email'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'An unexpected error occurred: ' + str(e)}, status=500)
        

        if check_password(password, user.password):
            admin_token = get_token(user, user_type='admin')
            return JsonResponse({'message': 'Login successful', 'token': admin_token})
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)
        

class AddAdmin(APIView):
    def post(self, request):
            try:
                data = request.data

                admin_serializer = AdminSerializer(data=data)

                if admin_serializer.is_valid():
                    admin_serializer.save()
                    return JsonResponse({'message': 'Data saved successfully'}, status=status.HTTP_201_CREATED)
                else:
                    return JsonResponse(admin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
            except Exception as e:
             return JsonResponse({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
