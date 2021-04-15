from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=5 , max_length=50,strip=False,empty_value='Sai',error_messages={'required':'Enter your Name'})
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    file = forms.CharField(widget=forms.FileInput)
    roll = forms.IntegerField(min_value=5 , max_value=40)
    price = forms.DecimalField(min_value=5 , max_value=40 , max_digits=4 , decimal_places=1)
    agree = forms.BooleanField(label_suffix = ' ' , label='I Agree')
    rate = forms.FloatField(min_value=5 , max_value=40)
    comment = forms.SlugField()
    website = forms.URLField(min_length=5 , max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    notes=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))

    #def clean(self):
     #   cleaned_data = super().clean()
      #  valname = self.cleaned_data['name']
       # valemail = self.cleaned_data['email']
        #if len(valname) < 4:
         #   raise  forms.ValidationError('please enter value greater than or equal to 4')
        #if len(valemail) < 10:
         #   raise  forms.ValidationError('please enter value greater than or equal to 10')
        