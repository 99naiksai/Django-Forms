from django.shortcuts import render
from . forms import StudentRegistration
from django.http import HttpResponseRedirect

def thank_you(request):
   return render(request , 'enroll/success.html')
def showformdata(request):
   if request.method=='POST':
      fm = StudentRegistration(request.POST)
      if fm.is_valid():
         print('Form Validated') 
         print('Name',fm.cleaned_data['name'])
         print('Email',fm.cleaned_data['email'])
         print('Password',fm.cleaned_data['password'])
         print('Roll No',fm.cleaned_data['roll'])
         print('Agree',fm.cleaned_data['agree'])
         print('Price',fm.cleaned_data['price'])
         print('Rate',fm.cleaned_data['rate'])
         print('Comment',fm.cleaned_data['comment'])
         print('Website',fm.cleaned_data['website'])
         print('Description',fm.cleaned_data['description'])
         print('Notes',fm.cleaned_data['notes'])
         return HttpResponseRedirect('/regi/success/') #for going to next page
         #return render(request , 'enroll/success.html' , {'nm':name}) #key nm will become variable in success.html

   else:
      fm = StudentRegistration()
      print('Yeh get request se aaya he')
   return render(request , 'enroll/userregistration.html' , {'form':fm}) #form will become variable in template file.

