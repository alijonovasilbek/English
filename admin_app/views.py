from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from app_pages.models import Category
from .form import CategoryForm
from django.shortcuts import render, redirect
from .form import DarsForm
from app_pages.models import  Bitriuvchilar
from admin_app.models import  Ustoz


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('category_list')


def add_dars(request):
    if request.method == 'POST':
        form = DarsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dars_list")

    else:
        form = DarsForm()
    return render(request, 'add_dars.html', {'form': form})


def index1(request):
    ustozlar = Ustoz.objects.all()
    latest_btr = Bitriuvchilar.objects.all()
    context = {
        'ustozlar': ustozlar,
        'latest_btr': latest_btr,
    }
    return render(request, 'ustoz_list.html', context)


def admin(request):
    return render(request,'admin.html')