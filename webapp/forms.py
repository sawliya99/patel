from  django import forms

class StudentForm(forms.Form):
    firstname =forms.CharField()
    lastname=forms.CharField()
    email =forms.CharField()
    file =forms.FileField()