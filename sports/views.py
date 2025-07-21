from django.shortcuts import render


# Create your views here.
def sports(request):
    images_row1 = [
        'java', 'spring-boot', 'python', 'django', 'fastapi', 'react',
        'php', 'android', 'html5', 'css', 'javascript', 'docker'
    ]
    images_row2 = [
        'bootstrap', 'material-ui', 'git', 'jira', 'aws', 'android',
        'mysql', 'mongodb', 'postman', 'swagger'
    ]
    return render(request, 'sports.html', {
        'images_row1': images_row1,
        'images_row2': images_row2,
    })
