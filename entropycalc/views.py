
from django.shortcuts import render, redirect, get_object_or_404
from .models import PerkaraYudisial
from .forms import PerkaraForm

def daftar_perkara(request):
    daftar = PerkaraYudisial.objects.all().order_by('-created_at')
    return render(request, 'entropycalc/index.html', {'daftar': daftar})

def kalkulasi_baru(request):
    if request.method == 'POST':
        form = PerkaraForm(request.POST)
        if form.is_valid():
            perkara = form.save()
            return redirect('detail_perkara', pk=perkara.pk)
    else:
        form = PerkaraForm()
    return render(request, 'entropycalc/form.html', {'form': form})

def detail_perkara(request, pk):
    perkara = get_object_or_404(PerkaraYudisial, pk=pk)
    return render(request, 'entropycalc/entropycalc.html', {'perkara': perkara})