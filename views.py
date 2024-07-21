from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *

def index(request):
  
    if request.method == 'POST':
        add_book=BookForm(request.POST,request.FILES) # add_book=BookForm(request.POST) من اجل ترحيل المعلومات التي تضاف الى قاعده البيانات
    # ,request.FILES هذه من اجل ان تحفظ الصور التي سيتم اضافتها او اي معلومه كملف 
        if add_book.is_valid(): # اذا الفورم تم تعبئته من الادمن وليس مخترق
            add_book.save()
        add_category=CategoryForm(request.POST)   
        if add_category.is_valid(): # اذا الفورم تم تعبئته من الادمن وليس مخترق
            add_category.save()
    context={
        'category':Category.objects.all(),
        'books':Book.objects.all(),
        'form':BookForm(),
        'formcat':CategoryForm(),
        'allbooks':Book.objects.filter(active=True).count(),
        'booksolid':Book.objects.filter(status='solid').count(),
        'bookrental':Book.objects.filter(status='rental').count(),
        'bookavalible':Book.objects.filter(status='avalible').count(),
    }
    return render(request,'pages/index.html',context)

def books(request):
    search=Book.objects.all()
    title=None
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title:
            search=search.filter(title__icontains=title) 
    
    context={
        'category':Category.objects.all(),
        'books':search,
        'formcat':CategoryForm(),
    }
    return render(request,'pages/books.html',context)

def update(request,id):
    book_id=Book.objects.get(id=id)
    if request.method == 'POST':
        book_save=BookForm(request.POST,request.FILES,instance=book_id) # instance=book_id ليرجع بالبيانات الخاصة بهذه ال id
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save=BookForm(instance=book_id)
    context={
        'form':book_save,
    }
    return render(request,'pages/update.html',context)

def delete(request,id):
    book_delete=get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')
    