from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import View, FormView, CreateView

from newsletter.forms import JoinForm
from .models import Page


# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "pages/home.html", {})



class HomeView(SuccessMessageMixin, CreateView):
    template_name = 'pages/home.html'
    form_class  = JoinForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['page_obj'] = Page.objects.all().first() #.order_by("?").first()
        return context

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Thank you for joining!"

    # def form_valid(self, form):
    #     email = form.cleaned_data.get("email")
    #     # other things with email
    #     return super(HomeView, self).form_valid(form)
