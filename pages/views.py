from django.views.generic import TemplateView
from allauth.account.views import EmailView

class HomePageView(TemplateView):
    template_name = "home.html"

class EmailPageView(EmailView):
    template_name = "email.html"
