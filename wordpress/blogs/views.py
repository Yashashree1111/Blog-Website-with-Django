from django.shortcuts import render
from django.http import Http404
from datetime import date
from .models import Post,Tag,Comment,Author
from .forms import commentForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.




def starting_page(request):
    posts = Post.objects.all().order_by("-date")[:3]

    return render(request,"blogs/index.html",{"posts":posts})


def All_blogs(request):
    
    all_posts = Post.objects.all()
    return render(request,"blogs/all-posts.html",{"all_blogs":all_posts})


class blog_details(View):
    
    def get(self,request,slug):
        identified_post = Post.objects.get(slug = slug)
        post_tags = identified_post.tags.all()
        form = commentForm()
        comments = identified_post.comment_set.all()

        return render(request, "blogs/detailed-post.html"
                      ,{"identified_blog":identified_post,
                                "post_tags" : post_tags
                                ,"form":form,
                                "comments":comments}
                                )
    def post(self,request,slug):
        identified_post = Post.objects.get(slug = slug)
        form = commentForm(request.POST)
        if form.is_valid():  
            comment = form.save(commit=False)
            comment.post = identified_post
            comment.save()

            return HttpResponseRedirect(reverse("detailed-blog",args=[identified_post.slug]))

        else:
            
            post_tags = identified_post.tags.all()
            form = commentForm()
            comments = identified_post.comment_set.all()

            return render(request, "blogs/detailed-post.html"
                          ,{"identified_blog":identified_post
                                    ,"post_tags" : post_tags,
                                    "form":form
                                    ,"comments":comments})

def about_us(request):
     return render(request,template_name="blogs/aboutus.html")

class addPost(CreateView):

    template_name = "blogs/new_post.html"
    model = Post
    success_url = reverse_lazy('starting-page')
    fields  = ["title","excerpt","image_name","content","author","tags"]
    
class addAuthor(CreateView):
    template_name = "blogs/add_author.html"
    model = Author
    success_url = reverse_lazy('starting-page')
    fields = "__all__"
