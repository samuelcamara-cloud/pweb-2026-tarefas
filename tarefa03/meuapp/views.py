from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    lista_usuarios = [
        {"nome": "Michael Douglas", "matricula": 2024001, "idade": 23, "cidade": "Ruy Barbosa"},
        {"nome": "James Wilson", "matricula": 2024002, "idade": 55, "cidade": "Natal"},
        {"nome": "Peter Parker", "matricula": 2024003, "idade": 22., "cidade": "São Tomé"},
        {"nome": "Jucelino", "matricula": 2024004, "idade": 30., "cidade": "Barcelona"},
        {"nome": "Laiza sapa", "matricula": 2024005, "idade": 15., "cidade": "São Paulo do Potengi"},
    ]

    context = {
        "usuarios": lista_usuarios,
    }
    return render(request, "usuarios.html", context)