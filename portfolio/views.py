from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Project
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from weasyprint import HTML
import os

def download_resume(request):
    # Данные для шаблона (можно передавать из модели)
    context = {
        'name': 'Руслан',
        'title': 'Python/Django Developer',
        'skills': ['Python', 'Django', 'HTML & CSS', 'Figma'],
        'experience': [
            {'company': 'Компания А', 'position': 'Разработчик', 'years': '2024–2026'},
        ],
        'education': 'СамГУ, факультет информатики',
    }
    template = get_template('portfolio/resume_template.html')
    html_content = template.render(context)

    # Генерируем PDF
    pdf_file = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Resume_Ruslan.pdf"'
    return response

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

def resume_page(request):
    return render(request, 'portfolio/resume_page.html')