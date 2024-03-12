import random

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render





def stats_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request,'cat_info.html')
    print(request.POST)

    context = {
        'cat_name': request.POST.get('cat_name','input_text'),
        'cat_age': 1,
        'hapiness_level': 10,
        'satiety_level': 40,
        'action':request.POST.get("action",[])
    }

    if context['action'] == 'feed':
        context['hapiness_level']+=5
        context['satiety_level']+=15
    elif context['action'] == 'play':
        context['hapiness_level']+=15
        context['satiety_level']-=10
        # chance_cat = random.randint(1,3)
        # context['hapiness_level']
    elif context['action'] == 'sleep':
        context['hapiness_level']-=5

    return render(request, 'cat_info.html',context=context)




