from django.shortcuts import render,redirect
from django.http import JsonResponse
import openai

from django.contrib import auth
from django.contrib.auth.models import User
from.models import Chat
from django.utils import timezone

openai_api_key = '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'

#openai_api_key = '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'
openai.api_key = openai_api_key


def ask_openai(message): 
    reponse = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-16k-0613", 
        messages= [
            
            {"role":"system", "content":"you are an helpful assistent."},
            {"role":"user","content":message},

        ]

    )
    # print(reponse) 
    answer = reponse.choices[0].message.content.strip()
    return answer


def chatbot(request): 
    chats = Chat.objects.filter(user=request.user)
    if request.method == 'POST': 
        message = request.POST.get('message')
        response = ask_openai(message)
        chat = Chat(user =request.user, message=message, response=response,created_at=timezone.now())
        chat.save()
        return JsonResponse({'message':message,'response':response})
    return render(request, 'chatbot.html',{'chats':chats})


def register(request): 
    if request.method == 'POST': 
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2: 
            try: 
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request,user)
                return redirect('chatbot')
            except:  
                error_message = 'Error creating account'
                return render(request,'register.html',{'error_message':error_message})

        else: 
            error_message = 'Password dont match'
            return render(request,'register.html', {'error_message':error_message})
    return render(request,'register.html')


def login(request): 
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None: 
            auth.login(request,user) 
            return redirect('chatbot')
        else: 
            error_message = 'Invalid Username or Password'
            return render(request,'login.html',{'error_message':error_message})
    else: 
        return render(request,'login.html')



def logout(request): 
    auth.logout(request)
    return redirect('login')
