from django.db import models

# Create your models here.


class Country(models.Model):
	Country_Name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.Country_Name

class Customer(models.Model):
    Customer_Id = models.IntegerField(null=False)
    Customer_Name = models.CharField(max_length=200, null=True)
    Open_Date = models.CharField(max_length=200, null=True)
    Last_Consulted_Date = models.CharField(max_length=200, null=True)
    Vaccination_Id = models.CharField(max_length=200, null=True)
    Dr_Name = models.CharField(max_length=200, null=True)
    State = models.CharField(max_length=200, null=True)
    Country = models.CharField(max_length=200, null=True)
    DOB = models.CharField(max_length=200, null=True)
    Is_Active = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.Customer_Name


class CustomerByCountry(models.Model):
    Country = models.ForeignKey(Country, null=True, on_delete= models.SET_NULL)
    Customer_Id = models.IntegerField(null=False)
    Customer_Name = models.CharField(max_length=200, null=True)
    Open_Date = models.CharField(max_length=200, null=True)
    Last_Consulted_Date = models.CharField(max_length=200, null=True)
    Vaccination_Id = models.CharField(max_length=200, null=True)
    Dr_Name = models.CharField(max_length=200, null=True)
    State = models.CharField(max_length=200, null=True)
    DOB = models.CharField(max_length=200, null=True)
    Is_Active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Country.Country_Name
