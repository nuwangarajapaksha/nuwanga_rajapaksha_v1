from django.shortcuts import render


# Create your views here.

def photography(request):

    cameras_row1 = [
        'nikon-d7200'
    ]

    lenses_row2 = [
        'nikon-18-55', 'nikon-18-55'
    ]

    tech_icons_row3 = [
        'adobe-ps', 'adobe-lr'
    ]

    return render(request, 'photography.html', {
        'cameras_row1': cameras_row1,
        'lenses_row2': lenses_row2,
        'tech_icons_row3': tech_icons_row3,
    })
