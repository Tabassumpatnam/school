from django import forms
from student.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = "_all_"
        # exclude = ["name","roll_no"]
        # fields = ["name", "roll_no", "mobile", "extra_field"]
        fields =["name", "roll_no", "mobile"]

    def clean_mobile(self):
        print(self.cleaned_data)
        mobile = self.cleaned_data.get("mobile")
        if len(mobile)<10:
            raise forms.ValidationError("Mobile number should be exactly 10 digits")
        return mobile