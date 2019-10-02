from django.db import models
from djrichtextfield.models import RichTextField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from smart_selects.db_fields import ChainedForeignKey




class Achievement(models.Model):
	achievement =models.CharField(max_length = 500)
	def __str__(self):
		return self.achievement
	class Meta:
		verbose_name_plural = 'Our Achievements'


class Service(models.Model):

	service =models.CharField(max_length = 500)
	def __str__(self):
		return self.service
	class Meta:
		verbose_name_plural = 'Our Services'


class Slider(models.Model):
	image_title =models.CharField(max_length=200, help_text="max. 20 char")
	image_description =models.CharField(max_length=800, help_text='Short Description(Max 80 Char)')
	image =models.ImageField(upload_to="sliders")
	def save(self):
		#Opening the uploaded image
		im = Image.open(self.image)

		output = BytesIO()

		#Resize/modify the image
		im = im.resize( (1920,700) )

		#after modifications, save it to the output
		im.save(output, format='JPEG', quality=100)
		output.seek(0)

		#change the imagefield value to be the newley modifed image value
		self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

		super(Slider,self).save()

	def __str__(self):
		return self.image_title



class Contact(models.Model):
	region=models.CharField(max_length=500)

	contact_person =models.CharField(max_length = 500)
	contact =models.CharField(max_length=500)
	def __str__(self):
		return self.region
	class Meta:
		verbose_name_plural = 'Regional Contact Persons'

class County(models.Model):
	county=models.CharField(max_length=500)
	def __str__(self):
		return self.county
	class Meta:
		verbose_name_plural = 'Counties'

class SubCounty(models.Model):
	county =models.ForeignKey(County, on_delete=models.CASCADE)
	sub_county=models.CharField(max_length=500)
	def __str__(self):
		return self.sub_county
	class Meta:
		verbose_name_plural = 'Sub Counties'

class Market(models.Model):
	market_name=models.CharField(max_length=500, verbose_name ="Market Center Name")

	product =models.CharField(max_length = 500, verbose_name ="Products/Services")
	contact_person =models.CharField(max_length=500, verbose_name ="Contact Person")
	county =models.ForeignKey(County, on_delete=models.CASCADE, verbose_name ="County")
	sub_county =models.ForeignKey(SubCounty, on_delete=models.CASCADE, verbose_name ="Sub County")
	division =models.CharField(max_length=500, verbose_name ="Division")
	town =models.CharField(max_length=500, verbose_name ="Town")
	contact_person_email=models.EmailField(null=True,blank=True, verbose_name ="Contact Person's Email")
	contact_person_phone=models.CharField(max_length=100, null=True,blank=True,verbose_name ="Contact Person's Phone Number")
	contact_facebook_account=models.CharField(max_length=200, null=True,blank=True, verbose_name ="Contact Person's Facebook Account")
	contact_telegram_account=models.CharField(max_length=200, null=True,blank=True, verbose_name ="Contact Person's Telegram Account")

	def __str__(self):
		return self.market_name
	class Meta:
		verbose_name_plural = 'Business Market Centers'

class Agent(models.Model):
	market_name=models.CharField(max_length=500, verbose_name ="Market Center Name")

	product =models.CharField(max_length = 500, verbose_name ="Products/Services")
	contact_person =models.CharField(max_length=500, verbose_name ="Contact Person")
	county =models.ForeignKey(County, on_delete=models.CASCADE, verbose_name ="County")
	sub_county =models.ForeignKey(SubCounty, on_delete=models.CASCADE, verbose_name ="Sub County")
	division =models.CharField(max_length=500, verbose_name ="Division")
	town =models.CharField(max_length=500, verbose_name ="Town")
	contact_person_email=models.EmailField(null=True,blank=True, verbose_name ="Contact Person's Email")
	contact_person_phone=models.CharField(max_length=100, null=True,blank=True,verbose_name ="Contact Person's Phone Number")
	contact_facebook_account=models.CharField(max_length=200, null=True,blank=True, verbose_name ="Contact Person's Facebook Account")
	contact_telegram_account=models.CharField(max_length=200, null=True,blank=True, verbose_name ="Contact Person's Telegram Account")

	def __str__(self):
		return self.market_name
	class Meta:
		verbose_name_plural = 'Business Agents'


class Blog(models.Model):
    title=models.CharField(max_length=200)
    body=RichTextField(verbose_name="Content")
    date_posted=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="blog_photos",null=True,blank=True)
    slug=models.SlugField(unique=False, max_length=600)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Blog, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title

class Farmer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	id_number =models.CharField(max_length=200,verbose_name="ID Number")
	cell =models.CharField(max_length=100,verbose_name="Phone Number")
	#county =models.ForeignKey(County, verbose_name="County", on_delete=models.CASCADE)
	location =models.CharField(max_length=200,verbose_name="Location")
	farm =models.CharField(max_length=200, verbose_name="Type of Farming")
	size =models.CharField(max_length=200, verbose_name="Farm Size")

	def __str__(self):
		return self.user.username


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	id_number =models.CharField(max_length=200,verbose_name="ID Number")
	cell =models.CharField(max_length=100,verbose_name="Phone Number")
	institution =models.CharField(max_length=200, verbose_name="Institution of Learning")
	location =models.CharField(max_length=200,verbose_name="Location")
	course =models.CharField(max_length=200,verbose_name="Course")
	def __str__(self):
		return self.user.username

class Expert(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class Profile(models.Model): #Jobseekers and Volunteers details
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    id_number =models.CharField(max_length=200,verbose_name="ID Number")
    cell =models.CharField(max_length=100,verbose_name="Phone Number")

    twitter_link =models.CharField(max_length=500, null=True, blank=True, verbose_name="Twitter Account Link")
    facebook_link = models.CharField(max_length=500, null=True, blank=True, verbose_name="Twitter Account Link")
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True, blank=True)
    sub_county = ChainedForeignKey(
        SubCounty,
        chained_field="county",
        chained_model_field="county",
        show_all=False,
        auto_choose=True,
        sort=True, null=True,blank=True)
    town = models.CharField(max_length=200, null=True, blank=True)
    market_center =models.CharField(max_length =300, null=True, blank=True)
    #linkedin_link =models.CharField(max_length=500, null=True, blank=True, verbose_name="Twitter Account Link")
    
    def __str__(self):
    	return self.user.username


class Document(models.Model):
    doc_name =models.CharField(max_length=500, verbose_name="Document Name")
    document = models.FileField(upload_to="Documents")
    def __str__(self):
        return self.doc_name

class Institution(models.Model):
	user =models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length = 500)
	cell =models.CharField(max_length=100,verbose_name="Phone Number")
	twitter_link =models.CharField(max_length=500, null=True, blank=True, verbose_name="Twitter Account Link")
	facebook_link = models.CharField(max_length=500, null=True, blank=True, verbose_name="Twitter Account Link")
	county = models.ForeignKey(County, on_delete=models.CASCADE, null=True, blank=True)
	sub_county = ChainedForeignKey(
        SubCounty,
        chained_field="county",
        chained_model_field="county",
        show_all=False,
        auto_choose=True,
        sort=True, null=True,blank=True)
	town = models.CharField(max_length=200, null=True, blank=True)
	def __str__(self):
		return self.user.username




class Entrepreneur(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	business =models.CharField(max_length=200,verbose_name="Business Name")
	registration =models.CharField(max_length=100,verbose_name="Registration Name")
	#county =models.ForeignKey(County, verbose_name="County", on_delete=models.CASCADE)
	business_type =models.CharField(max_length=200,verbose_name="Business Name")
	

	def __str__(self):
		return self.user.username

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	good =models.CharField(max_length=200,verbose_name="Good/Service")
	

	def __str__(self):
		return self.user.username