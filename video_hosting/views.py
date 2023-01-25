from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Video, Rating
from .services import open_file


def get_list_video(request):
    if request.path == '/vote/':
        return render(request, 'video_hosting/home.html', {'video_list': Video.objects.exclude(category='Full')})
    return render(request, 'video_hosting/home.html', {'video_list': Video.objects.all()})


def get_video(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    #_rating = get_object_or_404(Rating, vid_id=pk)
    _rating = Rating.objects.filter(vid_id=pk)
    return render(request, "video_hosting/video.html", {"video": _video, 'rating': _rating})


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response


def rate_image(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        obj = Rating.objects.get(id=el_id)
        obj.rate = val
        obj.save()
        return JsonResponse({'success': 'true', 'rate': val}, safe=False)
    return JsonResponse({'success': 'false'})


