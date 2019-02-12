from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from fourth_umpire.predictions.pred import *
from .forms import *
from .models import *
import pandas as pd
import numpy as np

def main(request):
    return render(request, 'fourth_umpire/main.html', {})

def first_inn(request):
    if request.method == 'POST':
        title_form = InningsFirst(request.POST)
        if title_form.is_valid():
            team1 = title_form.cleaned_data['team1']
            team2 = title_form.cleaned_data['team2']
            return render(request, 'fourth_umpire/firstinn.html', context={'form1': title_form,'team1':team1})
    else:
        title_form = InningsFirst()
    return render(request, 'fourth_umpire/firstinn.html', context={'form1': title_form})

def second_inn(request):
    dataset=pd.read_csv('fourth_umpire/ipl.csv')
    if request.method == 'POST':
        title_form = InningsSecond(request.POST)
        if title_form.is_valid():
            team1 = title_form.cleaned_data['team1']
            team2 = title_form.cleaned_data['team2']
            p1=request.POST.get('p1')
            p2=request.POST.get('p2')
            p3=request.POST.get('p3')
            p4=request.POST.get('p4')
            p5=request.POST.get('p5')
            p6=request.POST.get('p6')
            p7=request.POST.get('p7')
            p8=request.POST.get('p8')
            p9=request.POST.get('p9')
            p10=request.POST.get('p10')
            p11=request.POST.get('p11')
            t1=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]
            bos=request.POST.get('bos')
            p12=request.POST.get('p12')
            p13=request.POST.get('p13')
            p14=request.POST.get('p14')
            p15=request.POST.get('p15')
            p16=request.POST.get('p16')
            p17=request.POST.get('p17')
            p18=request.POST.get('p18')
            p19=request.POST.get('p19')
            p20=request.POST.get('p20')
            p21=request.POST.get('p21')
            p22=request.POST.get('p22')
            t2=[p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22]
            batsman=bos
            bowlers = t2
            role = 'batting'
            if batsman in t2:
                role = 'bowling'
            asc = False
            if role == 'bowling':
                bowlers = t1
                asc = True
            l=dataset[(dataset['batsman'] == batsman) & (dataset['bowler'].isin(bowlers))].sort_values('metric', ascending=asc)['bowler'].values

            return render(request, 'fourth_umpire/secondinn.html', context={'form2': title_form,'print':l,'batsman':batsman})
    else:
        title_form = InningsSecond()
    return render(request, 'fourth_umpire/secondinn.html', context={'form2': title_form})
