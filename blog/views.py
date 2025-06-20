from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,AboutUs
from .forms import ContactForm
from django.core.paginator import Paginator
# Create your views here.

# posts=[
#         {'id':1,'title':'Post 1','content':'content for post 1'},
#         {'id':2,'title':'Post 2','content':'content for post 2'},
#         {'id':3,'title':'Post 3','content':'content for post 3'},
#         {'id':4,'title':'Post 4','content':'content for post 4'}
#     ]
def index(request):
    blog_title='Posts'
    all_posts=Post.objects.all()
    paginator=Paginator(all_posts,5)
    page_no=request.GET.get('page')
    page_obj=paginator.get_page(page_no)
    return render(request,'index.html',{"blog_title":blog_title,'posts':page_obj})

def detail(request,slug):
    # Getting static data
    # post=next((item for item in posts if item['id']==int(post_id)),None)
    post=Post.objects.get(slug=slug)
    rel_post=Post.objects.filter(category=post.category).exclude(pk=post.id)
     #the filter gives us only the posts with same category
    return render(request,'detail.html',{'postss':post,'category':rel_post})

def old_url_red(request):
    return redirect("new_url")

def new_url_red(request):
    return HttpResponse("This is new the url mate!!")


def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        mess=request.POST.get('message')
        if form.is_valid():
            success_mess='Form has been submitted'
            return render(request,'contact.html',{'form':form,'suc_mes':success_mess})
        return render(request,'contact.html',{'form':form,'name':name,'email':email,'mess':mess})
    return render(request,'contact.html')#,{'postss':post,'category':rel_post})


def about_view(request):
    about_us=AboutUs.objects.first()
    return render(request,'about.html',{'about_us':about_us})
