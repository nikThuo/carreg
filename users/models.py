from django.db import models

# Create your models here.
#################### USER ROLES ####################
"""
Model for user roles
"""
class User_Roles(models.Model):
    role_id = models.AutoField(auto_created=True, primary_key=True)
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return "User_Role: {}".format(self.role_name)

    class Meta:
        db_table = 'user_role'

#################### USER TYPE ####################
"""
Model for user type
"""
class User_Type(models.Model):
    user_type_id = models.AutoField(auto_created=True, primary_key=True)
    user_name = models.CharField(max_length=100)
    role = models.ForeignKey(User_Roles, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "User_Type: {}".format(self.user_name)

    class Meta:
        db_table = 'user_type'

#################### PARTICIPANTS ####################
"""
Model for authority
"""
class Authority(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    user_type = models.ForeignKey(User_Type, on_delete=models.CASCADE, null=False)
    pwd = models.CharField(max_length=100, default='')

    def __str__(self):
        return "Authority: {}".format(self.name)

    class Meta:
        db_table = 'authority'

"""
Model for agents
"""
class Agent(models.Model):
    # id = models.AutoField(auto_created=True)
    name = models.CharField(max_length=100)
    kra_pin = models.CharField(primary_key=True, max_length=100)
    user_type = models.ForeignKey(User_Type, on_delete=models.CASCADE, null=False)
    pwd = models.CharField(max_length=100, default='')

    def __str__(self):
        return "Agent: {}".format(self.name)

    class Meta:
        db_table = 'agents'

"""
Model for owners
"""
class Owner(models.Model):
    national_id = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    dob = models.DateField()
    kra_pin = models.CharField(max_length=100)
    user_type = models.ForeignKey(User_Type, on_delete=models.CASCADE, null=False)
    pwd = models.CharField(max_length=100, default='')

    def __str__(self):
        return "Owner: {}".format(self.fullname)

    class Meta:
        db_table = 'owners'