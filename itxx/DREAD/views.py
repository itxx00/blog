#coding:utf-8
from django.http import HttpResponse
from django import forms
from django.shortcuts import render_to_response

radio=['低：','中：','高：']
CHOICES1 = (('1', radio[0]+'泄露其他信息',), ('2', radio[1]+'泄露敏感信息',),('4',radio[2]+'获取完全控制权限；执行管理员操作；非法上传文件'))
CHOICES2 = (('1', radio[0]+'攻击者很难重复攻击',), ('2', radio[1]+'攻击者可以重复攻击，但有时间限制',),('4',radio[2]+'攻击者可以随意再次攻击'))
CHOICES3 = (('1', radio[0]+'漏洞利用条件非常苛刻',), ('2', radio[1]+'熟练的攻击者才能完成攻击',),('4',radio[2]+'初学者在短期内能掌握攻击方法'))
CHOICES4 = (('1', radio[0]+'极少用户，匿名用户',), ('2', radio[1]+'部分用户，非默认配置',),('4',radio[2]+'所有用户，默认配置，关键用户'))
CHOICES5 = (('1', radio[0]+'发现该漏洞极其困难',), ('2', radio[1]+'在私有区域，部分人能看到，需要深入挖掘',),('4',radio[2]+'漏洞很明显，攻击条件很容易获得'))

class SelectForm(forms.Form):
    choice_field1 = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES1,label='一、Damage Potential(潜在威胁)')
    choice_field2 = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES2,label='二、Reproducibility(可重复性)')
    choice_field3 = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES3,label='三、Exploitability(可利用性)')
    choice_field4 = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES4,label='四、Affected users(影响范围)')
    choice_field5 = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES5,label='五、Discoverability(可发掘性)')
    
def index(request):
    
    if request.POST:
        form = SelectForm(request.POST)
        if form.is_valid():
            d1=int(request.POST['choice_field1'][0])
            r=int(request.POST['choice_field2'][0])
            e=int(request.POST['choice_field3'][0])
            a=int(request.POST['choice_field4'][0])
            d2=int(request.POST['choice_field5'][0])
            score=d1+r+e+a+d2
            rate = False
            if 0 <= score <= 7:
            	rate = 'low'
            elif 8 <= score <= 12:
            	rate = 'mid'
            elif 13 <= score <= 20:
            	rate = 'high'
            else:
            	p = '神马情况？'
            result = 'D(%d)+R(%d)+E(%d)+A(%d)+D(%d) = %d' % (d1, r, e, a, d2, score)
            return render_to_response('DREAD/index.html',{'form':form,'result':result,'rate':rate})
    else:
        form = SelectForm(initial=request.GET)

    return render_to_response('DREAD/index.html',{'form': form})
