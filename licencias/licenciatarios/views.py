from django.shortcuts import render
from django.http import HttpResponse

from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from .models import Licenciatarios
from datetime import date
#//////////////////////////

from .forms import AddLicenciatario
form = AddLicenciatario()

# Create your views here.
def index(request):
    latest_licenciatarios = list(Licenciatarios.objects.order_by('expedicion_fecha')[:5])

    for lic in latest_licenciatarios:
        # print(date.date(lic.expedicion_fecha))
        lic.status = lic.expedicion_fecha - date.today()
        lic.print_url = '/licenciatarios/print/'+str(lic.pk)

    ctx = {
        'licenciatarios':latest_licenciatarios,
        'form': form,
    }
    return render(request, 'licenciatarios/index.html', ctx)

def print_licencia(request, id):

    l = Licenciatarios.objects.get(pk=id)

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="licencia.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setFont("Helvetica", 30)
    p.drawString(250, 705, l.folio)
    p.setFont("Helvetica", 11)
    p.drawString(100, 678, l.nombre)
    p.drawString(95, 661, l.razon_social)
    p.drawString(165, 647, l.nombre_comercial)
    p.drawString(210, 630, l.domicilio+ ', '+l.colonia+', '+l.municipio+', '+l.entidad)
    p.drawString(460, 595, str(l.cp))

    p.drawString(25, 580, str(l.telefono))
    p.drawString(260, 580, l.correo)
    p.drawString(465, 580, l.rfc)

    p.drawString(0, 520, l.actividad)
    p.drawString(0, 445, l.horario)


    # p.drawString(50, 250, "Tacha de vigencia")

    p.drawString(250, 245, str(l.expedicion_fecha))
    p.drawString(250, 205, str(l.vencimiento_fecha))


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    from reportlab.pdfbase import pdfdoc
    pdfdoc.PDFCatalog.OpenAction = '<</S/JavaScript/JS(this.print\({bUI:true,bSilent:false,bShrinkToFit:true}\);)>>'

    return response
