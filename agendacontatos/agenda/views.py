# -*- encoding: utf-8 -*-
import csv
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from models import ItemAgenda
from forms import FormItemAgenda
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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

@login_required
def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contatos.csv"'
    lista = ItemAgenda.objects.filter(usuario=request.user)
    writer = csv.writer(response)
    writer.writerow(['First Name', 'E-mail Address', 'Mobile Phone', 'Home Phone 2', 'Home Address'])
    for item in lista:
        var = item
        nome = "'"+var.nome+"'"
        email = "'"+var.email+"'"
        telefone1 = "'"+var.telefone1+"'"
        telefone2 = "'"+var.telefone2+"'"
        endereco = "'"+var.endereco+"'"

        writer.writerow([nome.encode('utf-8'), email.encode('utf-8'), telefone1.encode('utf-8'), telefone2.encode('utf-8')
, endereco.encode('utf-8')])
    return response
