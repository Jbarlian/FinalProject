from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [ url(r'^$', views.listblog), #(queryset=Post.objects.all().order_by("-date")[:25],
											#template_name="blog/blog.html")),
				url(r'^(?P<pk>\d+)$', views.viewblog),#DetailView.as_view(model= Post,
										#				template_name = 'blog/post.html')),
				url(r'^(?P<pk>\d+)/postcomment', views.postcomment)
    			]
