from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import myModel
from.forms import TodoModelForm
# Create your views here.


def home(request):

    #return HttpResponse('HEllo EveryBody')
    tasks = myModel.objects.all()
    form = TodoModelForm()
    
    
    context = {
        'mytask':tasks,
        'form':form
    }
    return render(request,'myapp/home.html',context)



def completed(request,pk):

    value = myModel.objects.get(id= pk)

    value.completed = True
    value.save()
    return redirect('/')
def unmark(request,pk):
    value = myModel.objects.get(id= pk)
    value.completed = False
    value.save()
    return redirect('/')

def important(request,pk):
    value = myModel.objects.get(id = pk)
    value.important = True
    value.save()
    return redirect('/')


def add(request):
    if request.method == 'POST':
        form = TodoModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    else:
        return redirect('/')

def delete(request,pk):

    delete_item = myModel.objects.get(id = pk)

    delete_item.delete()
    return redirect('/')

def deleteall(request):

    letsdeleteall = myModel.objects.all()
    letsdeleteall.delete()

    return redirect('/')


def edit(request,pk):
    task = myModel.objects.get(id=pk)
    form = TodoModelForm(instance= task)
    if request.method == 'POST':
        form = TodoModelForm(request.POST, instance= task)

        if form.is_valid():
            form.save()
            return redirect('/')
    

    context = {'form':form}

    return render(request,'myapp/edit.html',context)



        

'''


def updatetodo(request,pk):

    update = myModel.objects.get(id=pk)
    form = TodoModelForm(request.POST,instance=update)
    print('sangam')
    if request.method == 'POST':
        form = TodoModelForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            update = myModel.objects.all()
            return redirect('/')

        else:
            return redirect('/')

'''