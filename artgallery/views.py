from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.shortcuts import redirect
from .models import Categories, Painting


def index(request):
    return render(request, template_name='artgallery/index.html')


def registerPage(request):
    return render(request, 'accounts/register.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or Password Incorrect')
            return render(request, 'accounts/login.html',)
    else:
        return render(request, 'accounts/login.html',)


def logoutUser(request):

    logout(request)
    return redirect('login')


def publications(request):

    return render(request, template_name='artgallery/publications.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email =request.POST['email']
        message =request.POST['message']
        

        data = {
            'name': name,
            'email': email,
            'message': message
        }

        done_message = 'Your message has been sent. We will respond to you soon'

        try: 
            #send_mail(data['name'],data['message']+ '\n' ' from ' + data['email'],'info@kahwart.com',['info@kahwart.com'],fail_silently=False)
            msg=EmailMessage(data['name'],data['message']+ '\n' ' from ' + data['email'],'info@kahwart.com',['info@kahwart.com'])
            msg.send()
            return render(request,'artgallery/contact.html',{'message':done_message})
        except BadHeaderError:
            return render(request,'artgallery/index.html',{'message':done_message})
               
        #Just Cheking if it worked
        #print(data)
      
    else:
        return render(request, 'artgallery/contact.html')

def aboutus(request):

    return render(request, template_name='artgallery/aboutus.html')


def gallery(request):
    painting = Painting.objects.all()
    context = {
        'painting': painting,
    }
    return render(request, 'artgallery/gallery.html', context)


def shop(request):
    forsale = Painting.objects.filter(sale='YES')
    context = {
        'forsale': forsale
    }

    return render(request, 'artgallery/shop.html', context)


def services(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        number=request.POST['number']
        email=request.POST['email']
        city=request.POST['city']

        quote = {

            'fname': fname,
            'number': number,
            'email': email,
            'city': city

        }
        try:
            msg=EmailMessage(quote['fname'],'Phone Number : ' + quote['number'] + '\n'  'from '+ quote['email'],'info@kahwart.com',to=['info@kahwart.com'] )
            msg.send()
            message1='Thank You.'
            message2=' Our Design consultant will shortly call you to get more details on your requirements'
            return render(request, 'artgallery/services.html',{'message1':message1, 'message2':message2})
        except BadHeaderError:
            message1='Bad Header Error data. Please try again'
            return render(request, 'artgallery/services.html', {'messagae1':message1})
    else:
        return render(request, 'artgallery/services.html')

    

def exhibitions(request):

    return render(request, template_name='artgallery/exhibitions.html')


def workshop(request):

    return render(request, template_name='artgallery/workshop.html')


def gallery2(request):

    return render(request, 'artgallery/gallery2.html')

def error_404(request, exception):
    return render(request,'artgallery/404 page.html')


def quote(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        number=request.POST['number']
        email=request.POST['number']
        city=request.POST['city']

        quote = {

            'fname': fname,
            'number': number,
            'email': email,
            'city': city

        }
        try:
            msg=EmailMessage(quote['name'],quote['number'] + '\n'  'from'+ quote['email'] + quote['number'],'info@kahwart.com',to=['info@kahwart.com'] )
            msg.send()
            message1='Thank You.'
            message2=' Our Design consultant will shortly call you to get more details on your requirements'
            return render(request, 'artgallery/services.html',{'message1':message1, 'message2':message2})
        except BadHeaderError:
            message1='Bad Header Error data. Please try again'
            return render(request, 'artgallery/services.html', {'messagae1':message1})
    else:
        return render(request, 'artgallery/services.html')
