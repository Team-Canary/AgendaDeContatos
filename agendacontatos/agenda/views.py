# -*- encoding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from models import ItemAgenda
from forms import FormItemAgenda
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    lista_itens = ItemAgenda.objects.filter(usuario=request.user)
    return render(request, "lista.html",
                  {"lista_itens": lista_itens},context_instance=RequestContext(request))

@login_required
def adiciona(request):
    if request.method == "POST":
        form = FormItemAgenda(request.POST, request.FILES)
        if form.is_valid():
            item =form.save(commit=False)
            item.usuario =request.user
            item.save()
            return render(request, "salvo.html", {})
    else:
        form = FormItemAgenda()
    return render(request, "adiciona.html", {"form": form},
                  context_instance=RequestContext(request))

@login_required
def item(request, id_item):
    item =get_object_or_404(ItemAgenda, usuario=request.user, pk=id_item)
    if request.method == "POST":
        form = FormItemAgenda(request.POST, request.FILES, instance=item)
        if (form.is_valid()):
            form.save()
            return render(request, "salvo.html", {})
    else:
        form = FormItemAgenda(instance=item)
    return render(request, "item.html",{'form': form}, context_instance=RequestContext(request))

@login_required
def remove(request, id_item):
    item =get_object_or_404(ItemAgenda, usuario=request.user, pk=id_item)
    item = get_object_or_404(ItemAgenda, pk=id_item)
    if(request.method == "POST"):
        item.delete()
        return render(request, "removido.html", {})
    return render(request, "remove.html",{'item': item}, context_instance=RequestContext(request))