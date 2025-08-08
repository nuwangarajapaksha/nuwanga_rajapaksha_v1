from django.http import Http404
from django.shortcuts import render


# Create your views here.
def programming(request):
    context = {
        'tech_icons': ['java', 'spring-boot', 'python', 'django', 'fastapi', 'react',
                       'php', 'android', 'html5', 'css', 'javascript', 'docker',
                       'bootstrap', 'material-ui', 'git', 'github', 'gitlab', 'jira', 'aws',
                       'mysql', 'mongodb', 'postman', 'swagger']
    }

    return render(request, 'programming.html', context)


def modal_content(request, filename):
    templates = {
        'melioraa.html': {
            'images': [f'melioraa{i:02d}' for i in range(2, 10)],
            'tech_icons': ['java', 'spring-boot', 'mysql', 'react', 'javascript', 'html5', 'css', 'material-ui',
                           'bootstrap', 'postman', 'swagger', 'git', 'gitlab', 'jira', 'aws', 'azure', 'digitalocean']
        },
        'dialog_power_app.html': {
            'images': [f'dialog-power-app{i:02d}' for i in range(2, 11)],
            'tech_icons': ['java', 'spring-boot', 'mysql', 'react', 'redux', 'javascript', 'html5', 'css', 'bootstrap',
                           'material-ui', 'flutter', 'android', 'postman', 'swagger', 'git', 'gitlab', 'jira', 'aws',
                           'docker']
        },
        'morex.html': {
            'images': [f'morex{i:02d}' for i in range(2, 13)],
            'tech_icons': ['php', 'mysql', 'vue-js', 'javascript', 'html5', 'css', 'bootstrap', 'grafana', 'git',
                           'gitlab', 'jira']
        },
        'ndcamera.html': {
            'images': [f'ndcamera{i:02d}' for i in range(2, 27)],
            'tech_icons': ['java', 'mysql', 'javascript', 'html5', 'css', 'bootstrap', 'android', 'firebase']
        },
        'pamunuwila_hardware.html': {
            'images': [f'pamunuwila-hardware{i:02d}' for i in range(2, 36)],
            'tech_icons': ['java', 'mysql']
        }
    }

    if filename not in templates:
        raise Http404("Template not allowed")

    context = templates[filename]  # Gets both 'images' and 'tech_icons'
    return render(request, filename, context)
