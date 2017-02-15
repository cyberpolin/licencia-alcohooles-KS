from django.shortcuts import render, redirect
from django.http import HttpResponse

from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from .models import Licenciatarios
from django.contrib.auth.models import User
from datetime import date
#//////////////////////////

from .forms import AddLicenciatario

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, View
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def index(request):
    latest_licenciatarios = list(Licenciatarios.objects.order_by('-id'))

    for lic in latest_licenciatarios:
        # print(date.date(lic.expedicion_fecha))
        lic.status = lic.expedicion_fecha - date.today()


    ctx = {
        'licenciatarios':latest_licenciatarios,
    }
    return render(request, 'licenciatarios/index.html', ctx)

@login_required
def show_licencia(request, id):
    return print_licencia(id)

@login_required
def print_licencia(id):

    l = Licenciatarios.objects.get(pk=id)

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="%s.pdf"' % l.folio

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


    p.drawString(250, 245, str(l.expedicion_fecha))
    p.drawString(250, 205, str(l.vencimiento_fecha))


    # Close the PDF object cleanly, and we're done.
    p.showPage()

    p.save()

    return response
@login_required
def licencia_nueva(request):

    current_id = Licenciatarios.objects.latest('folio')
    next_id = int(current_id.folio) + 1

    ctx = {}
    if request.method == 'POST':
        form =  AddLicenciatario(request.POST)
        if form.is_valid():
            formResult = form.save()
            pdf = print_licencia(current_id.pk)
            return pdf
        else:
            return render(request, 'licenciatarios/add-licenciatario.html', {'form':form})
    else:
        ctx['form'] = AddLicenciatario()
        ctx['title'] = 'Agrega un licenciatario'
        return render(request, 'licenciatarios/add-licenciatario.html', ctx)

@login_required
def licencia_edit(request, id):
    licenciatario = Licenciatarios.objects.get(pk=id)
    ctx = {}
    ctx['form'] = AddLicenciatario()
    ctx['title'] = 'Editar un licenciatario'
    return render(request, 'licenciatarios/add-licenciatario.html', ctx)


class LicenciaCreate(LoginRequiredMixin, CreateView):
    model = Licenciatarios
    form_class = AddLicenciatario
    template_name='licenciatarios/add-licenciatario.html'
    success_url = reverse_lazy('licenciatarios:index')

class LicenciaUpdate(LoginRequiredMixin, UpdateView):

    model = Licenciatarios
    form_class = AddLicenciatario
    success_url = reverse_lazy('licenciatarios:index')
class LicenciaDelete(LoginRequiredMixin, DeleteView):
    model = Licenciatarios
    success_url = reverse_lazy('licenciatarios:index')


class UsuarioList(LoginRequiredMixin, ListView):
    model = User

class UsuarioCreate(LoginRequiredMixin, CreateView):
    model = User
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('licenciatarios:usuario')

    def form_valid(self, form):
        user = User.objects.create_user(form.cleaned_data['username'],
                                        form.cleaned_data['email'],
                                        form.cleaned_data['password'])
        user.is_active = True
        # user.save()
        return super(UsuarioCreate, self).form_valid(form)

class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('licenciatarios:usuario')


class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('licenciatarios:usuario')

class ConfigUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('licenciatarios:usuario')


class LoginView(View):
    success_url = reverse_lazy('licenciatarios:usuario')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print('username')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return HttpResponseRedirect('/form')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
