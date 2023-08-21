from django.shortcuts import render


def one(request):
    context = {'words_text': 'ASD'}
    return render(request, 'words/index.html', context=context)
    


