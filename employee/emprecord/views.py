# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee, Factory, Stream
from .forms import EmployeeForm, FactoryForm, StreamForm

def dashboard(request):
    context = {
        'total_employees': Employee.objects.count(),
        'total_factories': Factory.objects.count(),
        'total_streams': Stream.objects.count(),
        'recent_employees': Employee.objects.order_by('-hire_date')[:5],
    }
    return render(request, 'dashboard.html', context)

# Employee Views
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['streams'] = Stream.objects.filter(employee=self.object)
        return context

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'
    success_url = reverse_lazy('employee-list')

# Factory Views
class FactoryListView(ListView):
    model = Factory
    template_name = 'factory/factory_list.html'
    context_object_name = 'factories'

class FactoryDetailView(DetailView):
    model = Factory
    template_name = 'factory/factory_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['streams'] = Stream.objects.filter(factory=self.object)
        return context

class FactoryCreateView(CreateView):
    model = Factory
    form_class = FactoryForm
    template_name = 'factory/factory_form.html'
    success_url = reverse_lazy('factory-list')

class FactoryUpdateView(UpdateView):
    model = Factory
    form_class = FactoryForm
    template_name = 'factory/factory_form.html'
    success_url = reverse_lazy('factory-list')

class FactoryDeleteView(DeleteView):
    model = Factory
    template_name = 'factory/factory_confirm_delete.html'
    success_url = reverse_lazy('factory-list')

# Stream Views
class StreamListView(ListView):
    model = Stream
    template_name = 'stream/stream_list.html'
    context_object_name = 'streams'

class StreamCreateView(CreateView):
    model = Stream
    form_class = StreamForm
    template_name = 'stream/stream_form.html'
    success_url = reverse_lazy('stream-list')

class StreamUpdateView(UpdateView):
    model = Stream
    form_class = StreamForm
    template_name = 'stream/stream_form.html'
    success_url = reverse_lazy('stream-list')

class StreamDeleteView(DeleteView):
    model = Stream
    template_name = 'stream/stream_confirm_delete.html'
    success_url = reverse_lazy('stream-list')
