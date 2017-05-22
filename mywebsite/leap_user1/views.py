# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def list_users(request):
    return render(request, 'blog/post_list.html', {})

#views.list_users
