from datetime import date
from django.shortcuts import render

def index(request):
    context = {
        'first_name': 'ayham',
        'last_name': 'El Hour',
        'student_id': '120221684',
        'address': 'gaza, palestine',
        'email': 'ayham.a.alhour@gmail.com',
        'date_of_birth': date(2003, 5, 13),
    }

    return render(request, 'pages/index.html', context)