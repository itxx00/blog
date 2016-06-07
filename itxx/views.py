#coding:utf-8
from django.http import HttpResponse


def hello(request):
    html = '''<html><meta http-equiv="refresh" content="0;url=http://itxx.sinaapp.com/blog/"></html>'''
    return HttpResponse(html)


def index(request):
    html = '''<html>
    <head>
      <title>技术改变生活 - 专注云计算服务研究</title>
      <meta name="keywords" content="云计算服务" />
      <meta name="description" content="技术让生活更简单" />
      <style type="text/css">
html,body,div,ul,li{
	margin:0;
	padding:0;
}
/*body*/
body{
	background:#000;
    background-image: url("media/img/bg.png");
	color:rgb(118,118,118);
	overflow-x:hidden;
}
a{
	color:rgb(118,118,118);
}
/*header*/
#header{
	text-align:center;
}
#logo{
	width:24.3%;
	min-width:100px;
	max-width:700px;
}
/*main*/
#main{
	width:100%;
	margin-top:20px;
}
#nav{
	width:40%;
	margin:auto;
	overflow:hidden;
}
#nav ul{
	overflow:hidden;
}
#nav ul li{
	margin: 100px;
	text-align:center;
	list-style:none;
}
#nav a{
	color:rgb(118,118,118);
	text-decoration:none;
	font:26px 微软雅黑;
}
#nav a:hover{
	color:#fff;
	font-size:26px;
	text-shadow:0 0 5px #fff;
}
#nav li{
	overflow:hidden;
}

/*footer*/
#footer{
	margin:0 auto;
	margin-top:200px;
	overflow:hidden;
    text-align:center;
	font:16px helvetica;
}
#footer a{
	font-family:georgia;
	text-decoration:none;
}
#footer a:hover{
	color:#fff;
	text-shadow:0 0 5px #fff;
}

    </style>
  </head>
  <body> 
	<div id="header"></div>
	<div id="main">
		<div id="nav">
			<ul>
				<li><a href='/blog/'>博客</a></li>
			</ul>
		</div>
	</div>
	<div id="footer">&copy;2011-2013 <a href="http://itxx.sinaapp.com">专注云计算</a></div>
    </body>
    </html>
    '''
    return HttpResponse(html)
    
def robots(request):
    txt = '''User-agent:*
Allow:/blog
Disallow:/media'''
    return HttpResponse(txt)