from django.db import models
from django .contrib.auth.models import User
from django.utils import timezone
# Create your models here.

conditions = (
        (1,'Joy'),
        (5,'Passionate'),
        (10,'Happy'),
        (15,'Positive'),
        (20,'Optimistic'),
        (25,'Bored'),
        (30,'Pessimistic'),
        (35,'Frustrated'),
        (40,'overwhelmed'),
        (45,'angry'),
)

class Thought(models.Model):
    user = models.ForeignKey(User, related_name='thoughts')
    recorded = models.DateTimeField(default=timezone.now , editable = False)
    condition = models.IntegerField(choices = conditions)
    notes = models.TextField(blank = True,default='')

    def  __str__(self):
        return '{}:{}'.format(self.recorded.strftime('%Y-%m-%d %H:%M:%S '),self.get_condition_display())







