from django.shortcuts import render

# Vista basada en una funcion
def index_views(request):
    return render(request, 'index.html/', {})

