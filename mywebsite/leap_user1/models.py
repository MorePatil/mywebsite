from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Department(models.Model):
    title = models.CharField(max_length=100)

class Role(models.Model):
    title = models.CharField(max_length=100)

def _get_roles():
        roles_List = []
        for i in Role.objects.all():  
            roles_List.append((i.id, i.title))
        return roles_List


def _get_department():
        department_List = []
        for i in Department.objects.all():#.values('title', 'id')
            department_List.append((i.id,i.title))
        print department_List
        return  department_List

class fields(models.Model):
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True) 
    L1_manage = models.CharField(max_length=200,blank=True,null=True)  
    Active = models.CharField(choices=[(1,'Yes'),(0,'No')],max_length=200) 
    created_date = models.DateTimeField(
            default=timezone.now)
    data_of_joining = models.DateTimeField(
            blank=True, null=True)
    role =  models.CharField(choices=_get_roles(),blank=True,null=True,max_length=200)
    department = models.CharField(choices=_get_department(),blank=True,null=True,max_length=200)

    def __str__(self):
        return self.title
