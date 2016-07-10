from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from app.forms import *
from app.processes import get_form
from app.processes import save_quote
from app.processes import get_feedback
from app.processes import save_feedback
from app.models import *
# Create your views here.
def home(request):
    context = RequestContext(request)
    return render_to_response('index.html',{},context_instance=context)

def portfolio_items(request):
    context=RequestContext(request)
    portfolio_list=portfolio.objects.all()
    print (portfolio_list)
    return render_to_response('portfolio.html',{
        'portfolio_list':portfolio_list,
    }, context_instance=context)

def pricelist(request):
    context= RequestContext(request)
    return render_to_response('pricing.html',{}, context_instance=context)

def quote(request):
    context= RequestContext(request)
    form = prospects(data=request.POST)
    if request.method == 'POST':
        data = {}
        get_form.GetForm.run(request.POST, data)
        save_quote.SaveQuote.run(data)
    return  render_to_response('quote.html', {}, context_instance=context)

def feedback(request):
    context=RequestContext(request)
    form = feedbackform(data=request.POST)
    if request.method=='POST':
        data={}
        get_feedback.GetForm.run(request.POST, data)
        save_feedback.SaveFeedback.run(data)
    return  render_to_response('feedback.html',{},context_instance=context)
