#coding:utf-8
from django.shortcuts import render_to_response
from itxx.search.models import Md5s
import hashlib 
import datetime

def search(request):

    error = False
    if 'q' in request.POST: ##crack md5
        hashlist = request.POST['q']
        qs = list(hashlist.split())
        passwds = []
        if not qs:
            error = True
            return render_to_response('search/base.html',{'error':error})
        for q in qs:
            if len(q) != 32:
                error = True
                return render_to_response('search/base.html',{'error':error})
            elif len(passwds) < 10:
                passwd = Md5s.objects.filter(hash_md5=q)
                a = str(passwd)
                passwd = a[8:-2]
                passwds.append(passwd)
            else:
                error = True
                return render_to_response('search/base.html',{'toomany':error})
        return render_to_response('search/search.html',{'hashmd5s':qs,'passwords':passwds})

    elif 'p' in request.POST:  ##gethash
        p = request.POST['p']
        if not p:
            error = True
        elif len(p) > 32:
            error = True
        else:
            pmd5 = hashlib.md5(p).hexdigest()
            if list(Md5s.objects.filter(hash_md5=pmd5)) == []:
                p1 = Md5s(passwd=p, hash_md5=pmd5)
                p1.save()
	    return render_to_response('search/encode.html',{'hashmd5':pmd5,'password':p})
    return render_to_response('search/base.html',{'error':error})
