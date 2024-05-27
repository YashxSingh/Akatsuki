from rest_framework import serializers
from .models import EmployeeData, Goals, PerformanceReview, Feedback, Appraisal, ComplianceData, AttData, CVAData, TSRData, SelfComments

class ComplianceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceData
        fields = ['empid', 'compliance_done', 'compliance_total']

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

class AppraisalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appraisal
        fields = ['appraisal_id', 'empid', 'appraisal_date', 'appraisal_score']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['feedback_id', 'empid', 'feedback_text']

class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = ['review_id', 'empid', 'reviewer_id', 'performance_rating', 'comments']

class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = ['goal_id', 'goal_description', 'due_date', 'empid']

class SelfCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfComments
        fields = ['emp_id', 'process_compliance', 'learning_and_development',
                  'team_collaboration', 'delivery', 'communication', 'customer_focus']

class EmployeeDataSerializer(serializers.ModelSerializer):
    ComplianceData_var = ComplianceDataSerializer(many = True, read_only = True)
    AttData_var = AttDataSerializer(many = True, read_only = True)
    CVAData_var = CVADataSerializer(many = True, read_only = True)
    TSRData_var = TSRDataSerializer(many = True, read_only = True)
    Goals_var = GoalsSerializer(many = True, read_only = True)
    PerformanceReview_var = PerformanceReviewSerializer(many = True, read_only = True)
    Feedback_var = FeedbackSerializer(many = True, read_only = True)
    Appraisal_var = AppraisalSerializer(many = True, read_only = True)
    SelfComments_var = SelfCommentsSerializer(many = True, read_only = True)
    class Meta:
        model = EmployeeData
        fields = ['empid', 'name', 'gender', 'mob', 'email', 'address', 'l1_manager', 'projid', 'horizontal', 'vertical', 'joining_date', 'ComplianceData_var', 'AttData_var', 'CVAData_var', 'TSRData_var', 'Goals_var', 'PerformanceReview_var', 'Feedback_var', 'Appraisal_var', 'SelfComments_var']