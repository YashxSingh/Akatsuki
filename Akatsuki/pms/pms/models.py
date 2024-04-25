from django.db import models

class EmployeeData(models.Model):
    empid = models.CharField(max_length=10)
    name = models.CharField(max_length=500)
    mob = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    l1_manager = models.CharField(max_length=10)
    projid = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ComplianceData(models.Model):
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='compliance_data')
    compliance_done = models.IntegerField(null=True)
    compliance_left = models.IntegerField(null=True)


class AttData(models.Model):
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='attendance_data')
    leaves_taken = models.IntegerField(null=True)
    wfh_taken = models.IntegerField(null=True)
    overtime = models.IntegerField(null=True)
    max_working_days = models.IntegerField(null=True)

class CVAData(models.Model):
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='CVA_data')
    CVA_id = models.CharField(max_length=50)
    CVA_description = models.CharField(max_length=500)
    CVA_feedback = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.CVA_description


class TSRData(models.Model):
    empid = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, null=True, related_name='TSR_data')
    course_name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=15)
    course_description = models.CharField(max_length=500)
    percentage_completion = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.course_name
