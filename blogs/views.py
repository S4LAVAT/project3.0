from django.shortcuts import render
from .models import Blog

def blog_list(request):
	blogs = Blog.objects.all()
	context={
		'blogs':blogs

	}
	return render(request, 'blogs/blog_list.html', context)
