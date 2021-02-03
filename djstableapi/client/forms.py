from django import forms
from .models import Student
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):

    # def clean_date(self):
    #     date = self.cleaned_data['date']
    #     print(date)
    #     if date == "" or date is None:
    #         print("Error")
    #         raise ValidationError("Invalid date")
    #     else:
    #         return date
    class Meta:
        model = Student
        fields = ('roll','name', 'college','date')