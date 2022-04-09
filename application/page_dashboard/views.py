from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
)

#functions
from django.db.models.functions import Coalesce,Concat
from django.db.models import Q,F,Sum,Count
from django.db.models import Value
from django.urls import reverse
#datetime
from datetime import datetime
#JSON AJAX
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils import timezone

success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

from django.contrib.auth.models import User

class Dashboard_Page(LoginRequiredMixin,TemplateView):
    template_name = 'pages/dashboard/page_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_1'] = 0
        context['title_2'] = 0
        context['title_3'] = 0
        context['title_4'] = 0
        context['incoming_document_count'] = 0
        context['outgoing_document_count'] = 0
        context['order_document_count'] = 0
        context['ordinance_resolution_document_count'] = 0
        return context
