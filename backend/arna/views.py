from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import * 
from django.http import JsonResponse

class QuestionPaperdetails(APIView):

    def post(self , request):
        data = request.data
        questionpaper_serializer  = QuestionPaperSerializer(data = data)
        if questionpaper_serializer.is_valid():
            questionpaper_serializer.save(status='assigned')
            return JsonResponse({'message': 'Data saved successfully'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(questionpaper_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def get(self , request):

        questionpapers = QuestionPaper.objects.all().order_by('id')
        questionpaperdetails = []

        for question in questionpapers:
            class_name = question.class_name.class_name
            subject=question.subject.subject
            if question.teacher is not None:
                Teacher = f"{question.teacher.first_name} {question.teacher.last_name}"
            else:
                Teacher = "No Teacher Assigned"

            questionpaperdetails.append({

                'id'             :  question.id,
                'ExamName'       :  question.exam_name,
                'subject'        :  subject,
                'exam_date'      :  question.exam_date,
                'Teacher'        :  Teacher,

            })

        return JsonResponse(questionpaperdetails, safe=False)       


class BlueprintDetailView(APIView):

    def get(self, request, id):
        try:
            qpaper = QuestionPaper.objects.get(id=id)
            serializer = QuestionPaperSerializer(qpaper)  
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except QuestionPaper.DoesNotExist:
            return JsonResponse({"detail": "Blueprint not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': f"An error occurred: {e}"}, status=500)        