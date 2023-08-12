from django.shortcuts import render, redirect
from django.contrib import messages
from Portfolio.models import Contact, Blogs, Internship

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("num")
        desc=request.POST.get("desc")
        quary=Contact(name=name,email=email,phonenumber=contact,description=desc)
        quary.save() 
        messages.info(request, " Your prablam is recived and i will contact you")
        return redirect("/contact")
    
    return render(request,"contact.html")

def blog(request):
    
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,"blog.html", context)


def internshipdetails(request):
    
    
    if not request.user.is_authenticated:
        messages.warning(request,"Please login to the page")
        return redirect("/application/login/")
    
    if request.method=="POST":
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        fnumber=request.POST.get("num")
        fcname=request.POST.get("cname")
        fcregno=request.POST.get("reg")
        fofferl=request.POST.get("OFL")
        fstdate=request.POST.get("SD")
        fenddate=request.POST.get("ED")
        fpreport=request.POST.get("PR")
        
        # upper case
        fname=fname.upper()
        fcname=fcname.upper()
        fcregno=fcregno.upper()
        fpreport=fpreport.upper()
        fofferl=fofferl.upper()
        
        # data present ar not
        a=Internship.objects.filter(collage_REG_NO= fcregno)
        b=Internship.objects.filter(email=femail)
        
        if a or b:
            messages.warning(request,"Data already present")
            return redirect("/internshipdetails")
        
        
        
        
        query=Internship(fullname=fname,email=femail,number=fnumber,collage_name=fcname, collage_REG_NO=fcregno, offerstatus=fofferl,startdate=fstdate,enddate=fenddate,proj_report=fpreport)
        query.save()
        messages.info(request, " Form submited successful")
        return redirect("/internshipdetails")
        
    return render(request,"internship.html")