from django.shortcuts import render
from string import digits,ascii_letters,punctuation
from random import shuffle
# Create your views here.

def random_string_pass(num:int) -> str:
    main: list = list(ascii_letters)
    shuffle(main)
    text:str =  "".join(main[:num])
    return text

def random_stringsymnum_pass(num:int) -> str:
    while True:
        main: list = list(ascii_letters+digits+punctuation)
        shuffle(main)
        text:str =  "".join(main[:num])
        if any(c in digits for c in text) and any(c in punctuation for c in text):
            return text


def random_stringnum_pass(num:int) -> str:
    while True:
        main: list = list(ascii_letters+digits)
        shuffle(main)
        text:str =  "".join(main[:num])
        if any(c in digits for c in text) :
            return text
def random_stringsym_pass(num:int) -> str:
    while True:
        main: list = list(ascii_letters+punctuation)
        shuffle(main)
        text:str =  "".join(main[:num])
        if any(c in punctuation for c in text) :
            return text
def passgenerator(requests) :
    password = "abc123%$"
    data = {
        "pass":"",
        "cn":"",
        "nm":"",
        "sy":""
    }
    if requests.method == 'POST':
        cn = int (requests.POST.get("charnum"))
        nm = requests.POST.get("numyes")
        sy = requests.POST.get("symyes")
        if nm and sy :
            password = random_stringsymnum_pass(cn)
        elif nm and not sy :
            password = random_stringnum_pass(cn)
        elif sy and not nm :
            password = random_stringsym_pass(cn)
        else :
            password = random_string_pass(cn)

        data.update({
                "pass":password,
                "cn":cn,
                "nm":nm,
                "sy":sy,
                "heelo":"heelo"
            })
    return render(
        request=requests, 
        template_name="passgen.html", 
        context=data
    )