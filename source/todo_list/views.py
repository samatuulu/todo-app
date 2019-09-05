from django.shortcuts import render, redirect
from todo_list.models import Things, STATUS_CHOICES


def home(request):
    jobs = Things.objects.all()
    return render(request, 'index.html', context={
        'jobs': jobs
    })


def detail_view(request):
    thing_id = request.GET.get('pk')
    job = Things.objects.get(pk=thing_id)
    context = {'job': job}
    return render(request, 'detail_view.html', context)


def create(request):

    context = {
        'status': STATUS_CHOICES
    }

    if request.method == 'GET':
        return render(request, 'create.html', context)
    elif request.method == 'POST':
        status = request.POST.get('status')
        description = request.POST.get('description')
        date = request.POST.get('date')
        Things.objects.create(description=description, status=status, date_of_completion=date)
        response = redirect('/')
        return response


def delete_task(request):
    thing_id = request.GET.get('pk')
    obj = Things.objects.get(pk=thing_id)
    obj.delete()
    response = redirect('/')
    return response
