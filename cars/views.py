from cars.models import Car, Agendamento
from django.shortcuts import render, redirect, get_object_or_404
from cars.forms import CarModelForm, AgendamentoForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('modelo')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(modelo__icontains=search)
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'


@login_required(login_url='login')
def criar_agendamento(request):
    erro = None

    if request.method == "POST":
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            carro = form.cleaned_data["carro"]
            data_hora = form.cleaned_data["data_hora"]

            conflito = Agendamento.objects.filter(
                carro=carro,
                data_hora=data_hora,
                status__in=["pendente", "confirmado"]
            ).exists()

            if conflito:
                erro = "Já existe um agendamento para esse carro nesse horário."
            else:
                agendamento = form.save()
                return redirect("detalhe_agendamento", pk=agendamento.pk)
    else:
        form = AgendamentoForm()

    return render(request, "criar_agendamentos.html", {
        "form": form,
        "erro": erro
    })


@login_required(login_url='login')
def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by("-data_hora")
    return render(request, "lista_agendamentos.html", {
        "agendamentos": agendamentos
    })


@login_required(login_url='login')
def detalhe_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    return render(request, "detalhe_agendamento.html", {
        "agendamento": agendamento
    })