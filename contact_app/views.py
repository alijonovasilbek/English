from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm
from django.contrib.auth import authenticate, login,logout


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Foydalanuvchini boshqa sahifaga yo'naltirish, masalan 'bosh' sahifasiga
    else:
        form = UserCreationForm()
    return render(request, 'registeration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registeration/login.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Parol muvaffaqiyatli o'zgartirildi, foydalanuvchiga xabar berish
            messages.success(request, 'Parol muvaffaqiyatli o\'zgartirildi!')
            return redirect('home')  # O'zgartirish muvaffaqiyatli bo'lganidan so'ng bosh sahifaga yo'naltirish
        else:
            # Xatolarni sahifada ko'rsatish
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            return redirect('home')  # Xatolar borligi uchun sahifani qayta yuklash
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registeration/change_password.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')




