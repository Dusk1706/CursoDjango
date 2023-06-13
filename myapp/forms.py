from django import forms

class CreateTask(forms.Form):
    title= forms.CharField(label="Titulo de tarea",max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea,label="Descripcion de tarea")
    