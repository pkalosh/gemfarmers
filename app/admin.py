from django.contrib import admin
from app.models import *
admin.site.register(Achievement)
admin.site.register(Service)

admin.site.register(Contact)
admin.site.register(Market)
admin.site.register(Agent)
admin.site.register(County)
admin.site.register(SubCounty)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','id_number','cell','county','sub_county','town','twitter_link', 'facebook_link',)
    search_fields=['user__email','user__first_name','user__last_name']
    list_filter = ('user__profile__county',) 


    def first_name(self, instance):
        return instance.user.first_name
    def last_name(self, instance):
        return instance.user.last_name
    def email(self, instance):
        return instance.user.email
    def id_number(self, instance):
        return instance.user.profile.id_number
    def cell(self, instance):
        return instance.user.profile.cell
    def twitter_link(self, instance):
        return instance.user.profile.twitter_link
    def facebook_link(self, instance):
        return instance.user.profile.facebook_link
    def county(self, instance):
        return instance.user.profile.county
    def sub_county(self,instance):
        return instance.user.profile.sub_county
    def town(self,instance):
        return instance.user.profile.town









class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('title',)}

admin.site.register(Blog, BlogAdmin)

class FarmerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','id_number','cell','county','sub_county','town','farm','farmsize','twitter_link', 'facebook_link',)
    search_fields=['user__email','user__first_name','user__last_name']
    list_filter = ('user__profile__county',) 


    def first_name(self, instance):
        return instance.user.first_name
    def last_name(self, instance):
        return instance.user.last_name
    def email(self, instance):
        return instance.user.email
    def id_number(self, instance):
        return instance.user.profile.id_number
    def cell(self, instance):
        return instance.user.profile.cell
    def twitter_link(self, instance):
        return instance.user.profile.twitter_link
    def facebook_link(self, instance):
        return instance.user.profile.facebook_link
    def county(self, instance):
        return instance.user.profile.county
    def sub_county(self,instance):
        return instance.user.profile.sub_county
    def town(self,instance):
        return instance.user.profile.town
    def farm(self,instance):
        return instance.user.farmer.farm
    def farmsize(self,instance):
        return instance.user.farmer.size



   
  
   
admin.site.register(Farmer, FarmerAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','id_number','cell','county','sub_county','town','institution','course','twitter_link', 'facebook_link',)
    search_fields=['user__email','user__first_name','user__last_name']
    list_filter = ('user__profile__county', 'user__student__institution') 


    def first_name(self, instance):
        return instance.user.first_name
    def last_name(self, instance):
        return instance.user.last_name
    def email(self, instance):
        return instance.user.email
    def id_number(self, instance):
        return instance.user.profile.id_number
    def cell(self, instance):
        return instance.user.profile.cell
    def twitter_link(self, instance):
        return instance.user.profile.twitter_link
    def facebook_link(self, instance):
        return instance.user.profile.facebook_link
    def county(self, instance):
        return instance.user.profile.county
    def sub_county(self,instance):
        return instance.user.profile.sub_county
    def town(self,instance):
        return instance.user.profile.town
    def institution(self,instance):
        return instance.user.farmer.farm
    def course(self,instance):
        return instance.user.farmer.size
admin.site.register(Student, StudentAdmin)
admin.site.register(Slider)
admin.site.register(Profile)



admin.site.register(Expert, ProfileAdmin)
admin.site.register(Document)

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','cell','county','sub_county','town','twitter_link', 'facebook_link',)
    search_fields=['user__email','user__first_name','user__last_name']
    list_filter = ('county', 'sub_county') 

    def email(self, instance):
        return instance.user.email
    def id_number(self, instance):
        return instance.user.profile.id_number
admin.site.register(Institution, InstitutionAdmin)


class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','id_number','cell','county','sub_county','town','business','registration','biz_type','twitter_link', 'facebook_link',)
    search_fields=['user__email','user__first_name','user__last_name']
    list_filter = ('user__profile__county',) 


    def first_name(self, instance):
        return instance.user.first_name
    def last_name(self, instance):
        return instance.user.last_name
    def email(self, instance):
        return instance.user.email
    def id_number(self, instance):
        return instance.user.profile.id_number
    def cell(self, instance):
        return instance.user.profile.cell
    def twitter_link(self, instance):
        return instance.user.profile.twitter_link
    def facebook_link(self, instance):
        return instance.user.profile.facebook_link
    def county(self, instance):
        return instance.user.profile.county
    def sub_county(self,instance):
        return instance.user.profile.sub_county
    def town(self,instance):
        return instance.user.profile.town
    def business(self,instance):
        return instance.user.entrepreneur.business
    def resgistration(self,instance):
        return instance.user.entrepreneur.resgistration
    def biz_type(self,instance):
        return instance.user.entrepreneur.business_type
admin.site.register(Entrepreneur, EntrepreneurAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','id_number','cell','county','sub_county','town','good','twitter_link', 'facebook_link',)
    search_fields=['user__email','user__first_name','user__last_name']
    list_filter = ('user__profile__county',) 


    def first_name(self, instance):
        return instance.user.first_name
    def last_name(self, instance):
        return instance.user.last_name
    def email(self, instance):
        return instance.user.email
    def id_number(self, instance):
        return instance.user.profile.id_number
    def cell(self, instance):
        return instance.user.profile.cell
    def twitter_link(self, instance):
        return instance.user.profile.twitter_link
    def facebook_link(self, instance):
        return instance.user.profile.facebook_link
    def county(self, instance):
        return instance.user.profile.county
    def sub_county(self,instance):
        return instance.user.profile.sub_county
    def town(self,instance):
        return instance.user.profile.town
    def good(self,instance):
        return instance.user.customer.good

admin.site.register(Customer, CustomerAdmin)
