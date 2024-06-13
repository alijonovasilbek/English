from django.views.generic import ListView
from .models import Category, Dars, Bitriuvchilar
from django.views.generic import DetailView
from django.shortcuts import redirect
from .forms import CommentForm
import json
from  time import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Dars
import time
from django.shortcuts import render, get_object_or_404
from .models import NewsTeacher

def index(request):
    latest_btr = Bitriuvchilar.objects.all()
    context = {
        'latest_btr': latest_btr,
    }
    return render(request, 'main.html', context)


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dars_list'] = self.object.dars_set.all()  # Get all Dars related to this category
        return context


class DarsListView(ListView):
    model = Dars
    template_name = 'dars_list.html'
    context_object_name = 'dars'

class DarsDetailView(DetailView):
    model = Dars
    template_name = 'dars_detail.html'
    context_object_name = 'dars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        context['msg'] = False
        if self.request.user.is_authenticated:
            user = self.request.user
            if self.object.likes.filter(id=user.id).exists():
                context['msg'] = True

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'like' in request.POST:
            return self.handle_like(request)
        else:
            return self.handle_comment(request)

    def handle_comment(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.dars = self.object
            comment.user = request.user
            comment.save()
            return redirect('dars_detail', pk=self.object.pk)
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)

    def handle_like(self, request):
        if request.user.is_authenticated:
            user = request.user
            if self.object.likes.filter(id=user.id).exists():
                self.object.likes.remove(user)
                msg = False
            else:
                self.object.likes.add(user)
                msg = True
            return redirect('dars_detail', pk=self.object.pk)
        else:
            return redirect('login')  # или любая другая логика для неавторизованных пользователей


def like_post(request):
    data = json.loads(request.body)
    id = data["id"]
    post = get_object_or_404(Dars, id=id)
    already_liked = False

    if request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            already_liked = True
        else:
            post.likes.add(request.user)

    likes = post.likes.count()

    info = {
        "already_liked": already_liked,
        "num_of_likes": likes
    }

    return JsonResponse(info, safe=False)


@csrf_exempt
def increment_view_count(request, pk):
    if request.method == 'POST':
        dars_instance = get_object_or_404(Dars, pk=pk)
        viewed_key = f'viewed_dars_{pk}'

        # Check if the view count was incremented within the last 10 seconds
        last_view_time = request.session.get(viewed_key)
        current_time = time.time()

        if not last_view_time or (current_time - last_view_time > 15):
            dars_instance.view_count += 1
            dars_instance.save()
            request.session[viewed_key] = current_time
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'View count already incremented within the last 10 seconds.'}, status=400)
    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed.'}, status=405)


def news_list(request):
    news = NewsTeacher.objects.all().order_by('-date')
    return render(request, 'news_list.html', {'news': news})


def news_detail(request, pk):
    news_item = get_object_or_404(NewsTeacher, pk=pk)
    return render(request, 'news_detail.html', {'news_item': news_item})
