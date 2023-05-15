from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    title=models.CharField(max_length=200)
    campus=models.CharField(max_length=200)
    emailaddress=models.CharField(max_length=100)
    postbox=models.CharField(max_length=100)
     
    def __str__(self):
        return f"{self.title} - {self.campus}"
    class Meta:
        ordering=['title','campus']

class Logs(models.Model):
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    startdate=models.DateField()
    enddate=models.DateField()
    activityDone=models.TextField(max_length=2000)
    newSkillsAquired=models.TextField(max_length=2000)
    challangesMet=models.TextField(max_length=500)
    def __str__(self):
        return f"Logs for {self.startdate} - {self.enddate}"
    

class Attachment(models.Model):
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    logs=models.ForeignKey(Logs, on_delete=models.CASCADE)
    def __str__(self):
        return f"Attachment {self.student}"

class Department(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.title} Department"
    
class Student(models.Model):
    username=models.CharField(max_length=100)
    institution=models.ForeignKey(Institution, on_delete=models.CASCADE)
    refcode=models.CharField(max_length=50)
    phone=models.CharField(max_length=50, null=True, blank=True)
    startdate=models.DateField()
    enddate=models.DateField()
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.username} - {self.institution}"
    
class Supervisor(models.Model):
    supervisor=models.ForeignKey(User, on_delete=models.CASCADE)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.supervisor} - {self.department}"
    