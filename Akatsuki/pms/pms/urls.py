from django.contrib import admin
from django.urls import path
from pms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employeedata/', views.employee_data_list),
    path('employeedata/<int:employeeId>', views.employeeByID),
    path('goals/', views.goals_list),
    path('performancereview/', views.performance_review_list),
    path('feedback/', views.feedback_list),
    path('appraisal/', views.appraisal_list),
    path('compliancedata/', views.compliance_data_list),
    path('attdata/', views.att_data_list),
    path('cvadata/', views.cva_data_list),
    path('tsrdata/', views.tsr_data_list),
]
