from django.shortcuts import render

from .models import Licenciatarios
from datetime import date

# Create your views here.
def index(request):
    latest_licenciatarios = list(Licenciatarios.objects.order_by('expedicion_fecha')[:5])

    for lic in latest_licenciatarios:
        # print(date.date(lic.expedicion_fecha))
        lic.status = lic.expedicion_fecha - date.today()

    ctx = {
        'licenciatarios':latest_licenciatarios,
    }
    return render(request, 'licenciatarios/index.html', ctx)
