from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Pan-Pan Self Portrait',
        'price': 'Rp. 200.000',
        'stock': '10',
        'description': 'A self portrait of Pan-Pan, the panda.'
    }

    return render(request, "main.html", context)

def show_credentials(request):
    context = {
        'name': 'Alexander William Lim',
        'npm': '2306207505',
        'class': 'PBP F',
    }

    return render(request, "main.html", context)