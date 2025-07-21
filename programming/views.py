from django.shortcuts import render


# Create your views here.
def programming(request):

    tech_icons_row1 = [
        'java', 'spring-boot', 'python', 'django', 'fastapi', 'react',
        'php', 'android', 'html5', 'css', 'javascript', 'docker'
    ]
    tech_icons_row2 = [
        'bootstrap', 'material-ui', 'git', 'jira', 'aws', 'android',
        'mysql', 'mongodb', 'postman', 'swagger'
    ]

    return render(request, 'programming.html', {
        'tech_icons_row1': tech_icons_row1,
        'tech_icons_row2': tech_icons_row2,
    })
