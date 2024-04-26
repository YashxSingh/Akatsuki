from django.db import models

class EmployeeData(models.Model):
    GENDER_CHOICES = (('SELECT', 'Select'), ('MALE', 'Male'), ('FEMALE', 'Female'),('OTHER', 'Other'))
    HORIZONTAL_CHOICES = (('SELECT', 'Select'), ('ES', 'Enterprise Services'), ('IMS', 'Application Management'), ('BPS', 'Business Processes'))
    VERTICAL_CHOICES = (('SELECT', 'Select'), ('M&C', 'Manufacturing'), ('BFS', 'Banking and Financial sevices'), ('GTT', 'GTT'))

    empid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=500)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='SELECT', null=True)
    mob = models.CharField(max_length=12)
    email = models.EmailField(max_length=254, unique=True, null=True)
    address = models.CharField(max_length=500)
    l1_manager = models.CharField(max_length=10)
    projid = models.CharField(max_length=50)
    horizontal = models.CharField(max_length=50, choices=HORIZONTAL_CHOICES, default='SELECT', null=True)
    vertical = models.CharField(max_length=50, choices = VERTICAL_CHOICES, default='SELECT', null=True)
    joining_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Goals(models.Model):
    goal_id = models.AutoField(primary_key=True)
    goal_description = models.TextField()
    due_date = models.DateField(blank=True, null=True)
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name="goals", default='', blank=True)

    def __str__(self):
        return f"Goal {self.goal_id} for Employee {self.empid}"

class PerformanceReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='employee_reviews', default='', blank=True)
    reviewer_id = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='reviewer_reviews')
    performance_rating = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField()

    def __str__(self):
        return f"Review {self.review_id} for Employee {self.empid}"
    

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='feedback', default='', blank=True)
    feedback_text = models.TextField()

    def __str__(self):
        return f"Feedback {self.feedback_id} for Employee {self.empid}"

class Appraisal(models.Model):
    appraisal_id = models.AutoField(primary_key=True)
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='employee_appraisal', default='', blank=True)
    appraisal_date = models.DateField(blank=True, null=True)
    appraisal_score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Appraisal {self.appraisal_id} for Employee {self.empid}"


class ComplianceData(models.Model):
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='compliance_data', default='', blank=True)
    compliance_done = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.compliance_done} Compliance trainings done from {self.compliance_total}"


class AttData(models.Model):
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='attendance_data', default='', blank=True)
    leaves_taken = models.IntegerField(null=True)
    wfh_taken = models.IntegerField(null=True)
    overtime = models.IntegerField(null=True)
    max_working_days = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.leaves_taken} leaves taken, {self.wfh_taken} wfh taken, {self.overtime}, in {self.max_working_days} days in a year"


class CVAData(models.Model):
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='CVA_data', default='', blank=True)
    CVA_id = models.AutoField(primary_key=True)
    CVA_description = models.CharField(max_length=500)
    CVA_feedback = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.CVA_description


class TSRData(models.Model):
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='TSR_data', default='', blank=True)
    course_name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=15)
    course_description = models.CharField(max_length=500)
    percentage_completion = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.course_name
