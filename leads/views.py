from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from .models import Leads,User,Agent
from .forms import Leadform, LeadModelForm, CustomUserForm
from django.views.generic import TemplateView, ListView, UpdateView,DetailView,DeleteView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class LandingPageView(TemplateView):
    template_name='landing.html'

class SignupView(CreateView):
    template_name='registration/signup.html'
    form_class= CustomUserForm
    

    def get_success_url(self):
        return reverse('login')

def landing_page(request):
    return render(request, 'landing.html')

class LeadListView(LoginRequiredMixin, ListView):
    template_name='leads/first.html'
    queryset=Leads.objects.all()    
    context_object_name='lead'

def leads(request):
    lead=Leads.objects.all()
    context={'lead':lead}
    return render(request, 'leads/first.html',context)


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name='leads/second.html'
    queryset=Leads.objects.all()    
    context_object_name='lead'


def lead_detail(request,pk):
    lead=Leads.objects.get(id=pk)
    context={'lead':lead}
    return render(request, 'leads/second.html',context) 


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name='leads/lead_create.html'
    form_class=LeadModelForm
    

    def get_success_url(self):
        return reverse('leads:leads')

    def form_valid(self, form):
        send_mail(
            subject="A lead is created",
            message='Go to leads to see the new lead',
            from_email='test@xyz.com',
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)



def lead_create(request):
    form = LeadModelForm()
    if request.method=='POST':
        print('Method = post')
        form=LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context={'form':form,}
    return render(request, 'leads/lead_create.html',context)  

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name='leads/lead_update.html'
    queryset=Leads.objects.all()  
    form_class= LeadModelForm
    context_object_name='lead'

    def get_success_url(self):
        return reverse("leads:leads")    

def lead_update(request, pk):
    lead=Leads.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')     
    context={'form':form, 'lead':lead}    
    return render(request, "leads/lead_update.html", context) 


def lead_delete(request, pk):
    lead=Leads.objects.get(id=pk)
    lead.delete()            
    return redirect('/leads')

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name='leads/lead_delete.html'
    queryset=Leads.objects.all()  
    

    def get_success_url(self):
        return reverse("leads:leads")  




# def lead_update(request, pk):
#     lead=Leads.objects.get(id=pk)  
#     form = Leadform()
#     if request.method=='POST':
#         form=Leadform(request.POST)
#         if form.is_valid():
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']
#             lead.first_name=first_name
#             lead.last_name=last_name
#             lead.age=age
#             return redirect("/leads")
#     context={'form':form, 'lead':lead}
#     return render(request, "leads/lead_update.html", context)     


# def lead_create(request):
    # form = Leadform()
    # if request.method=='POST':
    #     print('Method = post')
    #     form=Leadform(request.POST)
    #     if form.is_valid():
    #         first_name=form.cleaned_data['first_name']
    #         last_name=form.cleaned_data['last_name']
    #         age=form.cleaned_data['age']
    #         agent=Agent.objects.first()
    #         Leads.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             age=age,
    #             agent=agent
    #         )
    #         return redirect("/")
    # context={'form':form,}
#     return render(request, 'leads/lead_create.html',context)     