from django.http import JsonResponse
from .models import EmployeeData, ComplianceData, AttData, CVAData, TSRData
from .serializers import EmployeeDataSerializer, ComplianceDataSerializer, AttDataSerializer, CVADataSerializer, TSRDataSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        employeedata = EmployeeData.objects.all()
        serializer = EmployeeDataSerializer(employeedata, many = True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = EmployeeDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        