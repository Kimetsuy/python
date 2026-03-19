from django.http import HttpResponse

def teste_view(request):
    return HttpResponse("Olá, Mundo!")
def index_view(request):#index_view é a pagina inicial do site
    return HttpResponse("Bem-vindo à página inicial!")