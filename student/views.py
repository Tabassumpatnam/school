from django.shortcuts import render
from student.models import Student
from django.shortcuts import render,redirect
from student.forms import StudentForm

def home_view(request):
   return render(request,"index.html")

def college_view(request):
    return render(request,"college.html")

def create_student_view(request):
    if request.method=="POST":
        
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
        else:
            return render(request, "student/create_student.html", {"form": student_form})
    student_form = StudentForm()
    return render(request, "student/create_student.html", {"form": student_form })

def update_student_view(request,id):
    st=Student.objects.get(pk=id)
    if request.method=="POST":
        nm=request.POST.get("st_name")
        roll=request.POST.get("st_roll_no")
        st.name=nm
        st.roll_no=roll
        st.save()
    return render(request,"student/update_student.html",{'student:student_form'})

# def student_list_view(request):
#     student_list=Student.objects.all()
#     return render(request,"student/student_list.html",{'student':student_list})

# def student_delete_view(request,id):
#     student = Student.objects.get(pk=id)
#     Student.delete()
#     return redirect("/student/student_list/")


def category_view(request,):
  
    return render(request,'blog/category.html')
 

# Create your views here.
