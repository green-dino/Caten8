# views.py
import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Playbook
from .utils import PlaybookUtils, PlaybookGraphCreator, InteractiveGraphCreator

def create_playbook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        play_name = data.get('play_name')
        roles = data.get('roles')
        blocks = data.get('blocks')
        tasks = data.get('tasks')
        version = data.get('version')
        author = data.get('author')

        errors = PlaybookUtils.validate_input(play_name, roles, blocks, tasks)
        if errors:
            return JsonResponse({'errors': errors}, status=400)

        playbook = Playbook.objects.create(
            play_name=play_name,
            roles=roles,
            blocks=blocks,
            tasks=tasks,
            version=version,
            author=author
        )
        return JsonResponse({'message': 'Playbook created successfully', 'playbook_id': playbook.id})

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_playbook(request, playbook_id):
    playbook = get_object_or_404(Playbook, id=playbook_id)
    return JsonResponse({
        'play_name': playbook.play_name,
        'roles': playbook.roles,
        'blocks': playbook.blocks,
        'tasks': playbook.tasks,
        'version': playbook.version,
        'author': playbook.author
    })

def create_playbook_graph(request, playbook_id):
    playbook = get_object_or_404(Playbook, id=playbook_id)
    creator = PlaybookGraphCreator(playbook.play_name, playbook.roles, playbook.blocks, playbook.tasks)
    dot_representation = creator.get_dot()
    dot_representation.render(f'playbook_graph_{playbook_id}', format='png')
    return HttpResponse(f'Graph created for playbook {playbook_id}', content_type='text/plain')

def create_interactive_playbook_graph(request, playbook_id):
    playbook = get_object_or_404(Playbook, id=playbook_id)
    net = InteractiveGraphCreator.create_interactive_graph(playbook.play_name, playbook.roles, playbook.blocks, playbook.tasks)
    net.show(f'playbook_graph_{playbook_id}.html')
    return HttpResponse(f'Interactive graph created for playbook {playbook_id}', content_type='text/plain')