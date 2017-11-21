from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from .models import Materia
from django.shortcuts import render, get_object_or_404
from .forms import MateriaForm
from django.shortcuts import redirect

def materia_new(request):
    if request.method == "POST":
        form = MateriaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return render(request, 'materia/materia_edit.html', {'form': form})

    else:
        form = MateriaForm()
        return render(request, 'materia/materia_edit.html', {'form': form})
