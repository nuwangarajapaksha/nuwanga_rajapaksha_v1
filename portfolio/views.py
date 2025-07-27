from django.shortcuts import render


# Create your views here.


def portfolio(request):
    tech_icons = [
        'adobe', 'adobe-ps', 'adobe-ai', 'adobe-pr', 'adobe-ae', 'adobe-lr'
    ]
    return render(request, 'portfolio.html', {
        'tech_icons': tech_icons,
    })
