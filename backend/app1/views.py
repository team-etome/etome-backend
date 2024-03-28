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
            user = Admin.objects.get(email_id=email)
        except Admin.DoesNotExist:
            return JsonResponse({'error': 'No admin found with this email'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'An unexpected error occurred: ' + str(e)}, status=500)
        if user.is_school is False:
        
            if user.school is True:
                if check_password(password, user.password):
                    school_token = get_token(user, user_type='school')
                    return JsonResponse({'message': 'Login successful', 'token': school_token})
            elif user.school is False:
                if check_password(password, user.password):
                    college_token = get_token(user, user_type='college')
                    return JsonResponse({'message': 'Login successful', 'token': college_token })
        
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=401)
        else:
                return JsonResponse({'error': 'admin has been blocked '}, status=402)
    def get(self, request,pk):
        try:
            admin = Admin.objects.get(id=pk)
            adminDetails = []

            adminDetails.append({
                'institute_name': admin.institute_name,
                'institute_code': admin.institute_code,
                'eduational_body':admin.eduational_body,
                'email_id': admin.email_id,
                'address': admin.address,
                'phn_number': admin.phn_number,
                'database_code': admin.database_code,
                'region':admin.region,
                'password': admin.password,
                'logo': admin.logo,

            })
            return JsonResponse(adminDetails, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        

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
            
    def get(self, request):
        try:
            admins = Admin.objects.all().order_by('id')
            adminDetails = []

            for admin in admins:
                adminDetails.append({
                    'institute_name': admin.institute_name,
                    'institute_code': admin.institute_code,
                    'eduational_body':admin.eduational_body,
                    'region':admin.region
                })
            return JsonResponse(adminDetails, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

    def put(self,request,pk):

        data=request.data
        id= data.get('pk')

        try:
            admin=Admin.objects.get(id=id)
        except Admin.DoesNotExist:
                return JsonResponse({"error": "Table does not exist"}, status=status.HTTP_404_NOT_FOUND)



        if 'password' in data:
            admin.password=data['password']
            admin.save()
        return JsonResponse({"message": "password updated successfully"}, status=200)


class AddClassName(APIView):
    def post(self,request):
         try:
                data = request.data

                classname_serializer = ClassNameSerializer(data=data)
                
                if classname_serializer.is_valid():
                    classname_serializer.save()
                    return JsonResponse({'message': 'Data saved successfully'}, status=status.HTTP_201_CREATED)
                else:
                    return JsonResponse(classname_serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
         except Exception as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            classnames = ClassName.objects.all().order_by('id')
            classnameDetails = []

            for classname in classnames:
                classnameDetails.append({
                    'class_name': classname.class_name,
                    'division': classname.division,
                })
            return JsonResponse(classnameDetails, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
            data = request.data

            id = data.get('pk')
            classname = ClassName.objects.get(id=id)
        
            if 'class_name' in data:
                classname.class_name = data['class_name']
            if 'division' in data:
                classname.division = data['division']
            classname.save()
            return JsonResponse({"message": "classname updated successfully"}, status=status.HTTP_200_OK)
       


    def delete(self, request, pk):
        try:
            classname = ClassName.objects.get(id=pk)
            classname.delete()
            return JsonResponse(status=status.HTTP_204_NO_CONTENT)
        except ClassName.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
        
class ClassNameDetailsView(APIView):
    def get(self, request,pk):
        try:
            classname = ClassName.objects.get(id=pk)
            classnameDetails = []

            classnameDetails.append({
                    'class_name': classname.class_name,
                    'division': classname.division,
                    'medium': classname.medium,
                    'class_name': classname.class_name,
                    'category': classname.category,
                    'teacher': classname.teacher,
                    'subjects': classname.subjects,
                    'level': classname.level,
                    'class_name': classname.class_name,

                })
            return JsonResponse(classnameDetails, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

