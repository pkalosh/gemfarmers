from django.urls import  path
from app.views import *

urlpatterns = [
    path('index/',index, name='index'),
    path('', new_index, name='new_index'),
    path('new_about_us/', new_about_us, name='new_about_us'),
    path('new_services/', new_services, name='new_services'),
    path('new_hub/', new_hub, name='new_hub'),
    path('new_contacts/', new_contacts, name='new_contacts'),
    path('new_documents/', new_documents, name='new_documents'),
    path('new_blog/', new_blogs, name='new_blog'),
    path('about_us/',about_us, name='about_us'),

    path('our_services/',our_services, name='our_services'),
    path('contacts/',contacts, name='contacts'),
    path('business_hub/',business_hub, name='business_hub'),
    path('our_blog/',our_blog, name='our_blog'),
    path('blog_item/<int:id>/<slug:slug>/',blog_item, name='blog_item'),
    path('signup/',signup, name='signup'),

    path('farmer_signup/',farmer_signup, name='farmer_signup'),
    path('add_institution/',add_institution, name='add_institution'),
    path('resetpassword/',resetpassword, name='resetpassword'),
    
    path('new_password/',new_password, name='new_password'),
    path('dashboard/',dashboard, name='dashboard'),

    path('update_student/',update_student, name='update_student'),
    path('update_profile/',update_profile, name='update_profile'),
    path('farmer_details/',farmer_details, name='farmer_details'),
    path('student_details/',student_details, name='student_details'),
    path('expert_details/',expert_details, name='expert_details'),
    path('documents/',documents, name='documents'),
    path('update_institution/', update_institution, name='update_institution'),

    path('entreprenuer_details/',entreprenuer_details, name='entreprenuer_details'),
    path('customer_details/', customer_details, name='customer_details'),

      ]