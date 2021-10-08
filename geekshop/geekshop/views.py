from django.shortcuts import render


def main(request):
    title = 'Главная'

    context = {
        'title': title,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'Контакты'

    context = {
        'title': title,
    }
    return render(request, 'geekshop/contact.html', context)
    return render(request, 'geekshop/index.html')


def contacts(request):
    return render(request, 'geekshop/contact.html')
