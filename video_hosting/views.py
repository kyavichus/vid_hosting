from django.contrib.auth.views import LoginView
from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from .forms import AuthUserForm
from .models import Video, Rating, Category
from .services import open_file


def get_list_video(request):
    # slug = request.path.split('/')[-1]
    category = Category.objects.all()
    # print(request.user)
    if request.path == '/vote/':
        return render(request, 'video_hosting/home.html', {'video_list': Video.objects.exclude(category=1),
                                                           'category': category})
    return render(request, 'video_hosting/home.html', {'video_list': Video.objects.all().order_by('-id'),
                                                       'category': category})


def get_list_video_by_cat(request, slug):
    # slug = request.path.split('/')[-1]
    category = Category.objects.all()
    print(slug)
    return render(request, 'video_hosting/home.html', {'video_list': Video.objects.filter(category__slug=slug),
                                                       'category': category})


def get_video(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    #_rating = get_object_or_404(Rating, vid_id=pk)
    _rating = Rating.objects.filter(video_id=pk)
    return render(request, "video_hosting/video.html", {"video": _video, 'rating': _rating})


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

# @csrf_exempt
def rate_image(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        print(el_id)
        val = request.POST.get('val')
        print(val)
        # print(request.COOKIES)
        video = Video.objects.get(id=el_id)
        Rating.objects.filter(video=video, user_id=request.user).delete()
        video.rating_set.create(user_id=request.user, rating=val)

        return JsonResponse({'success': 'true', 'rate': val}, safe=False)
    return JsonResponse({'success': 'false'})


