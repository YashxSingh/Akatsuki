from rest_framework import serializers
from .models import EmployeeData, ComplianceData, AttData, CVAData, TSRData

class ComplianceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceData
        fields = ['empid', 'compliance_done', 'compliance_left']

class AttDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttData
        fields = ['empid', 'leaves_taken', 'wfh_taken', 'overtime', 'max_working_days']

class CVADataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVAData
        fields = ['empid', 'CVA_id', 'CVA_description', 'CVA_feedback']

class TSRDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TSRData
        fields = ['empid', 'course_name', 'course_id', 'course_description', 'percentage_completion']

class EmployeeDataSerializer(serializers.ModelSerializer):
    ComplianceData_var = ComplianceDataSerializer(many = True, read_only = True)
    AttData_var = AttDataSerializer(many = True, read_only = True)
    CVAData_var = CVADataSerializer(many = True, read_only = True)
    TSRData_var = TSRDataSerializer(many = True, read_only = True)
    class Meta:
        model = EmployeeData
        fields = ['empid', 'name', 'mob', 'email', 'address', 'l1_manager', 'projid', 'ComplianceData_var', 'AttData_var', 'CVAData_var', 'TSRData_var']