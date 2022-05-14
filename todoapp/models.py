from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Title', max_length=100, blank=False)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時',auto_now=True)

    def __str__(self):
        return self.title
