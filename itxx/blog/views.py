#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
#from django.http import HttpResponseRedirect
from itxx.blog.models import Config, Papertype,Paper,Link,Comment
import datetime, re
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from sae.mail import send_mail

def getinit():
    #初始化plists:文章分类
    plists = Papertype.objects.order_by('orderby')
    return plists


def index(request,paperid=0):
    #初始化值
    plists = getinit()
    #站点名称，从后台配置获取
    sitename = Config.objects.get().name

    if paperid == 0:
        paper = Paper.objects.latest()
    else:
        #如果不是首页，则有上一页
        paper = Paper.objects.get(id=paperid)

    typename = Papertype.objects.get(id=paper.papertype_id).typename
    comment = len(Comment.objects.filter(cid=paper.id))

    #paper_next = paper.get_next_by_createtime()
    paper_prev = paper.get_previous_by_createtime()
    #except:
    #    comment = False
    #    typename = False
    #    # 取出下一篇的标题，用于翻页按钮显示
    #    paper_next = False

    return render_to_response('blog/index.html',
          {'sitetitle':sitename,
          #'online':online,'papertype':plists,'links':links,
          'papertype':plists,
          'paper':paper,'comment':comment,'typename':typename,
          'prevpaper':paper_prev})


def papercomment(request,pid):
    #首页快速评论功能,页面中使用js异步加载
    paper = Paper.objects.get(id=pid) ##use paper id as url.	
    #######显示评论内容##########  
    comments = Comment.objects.filter(cid=pid)  
    #####添加评论#############
    success = False
    guestemail = False
    gname = False
    if 'email' in request.POST:
        guestemail = request.POST['email']
        match = re.search(r'[\w.-]+@[\w.-]+',guestemail)
        #match = re.search(r'(\w+|\w+-\w+)+@(gmail|qq|163)(.com)',guestemail)
        if not guestemail:
            return HttpResponse('{"state":"failed","time":"没有填email哦！"}')
        elif not match:
            return HttpResponse('{"state":"failed","time":"email填得不对哦！只能用公共邮箱gmail/qq/163 神马的哦"}')
            
    if 'nikename' in request.POST:
        gname = request.POST['nikename']
        if not gname:
            return HttpResponse('{"state":"failed","time":"没有填名字哦！"}')
    if 'comment' in request.POST:
        comment_p = request.POST['comment']
        if not comment_p:
            return HttpResponse('{"state":"failed","time":"没有填内容哦！"}')
        elif len(comment_p) > 100:
            return HttpResponse('{"state":"failed","time":"太多了就用pastebin哦！"}')
    	elif not errors:
       	    savecomment = Comment(cid=paper, email=guestemail, nikename=gname, comment=comment_p)
       	    savecomment.save()
       	    success = True
            return HttpResponse('{"state":"success","time":"' + datetime.datetime.now().strftime('%m/%d/%y %H:%M') + '"}')
    return render_to_response('blog/papercomment.html',
        {'paper':paper,
        'guestemail':guestemail,
        'postname':gname,
        'success':success,
        'cmts':comments,
        'cmtnumber':len(comments)})
    
def content(request,pid):
    #文章查看页面
    plists = getinit()
    ##use paper id as url.
    paper = Paper.objects.get(id=pid)
    typename = Papertype.objects.get(id=paper.papertype_id).typename
    ##show and add degree number
    if not paper.degree:
        degree = 0
    else:
        degree = paper.degree
    degreeGo = int(degree) + 1
    Paper.objects.filter(id = pid).update(degree = degreeGo)
    ###display the front and next paper link.
    try:
    	pold = Paper.objects.filter(id__lt = paper.id).order_by('-id')[0:1].values()[0]
    except:
        pold = False
    try:
    	pnew = Paper.objects.filter(id__gt = paper.id).order_by('id')[0:1].values()[0]   
    except:
        pnew = False
    #######显示评论内容##########
    comments = Comment.objects.filter(cid=pid)
    
    #####添加评论#############   
    errors = []
    success = False
    guestemail = False
    gname = False
    if 'email' in request.POST:
        guestemail = request.POST['email']
        match = re.search(r'[\w.-]+@[\w.-]+',guestemail)
        if not guestemail:
            return HttpResponse('{"state":"failed","time":"没有填email哦！"}')
        elif not match:
            return HttpResponse('{"state":"failed","time":"email填得不对哦xxx！"}')
            
    if 'nikename' in request.POST:
        gname = request.POST['nikename']
        if not gname:
            return HttpResponse('{"state":"failed","time":"没有填名字哦！"}')
    if 'comment' in request.POST:
        comment_p = request.POST['comment']
        if not comment_p:
            return HttpResponse('{"state":"failed","time":"没有填内容哦！"}')
        elif len(comment_p) > 100:
            return HttpResponse('{"state":"failed","time":"太多了就用pastebin哦！"}')
    	elif not errors:
       	    savecomment = Comment(cid=paper, email=guestemail, nikename=gname, comment=comment_p)
       	    savecomment.save()
       	    success = True
            send_mail('itxx00@gmail.com', 'New comment in blog...',
                'http://itxx.sinaapp.com/blog/content/'+pid+'#comments',
                ('smtp.gmail.com', 587,  'replyfromitxx@gmail.com', '2012df00##', True)
                )
            return HttpResponse('{"state":"success","time":"' + datetime.datetime.now().strftime('%m/%d/%y %H:%M') + '"}')
    return render_to_response('blog/content.html',
        {'request':request,
        'sitetitle':paper.title,'papertype':plists,
        'paper':paper,'typename':typename,'pold':pold,'pnew':pnew,'errors':errors,
        'guestemail':guestemail,'postname':gname,'success':success,
        'cmts':comments,'cmtnumber':len(comments)})  
    

def plist(request,ptype,ptid=0):
    #文章分类页面
    plists = getinit()
    joker = False
    if int(ptid) >= 9999:
        joker = True
    plist = Papertype.objects.get(id=ptype)
    typename = plist.typename
    ptitle = Paper.objects.filter(papertype=ptype).order_by("-createtime")[int(ptid)*30:(int(ptid)+1)*30]
    ptold = int(ptid)-1
    if ptold < 0:
        ptold = 0
    ptnew = int(ptid)+1
    if ptnew > 9999:
        joker = True
    return render_to_response('blog/list.html',
        {'sitetitle':typename,
        'papertype':plists,
        'typename':typename,'ptitle':ptitle,'ptold':ptold,'ptnew':ptnew,'ptype':ptype,'joker':joker})

    
def showimg(request,img_name):
    #显示博客内图片，重写图片url地址
    img_url = 'media/uploadimage/' + img_name
    image_data = open(img_url, "rb").read()
    return HttpResponse(image_data, mimetype="image/png")
    
def handler500(request):
    #500错误自定义
    plists = getinit()
    name = 'calm down，this is in the future...'
    content=''' '''
    return render_to_response('blog/500.html',{'sitetitle':name,'papertype':plists,'content':content})
def save_file(file,path=''):
    #在TinyMCE中扩展支持图片上传的功能,使用sae存储api
    import sae.const
    access_key = sae.const.ACCESS_KEY
    secret_key = sae.const.SECRET_KEY
    appname = sae.const.APP_NAME
    #domain_name:storage domain name
    domain_name = "itxxblog"
    import sae.storage
    stclient = sae.storage.Client()
    stobject = sae.storage.Object(file.read())
    url = stclient.put(domain_name, file.name, stobject)
    return url

@csrf_exempt
@login_required
def upload_image(request):  
    if request.method == 'POST':
        if "upload_file" in request.FILES:
            f = request.FILES["upload_file"]  
            savedfile = save_file(f)
            return HttpResponse(savedfile)
    return HttpResponse(u"")