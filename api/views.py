from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from twilio.rest import Client
from .forms import StudentForm
from .models import Student
def index(request):
    if request.method=="POST":
        # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
        client = Client('ACc2a7e10a8a382fc0595bd51a422de800','6daf149c93a7b1715bcd2e0b1e250f9a')
        name=request.POST.get('name')
        phone_no=request.POST.get('phone_no')
        print(request.FILES)
        img=request.FILES.get('img')
        print(img)
        obj=Student(name=name,phone_no=phone_no,img=img)
        obj.save()
        obj2 = obj.img.url
        obj1= request.build_absolute_uri() + obj2[1:]
        print(obj1)
        # this is the Twilio sandbox testing number
        # from_whatsapp_number='whatsapp:+91155238886'
        from_whatsapp_number='whatsapp:+14155238886'
        # from_whatsapp_number='whatsapp:+918221988235'
        # replace this number with your own WhatsApp Messaging number
        to_whatsapp_number=f'whatsapp:{phone_no}'
        media_url=f'http://127.0.0.1:8000/static/api/images/{img}'
        print(media_url)

        message=client.messages.create(body=f'Hello {name}',
                               media_url=obj1,
                               from_=from_whatsapp_number,
                               to=to_whatsapp_number)
        # print(message)
        # print(message.sid)
        return HttpResponse("Sent")
    else :
        fm=StudentForm()
    return render(request,'api/index.html',{'form':fm})