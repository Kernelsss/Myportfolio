from django.urls import path
from . import views

# urlpatterns — это обязательный список для Django
urlpatterns = [
        # '' означает пустой путь (главная страница)
    # views.home_page — ссылка на функцию, которую мы написали
    # name='home' — имя маршрута, чтобы ссылаться на него в будущем
    path('', views.home_page, name='home'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),  # новая строка
    path('contacts/', views.contacts, name='contacts'), # forms contacts
    path('download-resume/', views.download_resume, name='download_resume'),
    path('resume/', views.resume_page, name='resume_page'),
]
