from django.shortcuts import render


# Create your views here.


def portfolio(request):
    tech_icons_row1 = [
        'adobe', 'adobe-ps', 'adobe-ai', 'adobe-pr', 'adobe-ae', 'adobe-lr'
    ]
    return render(request, 'portfolio.html', {
        'tech_icons_row1': tech_icons_row1,
    })
