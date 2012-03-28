#-*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail
from forms import SubscriptionForm
from models import Subscription

def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscriptions/new.html', context)

    subscription = form.save()
    send_mail(subject=u'Cadastro com Sucesso',
                message=u'Obrigado pela sua inscricao!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[subscription.email])
    return HttpResponseRedirect(
        reverse('subscriptions:success', args=[ subscription.pk ]))

def new(request):
    form = SubscriptionForm(initial={
        'name': 'Entre com o seu nome',
        'cpf': 'Digite o seu CPF sem pontos',
        'email': 'Informe o seu email',
        'phone': 'Qual o seu telefone de contato?',
        })
    context = RequestContext(request, {'form': form})
    return render_to_response('subscriptions/new.html', context)

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def success(request, id, template_name='subscriptions/success.html'):
    subscription = get_object_or_404(Subscription, pk=id)
    return render(request, template_name, {'subscription':subscription})
