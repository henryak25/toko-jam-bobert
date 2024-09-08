from django.shortcuts import render
def show_main(request):
    context = {
        'description' : 'jujujuujujuupiter',
        'name': 'Pak Bepe',
        'price': 50
    }

    return render(request, "main.html", context)
# Create your views here.
