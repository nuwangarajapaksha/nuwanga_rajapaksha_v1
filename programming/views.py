from django.http import Http404
from django.shortcuts import render


# Create your views here.
def programming(request):
    tech_icons = [
        'java', 'spring-boot', 'python', 'django', 'fastapi', 'react',
        'php', 'android', 'html5', 'css', 'javascript', 'docker',
        'bootstrap', 'material-ui', 'git', 'github', 'gitlab', 'jira', 'aws',
        'mysql', 'mongodb', 'postman', 'swagger'
    ]

    return render(request, 'programming.html', {
        'tech_icons': tech_icons,
    })


def modal_content(request, filename):
    templates = {
        'melioraa.html': {
            'images': ['melioraa02', 'melioraa03', 'melioraa04', 'melioraa05', 'melioraa06', 'melioraa07',
                       'melioraa08', 'melioraa09'],
            'tech_icons': ['java', 'spring-boot', 'mysql', 'react', 'javascript', 'html5', 'css', 'material-ui',
                           'bootstrap', 'postman', 'swagger', 'git', 'gitlab', 'jira', 'aws', 'azure', 'digitalocean']
        },
        'dialog_power_app.html': {
            'images': ['dialog-power-app02', 'dialog-power-app03', 'dialog-power-app04', 'dialog-power-app05',
                       'dialog-power-app06', 'dialog-power-app07', 'dialog-power-app08', 'dialog-power-app09',
                       'dialog-power-app10'],
            'tech_icons': ['java', 'spring-boot', 'mysql', 'react', 'redux', 'javascript', 'html5', 'css', 'bootstrap',
                           'material-ui', 'flutter', 'android', 'postman', 'swagger', 'git', 'gitlab', 'jira', 'aws',
                           'docker']
        },
        'morex.html': {
            'images': ['morex02', 'morex03', 'morex04', 'morex05', 'morex06', 'morex07', 'morex08', 'morex09',
                       'morex10', 'morex11', 'morex12'],
            'tech_icons': ['php', 'mysql', 'vue-js', 'javascript', 'html5', 'css', 'bootstrap', 'grafana', 'git',
                           'gitlab', 'jira']
        },
        'ndcamera.html': {
            'images': ['ndcamera02', 'ndcamera03', 'ndcamera04', 'ndcamera05', 'ndcamera06', 'ndcamera07', 'ndcamera08',
                       'ndcamera09', 'ndcamera10', 'ndcamera11', 'ndcamera12', 'ndcamera13', 'ndcamera14', 'ndcamera15',
                       'ndcamera16', 'ndcamera17', 'ndcamera18', 'ndcamera19', 'ndcamera20', 'ndcamera21', 'ndcamera22',
                       'ndcamera23', 'ndcamera24', 'ndcamera25'],
            'tech_icons': ['java', 'mysql', 'javascript', 'html5', 'css', 'bootstrap', 'android', 'firebase']
        }
    }

    if filename not in templates:
        raise Http404("Template not allowed")

    context = templates[filename]  # Gets both 'images' and 'tech_icons'
    return render(request, filename, context)
