from django.http import JsonResponse 
from rest_framework.decorators import api_view
from django.shortcuts import render

# Create your views here.
response = {
    'slackUsername': 'Keseven',
    'backend': True,
    'age': 24,
    'bio': 'I am from ogun state,I am a backend developer'
}

@api_view(['Get'])
def Home(request):
    return JsonResponse(response)

@api_view(['POST'])
def performOperation(request):
    if request.method == "POST":
        operation_type = request.data.get('operation_type')
        operation = str()
        no_list = []
        result = int()
        x = request.data.get('x' or 'X')
        y = request.data.get('y' or 'Y')

        if '+' in operation_type or 'plus' in operation_type or 'add' in operation_type or 'addition' in operation_type:
            operation = 'add'
        elif '*' in operation_type or 'multiply' in operation_type or 'multiplication' in operation_type :
            operation = 'multiply'
        elif '-' in operation_type or 'substrate' in operation_type or 'minus' in operation_type:
            operation = 'substrate'    

        if x == "" or x == None  and y == "" or y == None:
            arr = operation_type.split(' ')
            for num in arr:
                if num.isdigit():
                    no_list.append(int(num))
        else:
            no_list.append(int(x))
            no_list.append(int(y))

        if operation == "add":
            result = sum(no_list)
        elif operation == "substrate":
            result = no_list[0] - no_list[1]
        elif operation == "multiply":
            result = no_list[0] * no_list[1]

        response = {
                    'slackUsername': 'Keseven',
                    'result':  result,
                     "operation_type": operation
                }
    return JsonResponse(response, safe=False)
