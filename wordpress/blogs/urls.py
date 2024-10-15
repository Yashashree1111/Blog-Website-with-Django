from django.urls import path
from . import views

urlpatterns = [
    path("",views.starting_page,name="starting-page"),
    path("blogs/",views.All_blogs,name="all-blogs"),
    path("blogs/<slug:slug>",views.blog_details.as_view(),name="detailed-blog"),
    path("about",views.about_us,name="about-us"),
    path("add-post",view=views.addPost.as_view(),name="add_post"),
    path("add-author",views.addAuthor.as_view(),name="add_author")
]
