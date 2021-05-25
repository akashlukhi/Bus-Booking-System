from django.shortcuts import redirect, render
from .models import bus_info,booked_seat,passenger_detail
from django.http import HttpResponseRedirect
import datetime
from datetime import date
from Blue_Bus.utils import render_to_pdf 
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

def home(request):
    user = request.user
    if request.user.is_authenticated:
        return render(request,'home.html',{'user':user})
    else:
        return render(request,'home.html',{'user':'nouser'})

def ticketbook(request):
    current_user = request.user
    if request.user.is_authenticated:
        return render(request,"ticketbook.html")
    else:
        return HttpResponseRedirect('/loginmodule/login/')

def show(request):
    src = request.POST.get('source','')
    dest = request.POST.get('destination','')
    d = datetime.datetime.strptime(request.POST.get('date'),"%Y-%m-%d").date()
    current_user = request.user
    if request.user.is_authenticated:
        if d < date.today():
            return render(request,"ticketbook.html")
        else:
            bus_list = bus_info.objects.filter(source=src).filter(destination=dest).filter(date=d)
            return render(request,"showlist.html",{'info':bus_list})
    else:
        return HttpResponseRedirect('/loginmodule/login/')
    
def showbus(request,key):
    bus = bus_info.objects.filter(plate_no=key)
    return render(request,'details.html',{'n':bus})

def seat(request):
    seats=request.POST.getlist('checked[]')
    key = seats[0]
    no=[]
    i = 1
    query = bus_info.objects.filter(plate_no=key)
    count = 0
    if len(seats) == 1: #zero seat selected
        return render(request,'details.html',{'n':query})
    for s in seats:
        no.append(i)
        i = i + 1
        count = count + 1
    no = no[:-1]
    count = count - 1
    price = count * query[0].rate
    return render(request,'checkout.html',{'source':query[0].source , 'destination':query[0].destination , 'no_of_passenger':count , 'price':price , 'pk':seats , 'no':no})


def confirme(request):
    i = 0
    data = []
    now = datetime.datetime.now()   
    seats = request.POST.getlist('checked[]')
    name = request.POST.getlist('name[]')
    email = request.POST.getlist('email[]')
    mobile = request.POST.getlist('mobile[]')
    age = request.POST.getlist('age[]')
    gender = request.POST.getlist('gender[]')
    key = seats.pop(0)
    query = bus_info.objects.filter(plate_no=key)
    data.extend((query[0].rate,query[0].bus_name,query[0].source,query[0].destination,query[0].boarding_time,query[0].departure_time))
    current_user = request.user
    if "U1" in seats:
        bus_info.objects.filter(plate_no=key).update(U1=True)
    if "U2" in seats:
        bus_info.objects.filter(plate_no=key).update(U2=True)
    if "U3" in seats:
        bus_info.objects.filter(plate_no=key).update(U3=True)
    if "U4" in seats:
        bus_info.objects.filter(plate_no=key).update(U4=True)
    if "U5" in seats:
        bus_info.objects.filter(plate_no=key).update(U5=True)
    if "U6" in seats:
        bus_info.objects.filter(plate_no=key).update(U6=True)
    if "U7" in seats:
        bus_info.objects.filter(plate_no=key).update(U7=True)
    if "U8" in seats:
        bus_info.objects.filter(plate_no=key).update(U8=True)
    if "U9" in seats:
        bus_info.objects.filter(plate_no=key).update(U9=True)
    if "U10" in seats:
        bus_info.objects.filter(plate_no=key).update(U10=True)
    if "U11" in seats:
        bus_info.objects.filter(plate_no=key).update(U11=True)
    if "U12" in seats:
        bus_info.objects.filter(plate_no=key).update(U12=True)
    if "U13" in seats:
        bus_info.objects.filter(plate_no=key).update(U13=True)
    if "U14" in seats:
        bus_info.objects.filter(plate_no=key).update(U14=True)
    if "U15" in seats:
        bus_info.objects.filter(plate_no=key).update(U15=True)
    if "U16" in seats:
        bus_info.objects.filter(plate_no=key).update(U16=True)
    if "U17" in seats:
        bus_info.objects.filter(plate_no=key).update(U17=True)
    if "U18" in seats:
        bus_info.objects.filter(plate_no=key).update(U18=True)
    if "L1" in seats:
        bus_info.objects.filter(plate_no=key).update(L1=True)
    if "L2" in seats:
        bus_info.objects.filter(plate_no=key).update(L2=True)
    if "L3" in seats:
        bus_info.objects.filter(plate_no=key).update(L3=True)
    if "L4" in seats:
        bus_info.objects.filter(plate_no=key).update(L4=True)
    if "L5" in seats:
        bus_info.objects.filter(plate_no=key).update(U5=True)
    if "L6" in seats:
        bus_info.objects.filter(plate_no=key).update(L6=True)
    if "L7" in seats:
        bus_info.objects.filter(plate_no=key).update(L7=True)
    if "L8" in seats:
        bus_info.objects.filter(plate_no=key).update(L8=True)
    if "L9" in seats:
        bus_info.objects.filter(plate_no=key).update(L9=True)
    if "L10" in seats:
        bus_info.objects.filter(plate_no=key).update(L10=True)
    if "L11" in seats:
        bus_info.objects.filter(plate_no=key).update(L11=True)
    if "L12" in seats:
        bus_info.objects.filter(plate_no=key).update(L12=True)
    if "L13" in seats:
        bus_info.objects.filter(plate_no=key).update(L13=True)
    if "L14" in seats:
        bus_info.objects.filter(plate_no=key).update(L14=True)
    if "L15" in seats:
        bus_info.objects.filter(plate_no=key).update(L15=True)
    if "L16" in seats:
        bus_info.objects.filter(plate_no=key).update(L16=True)
    if "L17" in seats:
        bus_info.objects.filter(plate_no=key).update(L17=True)
    if "L18" in seats:
        bus_info.objects.filter(plate_no=key).update(L18=True)
    for s in seats:
        booked_seat.objects.create(seat_no=s,plate_no=key,user_name=current_user,booked_time=now)
        passenger_detail.objects.create(seat_no=s,passenger_name=name[i],email=email[i],mobile_no=mobile[i],age=age[i],gender=gender[i],booked_by=current_user,source=query[0].source,destination=query[0].destination,bus_plate_no=key,bus_name=query[0].bus_name)
        data.extend((name[i],gender[i],age[i],s))
        i = i + 1
    print(data)
    return render(request,'thankyou.html',{'d':data})


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = request.GET.getlist('d[]')
        count = 0
        name = []
        email = []
        gender = []
        age = []
        seat= []
        rate =data.pop(0)
        b_name = data.pop(0)
        source = data.pop(0)
        dest = data.pop(0)
        boarding = data.pop(0)
        desti = data.pop(0)
        while len(data)!=0:
            count =count + 1
            name.append(data.pop(0))
            gender.append(data.pop(0))
            age.append(data.pop(0))
            seat.append(data.pop(0))
        rate = int(rate) * count
        pdf = render_to_pdf('ticket.html',{'rate':rate,'bus_name':b_name,'source':source,'dest':dest,'b_time':boarding,'d_time':desti,'name':name,'gender':gender,'age':age,'seat':seat})
        return HttpResponse(pdf, content_type='application/pdf')
        
            
def cancel_booking(request):
    current_user = request.user
    if request.user.is_authenticated:
        array = passenger_detail.objects.filter(booked_by=current_user)
        return render(request,'cancel.html',{'a':array})
    else:
        return HttpResponseRedirect('/loginmodule/login/')

def remove(request,param1,param2):
    passenger_detail.objects.filter(bus_plate_no=param1).filter(seat_no=param2).delete()
    booked_seat.objects.filter(seat_no=param2).filter(plate_no=param1).delete()
    if param2 == "U1":
        bus_info.objects.filter(plate_no=param1).update(U1=False)
    elif param2 == "U2":
        bus_info.objects.filter(plate_no=param1).update(U2=False)
    elif param2 == "U3":
        bus_info.objects.filter(plate_no=param1).update(U3=False)
    elif param2 == "U4":
        bus_info.objects.filter(plate_no=param1).update(U4=False)
    elif param2 == "U5":
        bus_info.objects.filter(plate_no=param1).update(U5=False)
    elif param2 == "U6":
        bus_info.objects.filter(plate_no=param1).update(U6=False)
    elif param2 == "U7":
        bus_info.objects.filter(plate_no=param1).update(U7=False)
    elif param2 == "U8":
        bus_info.objects.filter(plate_no=param1).update(U8=False)
    elif param2 == "U9":
        bus_info.objects.filter(plate_no=param1).update(U9=False)
    elif param2 == "U10":
        bus_info.objects.filter(plate_no=param1).update(U10=False)
    elif param2 == "U11":
        bus_info.objects.filter(plate_no=param1).update(U11=False)
    elif param2 == "U12":
        bus_info.objects.filter(plate_no=param1).update(U12=False)
    elif param2 == "U13":
        bus_info.objects.filter(plate_no=param1).update(U13=False)
    elif param2 == "U14":
        bus_info.objects.filter(plate_no=param1).update(U14=False)
    elif param2 == "U15":
        bus_info.objects.filter(plate_no=param1).update(U15=False)
    elif param2 == "U16":
        bus_info.objects.filter(plate_no=param1).update(U16=False)
    elif param2 == "U17":
        bus_info.objects.filter(plate_no=param1).update(U17=False)
    elif param2 == "U18":
        bus_info.objects.filter(plate_no=param1).update(U18=False)
    elif param2 == "L1":
        bus_info.objects.filter(plate_no=param1).update(L1=False)
    elif param2 == "L2":
        bus_info.objects.filter(plate_no=param1).update(L2=False)
    elif param2 == "L3":
        bus_info.objects.filter(plate_no=param1).update(L3=False)
    elif param2 == "L4":
        bus_info.objects.filter(plate_no=param1).update(L4=False)
    elif param2 == "L5":
        bus_info.objects.filter(plate_no=param1).update(U5=False)
    elif param2 == "L6":
        bus_info.objects.filter(plate_no=param1).update(L6=False)
    elif param2 == "L7":
        bus_info.objects.filter(plate_no=param1).update(L7=False)
    elif param2 == "L8":
        bus_info.objects.filter(plate_no=param1).update(L8=False)
    elif param2 == "L9":
        bus_info.objects.filter(plate_no=param1).update(L9=False)
    elif param2 == "L10":
        bus_info.objects.filter(plate_no=param1).update(L10=False)
    elif param2 == "L11":
        bus_info.objects.filter(plate_no=param1).update(L11=False)
    elif param2 == "L12":
        bus_info.objects.filter(plate_no=param1).update(L12=False)
    elif param2 == "L13":
        bus_info.objects.filter(plate_no=param1).update(L13=False)
    elif param2 == "L14":
        bus_info.objects.filter(plate_no=param1).update(L14=False)
    elif param2 == "L15":
        bus_info.objects.filter(plate_no=param1).update(L15=False)
    elif param2 == "L16":
        bus_info.objects.filter(plate_no=param1).update(L16=False)
    elif param2 == "L17":
        bus_info.objects.filter(plate_no=param1).update(L17=False)
    elif param2 == "L18":
        bus_info.objects.filter(plate_no=param1).update(L18=False)
    return HttpResponseRedirect('/booking/cancel_booking/')

