from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, SignUpForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'

def landing_page(request):
    return render(request, 'landing.html')

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"

def lead_list(request):
    #return HttpResponse("Hello World")
    leads = Lead.objects.all()
    context = {
        "leads" : leads,
    }
    return render(request, 'leads/lead_list.html', context)

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead,
    }
    return render(request, 'leads/lead_detail.html', context)


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        # TO DO Send email
        send_mail(
            subject='New Lead has been created', 
            message='Go to the site to see the newly created lead.\n\nThank You,\nCRM Admin',
            from_email='test@example.com', recipient_list=['test2@example.com']
            )
        return super(LeadCreateView, self).form_valid(form)


def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
        return redirect('/leads')
    
    context = {
        'form': form,
        'lead' : lead
    }
    return render(request, 'leads/lead_update.html', context)


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

'''
-Basics of the forms.
def lead_create(request):
    form = LeadForm()
    if request.method == 'POST':
        print("Receiving a post request!")
        form = LeadForm(request.POST)
        if form.is_valid():
            print("The form is valid!")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
                )
            print("Lead created successfully!")
            return redirect('/leads')
    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)
    '''


class CustomUserSignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse('login')
