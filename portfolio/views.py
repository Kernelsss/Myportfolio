from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Project
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def create_admin(request):
    User = get_user_model()
    if User.objects.filter(username='admin').exists():
        return HttpResponse("Суперпользователь уже существует. Войдите с логином admin и паролем admin123.")
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'
    )
    return HttpResponse("Суперпользователь создан! Войдите с логином admin и паролем admin123.")

def home_page(request):
    # Получаем все активные проекты, отсортированные по дате создания
    projects = Project.objects.filter(is_active=True).order_by
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)

def project_detail(request, pk):
    # Пытаемся найти проект по id, если не найден — выдаём 404 ошибку
    project = get_object_or_404(Project, pk=pk, is_active=True)
    context = {
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', context)

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Сохраняем в базу
            contact = form.save()
            
            # Отправляем письмо
            subject = f"Новое сообщение от {contact.name}: {contact.subject}"
            message = f"Имя: {contact.name}\nEmail: {contact.email}\n\nСообщение:\n{contact.message}"
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,   # обычно 'webmaster@localhost'
                [settings.CONTACT_EMAIL],      # твой email
                fail_silently=False,
            )
            
            messages.success(request, 'Ваше сообщение отправлено! Спасибо.')
            return redirect('contacts')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'portfolio/contacts.html', context)