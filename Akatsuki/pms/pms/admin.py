from django.contrib import admin
from .models import EmployeeData, ComplianceData, AttData, CVAData, TSRData

admin.site.register(EmployeeData)
admin.site.register(ComplianceData)
admin.site.register(AttData)
admin.site.register(CVAData)
admin.site.register(TSRData)