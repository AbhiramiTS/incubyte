from django.test import TestCase
from . models import *
from . views import CustomerByCountryFunc
from django.utils import timezone, tree

# models test
class CustomerTest(TestCase):

    def create_customer(self, 
    Customer_Name = "Customer A",
    Customer_Id = 135123,
    Open_Date = timezone.now(),
    Last_Consulted_Date = timezone.now(),
    Vaccination_Id = 'NSD',
    Dr_Name = 'DR',
    State = 'STATE',
    Country = 'COUNTRY',
    DOB = timezone.now(),
    Is_Active = False
    ):
        """Set up customer fixtures"""
        return Customer.objects.create(
        Customer_Name =Customer_Name,
        Customer_Id = Customer_Id,
        Open_Date = Open_Date,
        Last_Consulted_Date = Last_Consulted_Date,
        Vaccination_Id = Vaccination_Id,
        Dr_Name = Dr_Name,
        State = State,
        Country = Country,
        DOB = DOB,
        Is_Active = Is_Active
            )

    def test_customer_creation(self):
        """Creating / Inserting values to Customer Table"""
        c = self.create_customer()
        self.assertTrue(isinstance(c, Customer))
        self.assertEqual(c.__str__(), c.Customer_Name)


    def test_customer_by_country_view(self):
        """Loading customer data to corresponding country tables"""
        c = self.create_customer()
        customer = Customer.objects.all()
        self.assertTrue(isinstance(CustomerByCountryFunc(customer),CustomerByCountry ))