from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'Todo'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    project_id = models.IntegerField()
    assigned_to = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    priority = models.CharField(max_length=10, default='MEDIUM')
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'
        managed = False

    def __str__(self):
        return self.title