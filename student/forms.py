from django import forms
from student.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = __"all__"
        fields = ["name", "roll_no"]