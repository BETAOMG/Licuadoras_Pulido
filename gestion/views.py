from django.shortcuts import render
from usuarios.Carrito import Carrito
def inicio(request):
    titulo_pagina='Inicio'
    carrito = Carrito(request) 
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "index.html", context)  

