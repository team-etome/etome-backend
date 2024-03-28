from rest_framework import status
from rest_framework.views import APIView
from app1.models import *
from app1.serializers import * 
from app1.token import get_token
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
import pandas as pd

class UploadExcelTeacher(APIView):
    def post(self, request, *args, **kwargs):
        excel_file = request.FILES.get('file')

        if not excel_file:
            return JsonResponse({'error': 'No file uploaded.'}, status=400)
        
        try:
        
            df = pd.read_excel(excel_file, engine='openpyxl')
            for _, row in df.iterrows():
               
                
          
                Teacher.objects.update_or_create(
                    defaults={
                        'first_name': row['First Name'],
                        'last_name': row['Last Name'],
                        'email': row['Email'],
                        'phone_number': row.get('Contact Number', None),
                        'password': row.get('Password', None),
                        'gender': row.get('Gender', None),

                        
                    }
                )
            
            return JsonResponse({'message': 'Excel file processed successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
class TeacherLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('emailid')
        password = request.data.get('password')

        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=400)

        try:
            user = Teacher.objects.get(email_id=email)
        except Teacher.DoesNotExist:
            return JsonResponse({'error': 'No teacher found with this email'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'An unexpected error occurred: ' + str(e)}, status=500)
        
        if check_password(password, user.password):
            teacher_token = get_token(user, user_type='teacher')
            return JsonResponse({'message': 'Login successful', 'token': teacher_token})
       
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)
        
    def put(self,request):

        data=request.data
        id= data.get('pk')

        try:
            teacher=Teacher.objects.get(id=id)
        except Teacher.DoesNotExist:
                return JsonResponse({"error": "teacher does not exist"}, status=status.HTTP_404_NOT_FOUND)



        if 'subject' in data:
            teacher.subject=data['subject']
            teacher.save()
        return JsonResponse({"message": "subject updated successfully"}, status=200)
    def get(self, request,pk):
        try:
            teacher = Teacher.objects.get(id=pk)
            teacherDetails = []

                

            teacherDetails.append({
                'first_name': teacher.first_name,
                'last_name': teacher.last_name,
                'email': teacher.email,
                'phone_number': teacher.phone_number,
                'password': teacher.password,
                'gender': teacher.gender,
                'subject': teacher.subject,

            })
            

            return JsonResponse(teacherDetails, safe=False)
        except Exception as e:
            return JsonResponse({'error': f"An error occurred: {e}"}, status=500)

        
class TeacherDetails(APIView):
    def get(self, request):
        try:
            teachers = Teacher.objects.all().order_by('id')
            teacherDetails = []

            for teacher in teachers:
                try:
                    

                    teacherDetails.append({
                        'first_name': teacher.first_name,
                        'last_name': teacher.last_name,
                        'email': teacher.email,

                    })
                except Exception as e:
                    return JsonResponse("Error processing details for teacher with ID ")

            return JsonResponse(teacherDetails, safe=False)

        except Exception as e:
            return JsonResponse({'error': f"An error occurred: {e}"}, status=500)
        

    


    def delete(self , request , pk):
        try:
            teacher = Teacher.objects.get(id=pk)
            teacher.delete()
            return JsonResponse({'message': 'Teacher deleted successfully'},status=status.HTTP_204_NO_CONTENT)
        except Teacher.DoesNotExist:
            return JsonResponse({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    





