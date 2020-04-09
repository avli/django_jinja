from django.shortcuts import render


def hello(request):
    user = request.GET.get('user') or 'Stranger'
    return render(request, 'app/hello.html', context={'user': user})
