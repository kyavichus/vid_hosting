from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Max
from django.http import StreamingHttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView

from . import forms
from .forms import AuthUserForm
from .models import Video, Rating, Category
from .services import open_file


def get_list_video(request):
    rating_table = {}
    for cat in Category.objects.all()[1:]:
        vid = Video.objects.filter(category=cat).order_by('-rating').first()
        rating_table[vid] = Rating.objects.filter(video=vid).first()
    category = Category.objects.all()
    page_num = request.GET.get('page', 1)

    # print(request.user)
    if request.path == '/vote/':
        object_list = Video.objects.exclude(category=1).order_by("-id")

        paginator = Paginator(object_list, 24, orphans=3)
        page_obj = paginator.page(page_num)
        return render(request, 'video_hosting/home.html', {'video_list': page_obj,
                                                           'category': category,
                                                           'rating_table': rating_table})
    object_list = Video.objects.all().order_by('-id')

    paginator = Paginator(object_list, 24, orphans=3)
    page_obj = paginator.page(page_num)
    return render(request, 'video_hosting/home.html', {'video_list': page_obj,
                                                       'category': category,
                                                       'rating_table': rating_table})


def get_list_video_by_cat(request, slug):
    category = Category.objects.all()
    print(slug)
    return render(request, 'video_hosting/home.html', {'video_list': Video.objects.filter(category__slug=slug).order_by("-id"),
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
        val = request.POST.get('val')
        # print(request.COOKIES)
        video = Video.objects.get(id=el_id)
        Rating.objects.filter(video=video, user_id=request.user).delete()
        video.rating_set.create(user_id=request.user, rating=val)

        return JsonResponse({'success': 'true', 'rate': val}, safe=False)
    return JsonResponse({'success': 'false'})

class VideoCreateView(CreateView):
    model = Video
    template_name = 'video_hosting/video_new.html'
    # fields = ['title', 'category', 'description', 'image', 'file']
    # fields = '__all__'

    form_class = forms.ModuleForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

    # def form_valid(self, form):
    #     print(form)
    #     self.object.save()
    #     return super().form_valid(form)

    # def form_invalid(self, form):
    #     print(form.errors)
    #     return super().form_invalid(form)


class VideoUpdateView(UpdateView):
    model = Video
    template_name = 'video_hosting/video_new.html'
    form_class = forms.ModuleForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

