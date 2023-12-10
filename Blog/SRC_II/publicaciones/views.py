from django.shortcuts import render, redirect
from .models import Publicacion
from django.views.generic import ListView, CreateView, UpdateView
from .forms import Publicarform

# View basada en una funcion, para enlistar las publicaciones.
# def publicaciones_view(request):
#     ctx = {
#         'publicaciones' : Publicacion.objects.all()
#     }
#     return render(request, 'publicaciones.html/', ctx)


# View basada en clasese para enlistar las publicaciones.
class PublicacionesView(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = Publicacion
    context_object_name = 'publicaciones'

# View basada en una funcion, para crear las publicaciones.
# def publicar_view(request):
#     if request.method == 'POST':
#         form = Publicarform(request.POST)
#         if form.is_valid():
#             nueva_publicacion = form.save()
#             return redirect('publicaciones')
#     else:
#         form = Publicarform()
#         ctx = {'form' : form}
#         return render(request, 'publicaciones/publicar.html', ctx)
    
# View basada en una clase, para crear las publicaciones.

class Publicar(CreateView):
    model = Publicacion
    template_name = 'publicaciones/publicar.html'
    form_class = Publicarform


# View basada en una clase, para MODIFICAR una publicacion.

class ModificarPublicacionView(UpdateView):
    model = Publicacion
    template_name = 'publicaciones/modificar-publicacion.html'
    form_class = Publicarform
    success_url = '../ver-publicaciones'



