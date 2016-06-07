# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    index_msg = 'Hello,hacker!'
    return render_to_response('sedb/base.html',{'index_msg': index_msg})
