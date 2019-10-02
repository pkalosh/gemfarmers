from django.shortcuts import render,get_object_or_404
from app.models import *
from app.forms import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
def index(request):
    sliders =Slider.objects.all()[:3]
    return render(request,'home.html',{'nbar': 'home','sliders':sliders})

def new_index(request):
    return render(request, 'new/index.html', {})

def new_about_us(request):
    return render(request, 'new/about_us.html', {})

def new_services(request):
    return render(request, 'new/new_services.html', {})

def new_blogs(request):
    items =Blog.objects.all()
    return render(request,'new/new_blog.html',{'items':items})
def new_hub(request):
    context_dict ={}
    if request.method == "POST":
        hub=request.POST['produce']
        county= request.POST['county']
        search_county=County.objects.get(id=county)
        hubs = Market.objects.filter(county=search_county, product__icontains=hub)
        agents = Agent.objects.filter(county=search_county, product__icontains=hub)
        counties =County.objects.all()
        context_dict['hubs']=hubs
        context_dict['hub']=hub
        context_dict['search_county']=search_county
        context_dict['agents']= agents
        context_dict['counties']=counties
        

    else:
        counties =County.objects.all()
        context_dict['counties']=counties
    return render(request, 'new/new_hub.html', context_dict)

def new_contacts(request):
    return render(request, 'new/new_contacts.html', {})

def new_documents(request):
    documents =Document.objects.all()
    return render(request,'new/new_documents.html',{'documents':documents})
   


def about_us(request):
	achievements =Achievement.objects.all()
	return render(request,'about.html',{'achievements':achievements})



def our_services(request):
	services =Service.objects.all()
	return render(request,'services.html',{'services':services})

def contacts(request):
	contacts =Contact.objects.all()
	return render(request,'contacts.html',{'contacts':contacts})


def business_hub(request):
    context_dict ={}
    if request.method == "POST":
        hub=request.POST['produce']
        county= request.POST['county']
        search_county=County.objects.get(id=county)
        hubs = Market.objects.filter(county=search_county, product__icontains=hub)
        agents = Agent.objects.filter(county=search_county, product__icontains=hub)
        counties =County.objects.all()
        context_dict['hubs']=hubs
        context_dict['hub']=hub
        context_dict['search_county']=search_county
        context_dict['agents']= agents
        context_dict['counties']=counties
        

    else:
        counties =County.objects.all()
        context_dict['counties']=counties
    return render(request,'hub.html',context_dict)


def our_blog(request):
	items =Blog.objects.all()
	return render(request,'blog.html',{'items':items})

def blog_item(request, id , slug):
    item=Blog.objects.filter(slug=slug).get(id=id)
    items = Blog.objects.all().order_by('-id')[:10]
    return render(request,'new/blog_detail.html',{'item': item,'items':items})

def signup(request):
	return render(request,'signup.html',{})




def farmer_signup(request):
    form=UserForm(request.POST)
    pform=FarmerForm(request.POST)
    if request.method == 'POST':
        form=UserForm(request.POST)
        farmerform=FarmerForm(request.POST)
        if form.is_valid() and farmerform.is_valid():
            u=form.save(commit=False)
            email=form.cleaned_data.get('email')
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            id_number=farmerform.cleaned_data.get('id_number')
            cell=farmerform.cleaned_data.get('cell')
            town=farmerform.cleaned_data.get('location')
            farm=farmerform.cleaned_data.get('farm')
            size=farmerform.cleaned_data.get('size')
            password=form.cleaned_data.get('password')
            password=make_password(password= password,              
                  salt=None,
                  hasher='default')
            try:
                user=User.objects.get(email=email)
                messages.add_message(request, messages.WARNING, 'User with that email already exists')
                return HttpResponseRedirect('.')
            except User.DoesNotExist:
                user=User.objects.create(email=email,first_name=first_name,last_name=last_name,
                	username=email,password=password)
                farmerprofile=Farmer.objects.create(user=user,id_number=id_number,cell=cell,location=town,
                	farm=farm,size=size)
                messages.add_message(request, messages.SUCCESS, 'Signup Success, you can Login Now')
                return HttpResponseRedirect('/accounts/login/')
    else:
        form=UserForm()
        farmerform=FarmerForm()
    context_dict={'form':form,'farmerform':farmerform
                  }
    return render(request,'farmersignup.html',context_dict)



def add_institution(request):
    form=UserForm(request.POST)
    studentform=InstitutionForm(request.POST)
    if request.method == 'POST':
        form=UserForm(request.POST)
        studentform=InstitutionForm(request.POST)
        if form.is_valid() and studentform.is_valid():
            u=form.save(commit=False)
            email=form.cleaned_data.get('email')
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            cell=studentform.cleaned_data.get('cell')
            county=studentform.cleaned_data.get('county')
            sub_county=studentform.cleaned_data.get('sub_county')
            town=studentform.cleaned_data.get('location')
            twitter_link=studentform.cleaned_data.get('twitter_link')
            name=studentform.cleaned_data.get('name')
            facebook_link=studentform.cleaned_data.get('facebook_link')
            institution=studentform.cleaned_data.get('institution')
            course=studentform.cleaned_data.get('course')
            password=form.cleaned_data.get('password')
            password=make_password(password= password,              
                  salt=None,
                  hasher='default')
            try:
                user=User.objects.get(email=email)
                messages.add_message(request, messages.WARNING, 'Institution with that email already exists')
                return HttpResponseRedirect('.')
            except User.DoesNotExist:
                user=User.objects.create(email=email,
                	username=email,password=password)
                studentprofile=Institution.objects.create(user=user,cell=cell,name=name,town=town,
                	county=county,sub_county=sub_county, twitter_link=twitter_link, facebook_link=facebook_link)
                messages.add_message(request, messages.SUCCESS, 'Signup Success, you can Login Now')
                return HttpResponseRedirect('/accounts/login/')
    else:
        form=UserForm()
        studentform=InstitutionForm()
    context_dict={'form':form,'studentform':studentform
                  }
    return render(request,'studentsignup.html',context_dict)


def resetpassword(request):
    context = {}
    form =PasswordResetRequestForm(request.POST)
    if request.method =="POST":
        email=request.POST['email']
        
        try:
            person = User.objects.get(email=email)
            request.session['email'] = email
            return HttpResponseRedirect('/new_password/')
        except User.DoesNotExist:
            messages.add_message(request, messages.WARNING, 'User with that email does not exist,Contact us if you are having a trouble loging in')
            return HttpResponseRedirect('.')
    else:
        form=PasswordResetRequestForm()
        context['form'] =form
    return render(request,'reset.html', context)


def new_password(request):
    context = {}
    form =PassForm(request.POST)
    email = request.session.get('email')
    person = User.objects.get(email=email)
    context['person'] =person
    context['form'] = form
    if request.method == 'POST':
            password=request.POST['password']
            #password2=request.POST['password2']
            #if password != password2:
                #messages.add_message(request, messages.SUCCESS, 'password mismatch!!')
                #return HttpResponseRedirect('.')
            #else:
            uform =PassForm(request.POST, None ,instance=person)
            if uform.is_valid():
                check=uform.save(commit=False)
                #sign_up.password = make_password(form.cleaned_data['password'])
                #sign_up.status = 1
                check.password=make_password(password)
                #check.set_password(self.cleaned_data["password"])
                check.save()
                
                return HttpResponseRedirect('/accounts/login/')
    return render(request, 'resetpassword.html', context)

@login_required
def dashboard(request):
	return render(request,'dashbaord.html',{})





@login_required
def update_profile(request):
    person = request.user
    p=person.id
    prof = get_object_or_404(Profile, user=p)
    if request.method == 'POST':
        uform=UForm(request.POST or None, instance=person)
        pform=ProfileForm(request.POST or None, instance=prof)
        if uform.is_valid() and pform.is_valid() :
           
            uform.save()
            pform.save()
            messages.add_message(request, messages.SUCCESS, 'Profile Updated Successfully')
            #next = request.GET.get('from')
            #if next:
            return HttpResponseRedirect('/dashboard/')
            #return HttpResponseRedirect('/app/mentors')
    else:
        uform = UForm(instance=person)
        pform=ProfileForm( instance=prof)
    return render(request,'farmerupdate.html',{'pform':pform,'uform':uform})




@login_required
def update_student(request):
    person = request.user
    p=person.id
    prof = get_object_or_404(Student, user=p)
    if request.method == 'POST':
        uform=UForm(request.POST or None, instance=person)
        cform=StudentForm(request.POST or None, instance=prof)
        if uform.is_valid() and cform.is_valid() :
           
            uform.save()
            cform.save()
            messages.add_message(request, messages.SUCCESS, 'Profile Updated Successfully')
            #next = request.GET.get('from')
            #if next:
            return HttpResponseRedirect('/dashboard/')
            #return HttpResponseRedirect('/app/mentors')
    else:
        uform = UForm(instance=person)
        cform=StudentForm( instance=prof)
    return render(request,'farmerupdate.html',{'cform':cform,'uform':uform})


@login_required
def farmers_details(request, id):
    person = request.user
    p=person.id
    prof = get_object_or_404(Profile, user=p)
    if request.method == 'POST':
        form=BioForm(request.POST or None, instance=prof)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile Updated Successfully')
            #next = request.GET.get('from')
            #if next:
            return HttpResponseRedirect('/dashboard/')
    else:
        form=BioForm(instance=prof)
    return render(request,'dashboard/bio.html',{'form':form})


@login_required
def farmer_details(request):
    m=request.user
    p=m.id
    try:
        ac = get_object_or_404(Farmer, user=p)
        form=FarmerForm(request.POST or None, instance=ac)
        if request.method == 'POST':
            if form.is_valid():
                u=form.save(commit=False)
                u.user=m
                u.save()
                messages.add_message(request, messages.SUCCESS, 'You have Succesfully Updated your details')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = FarmerForm(instance=ac)
    except:
        form=FarmerForm(request.POST)
        if request.method == 'POST':
            form=FarmerForm(request.POST)
            if form.is_valid():
                u=form.save(commit=False)
                u.user=m
                u.save()
                messages.add_message(request, messages.SUCCESS, 'You have succefully joined Farmers Group')
                return HttpResponseRedirect('/dashboard')
        else:
            form=FarmerForm()

    
        #pform=UserProfileForm(instance=prof)
    
    return render(request,'farmjoin.html',{'form':form})


@login_required
def student_details(request):
    m=request.user
    p=m.id
    try:
        ac = get_object_or_404(Student, user=p)
        form=StudentForm(request.POST or None, instance=ac)
        if request.method == 'POST':
            if form.is_valid():
                u=form.save(commit=False)
                u.user=m
                u.save()
                messages.add_message(request, messages.SUCCESS, 'You have Succesfully Updated your details')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = StudentForm(instance=ac)
    except:
        form=StudentForm(request.POST)
        if request.method == 'POST':
            form=StudentForm(request.POST)
            if form.is_valid():
                u=form.save(commit=False)
                u.user=m
                u.save()
                messages.add_message(request, messages.SUCCESS, 'You have succefully joined Farmers Group')
                return HttpResponseRedirect('/dashboard')
        else:
            form=StudentForm()

    
        #pform=UserProfileForm(instance=prof)
    
    return render(request,'farmjoin.html',{'form':form})


@login_required
def expert_details(request):
    m=request.user
    p=m.id
    expert = Expert.objects.create(user=m)
    messages.add_message(request, messages.SUCCESS, 'You have succefully joined Farmers Group')
    return HttpResponseRedirect('/dashboard')
  

def documents(request):
    documents =Document.objects.all()
    return render(request,'documents.html',{'documents':documents})
   


@login_required
def update_institution(request):
    person = request.user
    p=person.id
    prof = get_object_or_404(Institution, user=p)
    if request.method == 'POST':
        cform=InstitutionForm(request.POST or None, instance=prof)
        if cform.is_valid() :
           
        
            cform.save()
            messages.add_message(request, messages.SUCCESS, 'Details Updated Successfully')
            #next = request.GET.get('from')
            #if next:
            return HttpResponseRedirect('/dashboard/')
            #return HttpResponseRedirect('/app/mentors')
    else:
        cform=InstitutionForm( instance=prof)
    return render(request,'inst.html',{'cform':cform})


@login_required
def entreprenuer_details(request):
    m=request.user
    p=m.id
    try:
        ac = get_object_or_404(Entrepreneur, user=p)
        form=EntrepreneurForm(request.POST or None, instance=ac)
        if request.method == 'POST':
            if form.is_valid():
                u=form.save(commit=False)
                u.user=m
                u.save()
                messages.add_message(request, messages.SUCCESS, 'You have Succesfully Updated your details')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = EntrepreneurForm(instance=ac)
    except:
        form=EntrepreneurForm(request.POST)
        if request.method == 'POST':
            form=EntrepreneurForm(request.POST)
            if form.is_valid():
                u=form.save(commit=False)
                u.user=m
                u.save()
                messages.add_message(request, messages.SUCCESS, 'You have succefully joined Farmers Group')
                return HttpResponseRedirect('/dashboard')
        else:
            form=EntrepreneurForm()

    
        #pform=UserProfileForm(instance=prof)
    
    return render(request,'farmjoin.html',{'form':form})


@login_required
def customer_details(request):
    m=request.user
    p=m.id
    try:
        ac = get_object_or_404(Customer, user=p)
        form=CustomerForm(request.POST or None, instance=ac)
        if request.method == 'POST':
            if form.is_valid():
                u=form.save(commit=False)
                u.user=m
                u.save()
                messages.add_message(request, messages.SUCCESS, 'You have Succesfully Updated your details')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = CustomerForm(instance=ac)
    except:
        form=CustomerForm(request.POST)
        if request.method == 'POST':
            form=CustomerForm(request.POST)
            if form.is_valid():
                u=form.save(commit=False)
                u.user=m
                u.save()
                messages.add_message(request, messages.SUCCESS, 'You have succefully joined Farmers Group')
                return HttpResponseRedirect('/dashboard')
        else:
            form=CustomerForm()

    
        #pform=UserProfileForm(instance=prof)
    
    return render(request,'farmjoin.html',{'form':form})