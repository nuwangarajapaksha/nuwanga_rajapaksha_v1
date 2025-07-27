from django.shortcuts import render


# Create your views here.

def photography(request):

    cameras = [
        'nikon-d7200'
    ]

    lenses = [
        'nikon-18-55', 'nikon-70-300'
    ]

    tech_icons = [
        'adobe-ps', 'adobe-lr'
    ]

    wildlife_images = [
        'wildlife02', 'wildlife03', 'wildlife04', 'wildlife05', 'wildlife06', 'wildlife07'
    ]

    model_images = [
        'model02', 'model03', 'model04', 'model05', 'model06', 'model07'
    ]

    event_images = [
        'event02', 'event03', 'event04', 'event05', 'event06', 'event07'
    ]

    landscape_images = [
        'landscape02', 'landscape03', 'landscape04', 'landscape05', 'landscape06', 'landscape07'
    ]

    return render(request, 'photography.html', {
        'cameras': cameras,
        'lenses': lenses,
        'tech_icons': tech_icons,
        'wildlife_images': wildlife_images,
        'model_images': model_images,
        'event_images': event_images,
        'landscape_images': landscape_images,
    })
