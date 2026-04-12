from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Task

@api_view(['POST'])
def mark_overdue(request):
    today = timezone.now().date()
    updated = Task.objects.filter(
        due_date__lt=today
    ).exclude(
        status__in=['DONE', 'OVERDUE']
    ).update(status='OVERDUE')
    return Response({'success': True, 'marked_overdue': updated})

@api_view(['PATCH'])
def update_task_status(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({'success': False, 'message': 'Task not found'}, status=404)

    new_status = request.data.get('status')

    if task.status == 'OVERDUE':
        if new_status == 'IN_PROGRESS':
            return Response({'success': False, 'message': 'Overdue tasks cannot move back to IN_PROGRESS'}, status=422)

    task.status = new_status
    task.save()
    return Response({'success': True, 'data': {'id': task.id, 'status': task.status}})