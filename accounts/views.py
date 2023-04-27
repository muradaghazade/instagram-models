from django.shortcuts import render
from accounts.models import User

def test_account(request, id):
    user = User.objects.get(pk=id)
    print(user.posts.all())
    context = {
        'user':user
    }
    return render(request, 'test.html', context)


