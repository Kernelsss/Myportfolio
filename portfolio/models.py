from django.db import models

class Project(models.Model):
    """
    Модель для хранения информации о проекте.
    Каждый проект — это запись в базе данных.
    """
    title = models.CharField(max_length=100, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание")
    cover_title = models.CharField(max_length=50, verbose_name="Подпись на обложке", default="Проект")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    # НОВОЕ ПОЛЕ: выбор иконки
    ICON_CHOICES = [
        ('code', 'Код'),
        ('chat', 'Сообщение'),
        ('list', 'Список'),
        ('star', 'Звезда'),
        ('folder', 'Папка'),
        ('gear', 'Шестерёнка'),
        ('user', 'Пользователь'),
        ('globe', 'Глобус'),
    ]
    icon = models.CharField(
        max_length=20,
        choices=ICON_CHOICES,
        default='code',
        verbose_name="Иконка"
    )

    # НОВОЕ ПОЛЕ: порядок сортировки (число)
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Порядок (меньше = выше)"
    )

    # НОВОЕ ПОЛЕ: загруженное изображение
    image = models.ImageField(
        upload_to='projects_images/',
        blank=True,
        null=True,
        verbose_name="Изображение проекта"
    )

    image = models.ImageField(
        upload_to='projects/',        # папка для загрузки
        null=True,                    # можно оставить пустым
        blank=True,                   # поле необязательное
        verbose_name="Изображение"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['order', '-created_at']  # Сначала ордер, а затем новые
    
class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images',          # чтобы можно было обратиться project.images.all()
        verbose_name="Проект"
    )
    image = models.ImageField(
        upload_to='projects/gallery/',
        verbose_name="Изображение"
    )
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Порядок (меньше = выше)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения проекта"

    def __str__(self):
        return f"Изображение для {self.project.title}"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")

    def __str__(self):
        return f"Сообщение от {self.name} — {self.subject}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['-created_at']