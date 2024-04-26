from django.contrib import admin
from .models import EmployeeData, ComplianceData, AttData, CVAData, TSRData, Goals, PerformanceReview, Feedback, Appraisal

admin.site.register(EmployeeData)
admin.site.register(ComplianceData)
admin.site.register(AttData)
admin.site.register(CVAData)
admin.site.register(TSRData)
admin.site.register(Goals)
admin.site.register(PerformanceReview)
admin.site.register(Feedback)
admin.site.register(Appraisal)
