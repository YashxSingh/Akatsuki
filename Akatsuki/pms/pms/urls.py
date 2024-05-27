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
    path('get_employee_goals/<int:emp_id>', views.get_employee_goals),
    path('get_employee_rnf/<int:employee_id>', views.get_employee_performance_and_feedback),
    path('selfcmt/<int:emp_id>', views.self_comments),
    path('postcmt/', views.post_comments),
    path('getfeedback/<int:emp_id>/<str:qual>', views.get_feedback),
]
