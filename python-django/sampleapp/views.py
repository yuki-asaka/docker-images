import logging
from time import sleep

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render


logger = logging.getLogger(__name__)


@login_required
def index(request):
    return render(request, 'sampleapp/index.html')


def add(request):
    if request.method == 'GET':
        num1 = int(request.GET.get('num1', 0))
        num2 = int(request.GET.get('num2', 0))

        result = num1 + num2
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)


def divide(request):
    if request.method == 'GET':
        num1 = int(request.GET.get('num1', 0))
        num2 = int(request.GET.get('num2', 1))

        # if num2 == 0:
        #     return JsonResponse({'error': 'Division by zero'}, status=400)
        sleep(3)
        result = num1 / num2
        # except ZeroDivisionError as e:
        #     logger.exception(e)
        #     return JsonResponse({'error': 'Division by zero'}, status=400)

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
