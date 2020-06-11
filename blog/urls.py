
from django.urls import path
from django.urls import include
from blog import views

app_name = 'blog'

urlpatterns = [

    path('',views.bloghome, name = 'bloghome'),
    path('<int:blog_id/>', views.detail , name = 'detail')

]
