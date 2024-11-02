from django.shortcuts import render
from django.contrib.auth import logout
from home.models import sign_up_table
from django.contrib.auth.models import User

# Create your views here.
def index1(request):
    return render(request,"teacher/teacher_dashboard.html")

def assignment(request):
    return render(request,"teacher/teacher_assignment.html")
 

def chat(request):
    return render(request,"teacher/teacher_chat.html")


def profile(request):
    context ={}
    data = sign_up_table.objects.get(main__id=request.user.id)
    # print(data)
    context["data"]=data
    if request.method == "POST":
        print(request.POST)
        # print(request.file)
        profile_pic = request.POST.get('profile-photo')
        email= request.POST.get('Email')
        frist_name= request.POST.get('Frist_Name')
        last_name = request.POST.get('Last_Name')
        add = request.POST.get('Address')
        city = request.POST.get('City')
        state = request.POST.get('State')
        pincode = request.POST.get('Pincode')
        about_me = request.POST.get('aboutme')
        mo=request.POST.get('no')
        parent_no = request.POST.get('p_no')
        qualification = request.POST.get('Qualification')
        college = request.POST.get('College')

        urs = User.objects.get(id=request.user.id)
        urs.first_name=frist_name
        urs.last_name=last_name
        urs.email=email
        urs.save()

        data.mobile=mo
        data.add = add
        data.city_name =city
        data.state = state
        data.pincode =pincode
        data.about_me=about_me
        data.p_mobile =parent_no
        data.qualification =qualification
        data.collge_name =college
        data.save()

        if "profile-photo" in request.FILES :
            img = request.FILES["profile-photo"]
            data.profile_pic =img
            data.save()

        context["status"]= "Changes save Successfully "
    return render(request,"teacher/teacher_profile.html",context)



def student_logout(request):
    logout(request)
    return render(request,"login.html")
    # return HttpResponse("back to home")
