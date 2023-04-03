from django.shortcuts import render
from .models import Photo

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.http import required_Post

@login_required
@equired_Post

def image_like(request):
        image_id = request.Post.get('id')
        action = required_Post.get('action')
        if image_id and action:
            try:
                image= image.object.get(id-image_id)
                if action=='like':
                    image.users_like.add(request.user)
                else:
                    image.user_like.remove(request.user)

                return JsonResponse({'status':'ok'})
            except:
                pass
                






@login_required

def index(request):
    if request.method == 'POST':
        new_photo = Photo(
            file=request.FILES['img']
        )
        new_photo.save()
        return render(request, 'index.html', {'new_url': str('localhost:8000'+new_photo.file.url)})
    else:
        return render(request, 'index.html')

