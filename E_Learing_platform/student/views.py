from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from home.models import sign_up_table ,course,notification,QuesModel,completeCourse
from student.models import usercourse,helpquary

# Create your views here.

def index1(request):
    new = notification.objects.all()
    context ={
        "new":new
    }
    return render(request,"studentdashboard.html",context)


def student_logout(request):
    logout(request)
    return render(request,"login.html")
    # return HttpResponse("back to home")



def feedback_info(request):
    return render(request, "feedbackform.html")


def student_cour(request):
    all = course.objects.all()
    context ={
        'all':all
}
    return render(request,"student_course.html",context)

def temp(request,slug):
    new_course = course.objects.filter(new_slug=slug)
    course_id = course.objects.get(new_slug = slug)
    try:
        enroll_course = usercourse.objects.get(user = request.user,sub =course_id)
    except usercourse.DoesNotExist:
        enroll_course = None
    data ={
        "new" :new_course,
        "enroll_course":enroll_course,
    }
    
    return render(request,"course_info.html",data)

def course_model(request,slug):
    new = course.objects.filter(new_slug=slug)
    data={
        "new":new
    }
    return render(request,"course_model.html",data)


def chapter_video1(request,slug):
    main= course.objects.filter(new_slug=slug)
    data={
        "main":main
    }
    return render(request,"chapers/chapter1.html",data)
def chapter_video2(request,slug):
    main= course.objects.filter(new_slug=slug)
    data={
        "main":main
    }
    return render(request,"chapers/chapter2.html",data)
def chapter_video5(request,slug):
    main= course.objects.filter(new_slug=slug)
    data={
        "main":main
    }
    return render(request,"chapers/chapter5.html",data)
def chapter_video3(request,slug):
    main= course.objects.filter(new_slug=slug)
    data={
        "main":main
    }
    return render(request,"chapers/chapter3.html",data)
def chapter_video4(request,slug):
    main= course.objects.filter(new_slug=slug)
    data={
        "main":main
    }
    return render(request,"chapers/chapter4.html",data)


def quizpage(request,slug):
    if request.method == 'POST':
        print(request.POST)
        sub = course.objects.get(new_slug=slug)
        course_user = User.objects.get(id=request.user.id)
        # main_core.is_complete= True if request.POST.get('is_true') == 'true' else False
        
        questions=QuesModel.objects.filter(sub__new_slug=slug)
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
        # percent = score/(total*10) *100

        if score>=1:
            flag=1
            status = "You sccussfully complate exam!"
        else:
            flag=0
            status ="You was failed.."

        print(flag)
        if flag == 1:
            temp =completeCourse(use=course_user,sub=sub,is_complete=True)
            temp.save()
        
        
    
        cname = course.objects.get(new_slug=slug)

        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            # 'percent':percent,
            'total':total,
            'status':status,
            'flag':flag,
            'cname':cname
        }
        return render(request,'new_quiz.html',context)
    else:
        questions=QuesModel.objects.filter(sub__new_slug=slug)
        new = course.objects.filter(new_slug=slug)
        context = {
            'questions':questions,
            'new':new
        }
        return render(request,'new_quiz.html',context)




def checkout(request,slug):
    sub = course.objects.get(new_slug=slug)
    course_user = User.objects.get(id=request.user.id)
    print(sub)
    print(course_user)
    context ={}
    context["sub"]=sub
    context["course_user"]=course_user
    temp = usercourse(user=course_user,sub=sub)
    temp.save()
    return redirect('mycourse')
    # return render(request,"checkout.html",context)

def assignment(request):
    data = sign_up_table.objects.get(main__id =request.user.id)
    print(data)
    if data.ispaid == True:
        return render(request,"assignment.html")
    else:
        return render(request,"assignment_false.html")


def chat(request):
    data = sign_up_table.objects.get(main__id =request.user.id)
    print(data)
    if data.ispaid == True:
        return render(request,"chat_with_teacher.html")
    else:
        return render(request,"chat_false.html")

def help(request):
    if request.method == "POST":
        student_name = request.POST.get('name')
        student_email = request.POST.get('email')
        student_message = request.POST.get('message')
        print(student_name,student_email,student_message)
        myque= helpquary(student_name=student_name,student_email=student_email,student_message=student_message)
        myque.save()
    return render(request,"support.html")
    
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
    return render(request,"profile.html",context)


def mycourse(request):
    new = course.objects.all()
    data = usercourse.objects.filter(user=request.user)
    main = completeCourse.objects.filter(use=request.user)
    print(main)
    print(new)
    print(data)
    context ={
        "data":data,
        "main":main
    }
    return render(request,"mycourse.html",context)

def upgrade(request):
    return render(request,"upgradepro.html")