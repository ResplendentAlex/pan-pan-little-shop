from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Pan-Pan Self Portrait',
        'price': 'Rp. 200.000',
        'quantity': '10',
        'description': 'A self portrait of Pan-Pan, the panda.'
    }

    return render(request, "main.html", context)
