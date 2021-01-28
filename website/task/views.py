from django.urls import reverse
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

# it will use client side validation, server will no nothing about this, this thing is solely done webpage itself.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="Add New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'task/index.html', {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        # creting a form variable by taking all of the data and filling all of the data
        # and filling it into this NewTaskForm, which will contain now all of the data the 
        # user submitted
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]  # this will give me access to all of the data the user submitted.
                              # and I want to get what task they submitted, bcz we had a variable
                              # called task inside of NewTaskForm, so add ["task"] to form.clean-data.
            
            tasks.append(task) # to add task
            return HttpResponseRedirect(reverse('task:index')) # to redirect to the task page on adding task.

        # if not valid show the error to the user
        else:
            return render(request, "task/add.html", {
                "form": form
                })
    # if empty submission redirect to the empty form
    return render(request, "task/add.html", {
        "form": NewTaskForm(),
    })
