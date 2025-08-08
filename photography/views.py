from django.shortcuts import render


# Create your views here.

def photography(request):
    context = {
        'cameras': ['nikon-d7200'],
        'lenses': ['nikon-18-55', 'nikon-70-300'],
        'tech_icons': ['adobe-ps', 'adobe-lr'],
        'wildlife_images': [f'wildlife{i:02d}' for i in range(2, 8)],
        'model_images': [f'model{i:02d}' for i in range(2, 8)],
        'event_images': [f'event{i:02d}' for i in range(2, 8)],
        'landscape_images': [f'landscape{i:02d}' for i in range(2, 8)],
    }
    return render(request, 'photography.html', context)
