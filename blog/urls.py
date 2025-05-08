from django.urls import path 
from blog.views import category_view, about_view, contact_view, index_view, single_post_view


urlpatterns=[
   path("category/" ,category_view),
   path("about/" ,about_view),
   path("contact/" ,contact_view),
   path("index/" ,index_view),
   path("single-post/" ,single_post_view)
   
  


  
]
 