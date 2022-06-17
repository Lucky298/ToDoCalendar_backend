from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task_model(models.Model):
    title = models.CharField('Title', max_length=255)
    description = models.TextField('Description', null=True, blank=True)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='tasks',
                             null=True)
