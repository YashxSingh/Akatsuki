from django.http import JsonResponse
from .models import EmployeeData, Goals, PerformanceReview, Feedback, Appraisal, ComplianceData, AttData, CVAData, TSRData
from .serializers import EmployeeDataSerializer, ComplianceDataSerializer, AttDataSerializer, CVADataSerializer, TSRDataSerializer, GoalsSerializer, PerformanceReviewSerializer, FeedbackSerializer, AppraisalSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def employee_data_list(request):
    if request.method == 'GET':
        employees = EmployeeData.objects.all()
        serializer = EmployeeDataSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = EmployeeDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def employeeByID(request, employeeId):
    try:
        employee = EmployeeData.objects.get(empid = employeeId)
    except EmployeeData.DoesNotExist:
        return  Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serilizer = EmployeeDataSerializer(employee)
        return Response(serilizer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = EmployeeDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def goals_list(request):
    if request.method == 'GET':
        goals = Goals.objects.all()
        serializer = GoalsSerializer(goals, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = GoalsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def performance_review_list(request):
    if request.method == 'GET':
        reviews = PerformanceReview.objects.all()
        serializer = PerformanceReviewSerializer(reviews, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = PerformanceReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def feedback_list(request):
    if request.method == 'GET':
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def appraisal_list(request):
    if request.method == 'GET':
        appraisals = Appraisal.objects.all()
        serializer = AppraisalSerializer(appraisals, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = AppraisalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def compliance_data_list(request):
    if request.method == 'GET':
        compliance_data = ComplianceData.objects.all()
        serializer = ComplianceDataSerializer(compliance_data, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = ComplianceDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def att_data_list(request):
    if request.method == 'GET':
        att_data = AttData.objects.all()
        serializer = AttDataSerializer(att_data, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = AttDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def cva_data_list(request):
    if request.method == 'GET':
        cva_data = CVAData.objects.all()
        serializer = CVADataSerializer(cva_data, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = CVADataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def tsr_data_list(request):
    if request.method == 'GET':
        tsr_data = TSRData.objects.all()
        serializer = TSRDataSerializer(tsr_data, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = TSRDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_employee_goals(request, emp_id):
    try:
        goals = Goals.objects.filter(empid=emp_id)
        serialized_goals = GoalsSerializer(goals, many=True).data
        return JsonResponse({"goals": serialized_goals})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def get_employee_performance_and_feedback(request, employee_id):
    try:
        performance_reviews = PerformanceReview.objects.filter(empid=employee_id)
        feedbacks = Feedback.objects.filter(empid=employee_id)

        serialized_performance_reviews = PerformanceReviewSerializer(performance_reviews, many=True).data
        serialized_feedbacks = FeedbackSerializer(feedbacks, many=True).data

        return JsonResponse({
            "performance_reviews": serialized_performance_reviews,
            "feedbacks": serialized_feedbacks
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)