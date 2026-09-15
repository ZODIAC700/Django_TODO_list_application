from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView ,FormView
from .forms import TaskForm
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django .contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task
from django.utils import timezone

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'base/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tasks = Task.objects.filter(user=self.request.user)

        context['total_tasks'] = tasks.count()
        context['pending_tasks'] = tasks.filter(complete=False).count()
        context['completed_tasks'] = tasks.filter(complete=True).count()
        
        today = timezone.localdate()

        overdue_tasks = tasks.filter(
            complete=False,
            due_date__lt=today
        )

        context['overdue_tasks'] = overdue_tasks
        context['overdue_count'] = overdue_tasks.count()
        return context
     
class CustomLoginView(LoginView):
  template_name= 'base/login.html'
  fields = '__all__'
  redirect_authenticated_user= True 
  
  def get_success_url(self):
   return reverse_lazy('dashboard')

class RegisterPage(FormView):
   template_name = 'base/register.html'
   form_class = UserCreationForm
   # redirect_authenticated = True
   success_url = reverse_lazy('dashboard')
   
   
   def form_valid(self, form):
      user = form.save()
      if user is not None:
         login(self.request,user)
         return super().form_valid(form)
   
   def get(self , *args , **kwargs):
      if self.request.user.is_authenticated:
         return redirect('tasks')
      return super(RegisterPage,self).get(*args , **kwargs)
   
class TaskList(LoginRequiredMixin, ListView):
   model = Task
   context_object_name='tasks'
   
   def get_context_data(self, **kwargs):
          context = super().get_context_data( **kwargs) 
          context['tasks'] =context['tasks'].filter(
             user = self.request.user)
          context['count'] = context['tasks'].filter(
                        complete=False).count()
          
          search_input = self.request.GET.get('search-area') or ''
          if search_input :
             context['tasks'] = context['tasks'].filter(
    title__startswith=search_input
)
             context['search-input'] = search_input 
          return context
   
    
   
class TaskDetail(LoginRequiredMixin, DetailView):
   model = Task
   context_object_name= 'task'
   template_name= 'base/task_detail.html'
   
class TaskCreate(LoginRequiredMixin, CreateView):
   model = Task 
   form_class = TaskForm
   success_url = reverse_lazy('tasks')
   
   def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
   
   
   
class TaskUpdate(LoginRequiredMixin, UpdateView):
   model = Task
   form_class = TaskForm
   success_url = reverse_lazy('tasks')
   
class TaskDelete(LoginRequiredMixin,DeleteView):
   model = Task
   context_object_name = 'task'
   success_url = reverse_lazy('tasks')