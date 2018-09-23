from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)   
  
    def __str__(self):
        return f"{self.name}"
     

class Pick(models.Model):
    name = User.name
    pick1 = models.CharField(max_length=50)
    pick2 = models.CharField(max_length=50)
    pick3 = models.CharField(max_length=50)
    pick4 = models.CharField(max_length=50)
    pick5 = models.CharField(max_length=50)
    pick6 = models.CharField(max_length=50)
    pick7 = models.CharField(max_length=50)
    pick8 = models.CharField(max_length=50)
    pick9 = models.CharField(max_length=50)
    pick10 = models.CharField(max_length=50)
    pick11 = models.CharField(max_length=50)
    pick12 = models.CharField(max_length=50)
    pick13 = models.CharField(max_length=50)
    pick14 = models.CharField(max_length=50)
    pick15 = models.CharField(max_length=50)
    pick16 = models.CharField(max_length=50)
    totalPtsMonday = models.IntegerField()
    totalCorrect = models.IntegerField()
    submission_date = models.DateTimeField()
    users = models.ManyToManyField(User, blank=True, related_name="user")
    
    def __str__(self):
       return f"Pick 1: {self.pick1} Pick 2: {self.pick2} Pick 3: {self.pick3} Pick 4: {self.pick4} Pick 5: {self.pick5} Pick 6: {self.pick6} Pick 7: {self.pick7} Pick 8: {self.pick8}Pick 1: {self.pick9}Pick 1: {self.pick10}Pick 1: {self.pick11}Pick 1: {self.pick12}Pick 1: {self.pick13}Pick 1: {self.pick14}Pick 1: {self.pick15}Pick 1: {self.pick16}"


