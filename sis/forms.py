from django import forms

from sis.models import Student



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name','studentID','email','phone','dob','department','year')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'studentID':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'17000000'}),
            'dob':forms.TextInput(attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}),
            'department':forms.Select(attrs={'class':'form-control'}),
            'year':forms.Select(attrs={'class':'form-control'})
        }
