from django.db import models

class UserRole(models.Model):
    role_name = models.CharField(max_length=100)
    role_detail = models.CharField(max_length=100)
    def __str__(self):
        return self.role_name


class UserTable(models.Model):
    #roles = (( 1,"admin"),(2,"guest"),(3,"user"))
    user_name= models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_pwd = models.CharField(max_length=100)
    user_contact = models.IntegerField()
    user_address = models.CharField(max_length=100)
    #role = models.CharField(max_length=100,choices=roles)
    role = models.ForeignKey(UserRole,on_delete=models.CASCADE,default='Select Role')
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name


class UserRights(models.Model):
    role = models.ForeignKey(UserRole,on_delete=models.CASCADE,default='Select Role')
    rights_name = models.CharField(max_length=100)
    rights_details = models.CharField(max_length=100)

    def __str__(self):
        return self.rights_name,self.rights_details

