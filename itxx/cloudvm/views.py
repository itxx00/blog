#coding:utf-8
from django.http import HttpResponse
#from django.http import HttpResponseRedirect


def index(request):
    html = '''<html>
    <head><title>星星，专注提供云主机服务</title></head>
   <body>
    <h1>服务说明</h1>
    <ul>
    <li>1. 服务对象仅限使用Linux系统（包括CentOS,Ubuntu,Debian,Redhat,etc.）的云主机；</li>
    <li>2. 仅服务于白道人群、合法服务、中小企业，黑道请绕行；</li>
    <li>3. 仅服务于追求长期稳定客户服务人群，瞎折腾者、好事者、没事找事者请绕行；</li>
    <li>4. 提供基于WEB的管理工具，开放API；</li>
    <li>5. 服务特色：针对每位客户提供定制化专业级服务；</li>
    <li>6. 限制条件：前期名额有限，欲合作的客户请mail(itxx00@gmail.com)联系。</li>
      </ul>
  
    </body>
  
    </html>'''
    return HttpResponse(html)