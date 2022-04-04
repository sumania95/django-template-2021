from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
import json
from django.contrib.auth import logout
#functions
from django.db.models.functions import Coalesce,Concat
from django.db.models import Q,F,Sum,Count
from django.db.models import Value
from django.urls import reverse
#datetime
from datetime import datetime
#JSON AJAX
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
success = 'success'
info = 'info'
error = 'error'
warning = 'warning'
question = 'question'

from django.utils import timezone
from application.render import (
    Render
)
# from application.models import (
#
# )
from django.contrib.auth.models import User

class Home(LoginRequiredMixin,TemplateView):
    template_name = 'pages/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['document_count'] = 0
        context['category_count'] = 0
        context['author_count'] = 0
        context['terms_count'] = 0
        total_size = 0
        size = 0
        for p in total_size:
            p.file.size
            size+=p.file.size
        context['total_size'] = size
        return context
