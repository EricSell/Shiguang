from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from find1.models import Baike


def baike_list(request):
    if request.method == "GET":
        baikes = Baike.objects.all()
        baike_name = []
        for baike in baikes:
            baike_name.append(baike.name)
        data = {
            'status': 1,
            'msg': 'ok',
            'data':
                {
                    'baike_name': baike_name
                }
        }
        return JsonResponse(data)
    else:
        return JsonResponse({
            'status': 0,
            'msg': 'fail',
        })


def baike_detail(request):
    if request.method == "GET":
        baikes = Baike.objects.all()
        baike_name = []
        baike_content = []
        for baike in baikes:
            baike_name.append(baike.name)

        data = {
            'status': 1,
            'msg': 'ok',
            'data': {
                'baike_name': baike_name,
                'baike_content': baike_content,
            }
        }
