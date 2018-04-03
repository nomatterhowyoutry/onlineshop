from django.shortcuts import render
from django.http import JsonResponse

def cart_adding(request):
    return_dict = dict()

    session_key = request.session.session_key

    print(request.POST)

    return JsonResponse(return_dict)
