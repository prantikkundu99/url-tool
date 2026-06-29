from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Urlshort
from string import digits,ascii_letters
from random import shuffle


# Create your views here.


def random_string_gen(num:int) -> str:
    main: list = list(ascii_letters+digits)
    shuffle(main)
    text:str =  "".join(main[:num])
    return text

def urlshort(requests):
    global store
    data = {
        "shorturl":"",
        "longurl":""
    }
    
    if requests.method == 'POST':
        url = requests.POST.get("link")
        while True:
            try:
                sturl = random_string_gen(6)
                Urlshort.objects.create(
                    code = sturl,
                    url = url
                )
                break
            except Exception as e:
                print(e)
            
        data.update({
            "shorturl":settings.BASE_URL+f"/{sturl}",
            "longurl":url
        })

    return render(
        request=requests, 
        template_name="urlshort.html", 
        context=data
    )

def urlredirect(requests, token:str):

    url = settings.BASE_URL

    try:
        info = Urlshort.objects.get(code=token)
        url = info.url
    except Exception as e:
        print(e)

    return redirect(url)

