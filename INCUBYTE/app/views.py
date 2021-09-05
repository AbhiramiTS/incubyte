from django.shortcuts import render
from .models import *
from datetime import datetime
from datetime import datetime, timedelta



def CustomerByCountryFunc(customer_data):
    """ splitting the customers based on the country and loading them into corresponding country tables"""
    for data in customer_data:
        country = data.Country
        try:
            country_obj = Country.objects.get(Country_Name= country)
        except:
            country_obj = Country.objects.create(Country_Name= country)
            country_obj.save()
        finally:
            try:
                customer_by_country = CustomerByCountry.objects.get(Customer_Id = data.Customer_Id)
            except:
                customer_by_country = CustomerByCountry.objects.create(Country = country_obj,
                Customer_Id= data.Customer_Id,
                Customer_Name= data.Customer_Name,
                Open_Date = data.Open_Date,
                Last_Consulted_Date = data.Last_Consulted_Date,
                Vaccination_Id = data.Vaccination_Id,
                Dr_Name = data.Dr_Name,
                State = data.State ,
                DOB = data.DOB,
                Is_Active = True if data.Is_Active == 'A' else False)
                customer_by_country.save()
    return customer_by_country

def UploadFile(request):
    """Save data to Customer Table from uploaded File (txt)"""
    if request.method == "POST":
        customer_data = request.FILES["cust_data"]
        print(customer_data)
        for data in customer_data:
            array_header = data.decode('utf8').strip().split("|")
            if array_header[1] == 'D':
                Open_Date_str = array_header[4]
                Open_Date = datetime(year=int(Open_Date_str[0:4]), month=int(Open_Date_str[4:6]), day=int(Open_Date_str[6:8])).date()
                Last_Consulted_Date_str = array_header[5]
                Last_Consulted_Date = datetime(year=int(Last_Consulted_Date_str[0:4]), month=int(Last_Consulted_Date_str[4:6]), day=int(Last_Consulted_Date_str[6:8])).date()
                DOB_str = array_header[10]
                DOB = datetime(day=int(DOB_str[0:2]), month=int(DOB_str[2:4]), year=int(DOB_str[4:8])).date()
                try:
                    customer_obj = Customer.objects.get(Customer_Id=int(array_header[3]))
                except:
                    customer_obj = Customer.objects.create(Customer_Id= int(array_header[3]),
                    Customer_Name= array_header[2],
                    Open_Date = Open_Date,
                    Last_Consulted_Date = Last_Consulted_Date,
                    Vaccination_Id = array_header[6],
                    Dr_Name = array_header[7],
                    State = array_header[8] ,
                    Country = array_header[9] ,
                    DOB = DOB,
                    Is_Active = True if array_header[11] == 'A' else False)
                    customer_obj.save()

        customer_data = Customer.objects.all()
        customer_by_country = CustomerByCountryFunc(customer_data)
        country = Country.objects.all()
        context = {"customer_data":customer_data, "country":country, "created":1}
        return render(request, "home.html",context)
    else:
        return render(request, "home.html")
