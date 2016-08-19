from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from books.forms import ContactForm
# Create your views here.
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',{'books':books,'query':q})
    return render_to_response('search_form.html',{'error':True})
        #return HttpResponse('Please submit a search term.')

def search_form(request):
    return render_to_response('search_form.html')



# def search(request):
#     error = False
#     if 'q' in request.GET:
#         q = request.GET['q']
#         if not q:
#             error = True
#         else:
#             books = Book.objects.filter(title__icontains=q)
#             return render_to_response('search_results.html',{'books':books,'query':q})
#     return render_to_response('search_form.html',{'error':True})
#         #return HttpResponse('Please submit a search term.')

# def search(request):
#     if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#         books = Book.object.filter(title__icontains=q)
#         return render_to_response('search_results.html',{'books':books,'query':q})
#     else:
#         return render_to_response('search_form.html',{'error':True})
#         #return HttpResponse('Please submit a search term.')



# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' %request.GET['q']
#     else:
#         message = 'You searched an empty form.'
#     return HttpResponse(message)
