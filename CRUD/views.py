

from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm
# Create your views here.



def home(request):

    task_list= Task.objects.all()
    tasks_orderd = task_list[::-1]
    form = TaskForm()

    if request.method == 'POST':
        
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
            
        else: form.add_error('task', 'vared');
    
    context = {
        'form'  : form,
        'tasks' : tasks_orderd,
    }
    return render(request, 'index.html', context)



def update(request, itemId):
    item = Task.objects.get(id=itemId)
    form = TaskForm(instance=item)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)

        if form.is_valid():
            
            form.save()
            
            return redirect('homeindex')

    context = {
        'form' : form,
    }
    return render(request, 'update.html', context)


def delete(request, itemId):

    item = Task.objects.get(id=itemId)


    context = {
        'item' : item
    }
    return render(request, 'delete.html', context)


def ok(request, itemId):

    item = Task.objects.get(id=itemId)
    item.delete()
    

    return redirect('/')


