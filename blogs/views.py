from django.shortcuts import render
from .models import Blog, Book

def blog_list(request):
	blogs = Blog.objects.all()
	context={
		'blogs':blogs

	}
	return render(request, 'blogs/blog_list.html', context)

def books_list(request):
	books = Book.objects.all()
	context={
		'books': books

	}
	return render(request, 'blogs/books_list.html', context)

def books_detail(request, book_id):
	book = Book.objects.get(id = book_id)
	context={
		'book': book

	}
	return render(request, 'blogs/books_detail.html', context)











