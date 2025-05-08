from django.urls import path 
from student.views import home_view, create_student_view



urlpatterns=[
   path("home/" ,home_view),
   # path("college/" ,college_view),


   path("create_student/" ,create_student_view),
#    path("update_student/<int:id>/" ,update_student_view),
#    path("student_list/" ,student_list_view),
#    path("student_delete/<int:id>/" ,student_delete_view),
#    path("student_detail/<int:id>/",student_detail_view),
]
 