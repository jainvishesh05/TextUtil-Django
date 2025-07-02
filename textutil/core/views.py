from django.shortcuts import render
from django.http import HttpResponse
import string

# Create your views here.
def Home(request):
    return render(request , 'core/home.html')

def result(request):
    if request.method == 'POST':
        text = request.POST.get('text' ,'')
        operations = []
        count =None
        remove_punc = request.POST.get('remove_punc' ,'off')
        con_UPPER = request.POST.get('to_upper' , 'off')
        con_lower = request.POST.get('to_lower' , 'off')
        rem_newline = request.POST.get('remove_newline' ,'off')
        count_car = request.POST.get('char_count' , 'off')
        result_text = text

        if rem_newline == 'on':
            result_text = result_text.replace('\n', ' ').replace('\r', ' ')
            operations.append('Remove NewLine')

        if remove_punc == 'on':
            punctuations = string.punctuation
            result_text = ''.join(char for char in result_text if char not in string.punctuation)
            operations.append('Remove Punctuatin')

        if con_UPPER == 'on' and con_lower == 'off':
            result_text = result_text.upper()
            operations.append('convert to uppercase') 

        if con_lower == 'on':
            result_text = result_text.lower()
            operations.append('convert to lowercase')

        if count_car == 'on':
            count = len(result_text)
            operations.append('count Charactors')



        if not operations:
            operations.append('no operatio selected')
        context = {'result' : result_text,
                   'operations':  operations,
                   'char_count': count}
            
        return render(request , 'core/result.html' , context)
    return render(request, 'core/result.html')   



