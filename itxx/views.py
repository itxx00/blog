#coding:utf-8
from django.http import HttpResponse

def scanv(request):
    html = '''mLzunSs23unsX1sk6L4AB2hFe8vGNED11DgCZ8ujLg6Ypp9A1F'''
    return HttpResponse(html)

def hello(request):
    html = '''<html><meta http-equiv="refresh" content="0;url=http://itxx.sinaapp.com/blog/"></html>'''
    return HttpResponse(html)
def google(request):
    html = '''google-site-verification: google96308fb5b75e6142.html'''
    return HttpResponse(html)
def index(request):
    html = '''<html>
    <head>
      <title>用技术改变生活---专注于云计算服务研究</title>
      <meta name="keywords" content="云计算服务" />
      <meta name="description" content="技术男，用技术让生活变得更简单" />
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
				<li><a href='/blog/'>我的博客</a></li>
			</ul>
		</div>
	</div>
	<div id="footer">&copy;2011-2013 <a href="http://itxx.sinaapp.com">专注云计算</a></div>
    </body>
    </html>
    '''
    return HttpResponse(html)
    
def robots(request):
    robotstxt = '''
User-agent:*
Allow:/blog
Disallow:/media

'''
    return HttpResponse(robotstxt)

    
def phpinfo(request):
    html = '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">
<!-- saved from url=(0047)http://manual.cidadevirtual.pt/cgi-bin/info.php -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1"><style type="text/css"><!--
A { text-decoration: none; }
A:hover { text-decoration: underline; }
H1 { font-family: arial,helvetica,sans-serif; font-size: 18pt; font-weight: bold;}
H2 { font-family: arial,helvetica,sans-serif; font-size: 14pt; font-weight: bold;}
BODY,TD { font-family: arial,helvetica,sans-serif; font-size: 10pt; }
TH { font-family: arial,helvetica,sans-serif; font-size: 11pt; font-weight: bold; }
//--></style>
<title>phpinfo()</title></head><body><table border="0" cellpadding="3" cellspacing="1" width="600" bgcolor="#000000" align="CENTER">
<tbody><tr valign="middle" bgcolor="#9999CC"><td align="left">
<h1>PHP Version 4.0.6</h1>
</td></tr>
</tbody></table><br>
<table border="0" cellpadding="3" cellspacing="1" width="600" bgcolor="#000000" align="CENTER">
<tbody><tr valign="baseline" bgcolor="#CCCCCC"><td bgcolor="#CCCCFF"><b>System</b></td><td align="left">SunOS sae.sina.com.cn 5.6 Generic_105181-21 sun4u sparc SUNW,Ultra-1</td></tr>
<tr valign="baseline" bgcolor="#CCCCCC"><td bgcolor="#CCCCFF"><b>Build Date</b></td><td align="left">Sep 28 2001</td></tr>
<tr valign="baseline" bgcolor="#CCCCCC"><td bgcolor="#CCCCFF"><b>Configure Command</b></td><td align="left">&nbsp;'./configure' '--prefix=/sae/php4' '--enable-discard-path' '--with-config-file-path=/sae/php4/lib' '--enable-safe-mode' '--with-exec-dir=/sae/php4/bin' '--with-informix'</td></tr>
<tr valign="baseline" bgcolor="#CCCCCC"><td bgcolor="#CCCCFF"><b>Server API</b></td><td align="left">CGI</td></tr>
<tr valign="baseline" bgcolor="#CCCCCC"><td bgcolor="#CCCCFF"><b>Virtual Directory Support</b></td><td align="left">disabled</td></tr>
<tr valign="baseline" bgcolor="#CCCCCC"><td bgcolor="#CCCCFF"><b>Configuration File (php.ini) Path</b></td><td align="left">/sae/php4/lib/php.ini</td></tr>
<tr valign="baseline" bgcolor="#CCCCCC"><td bgcolor="#CCCCFF"><b>ZEND_DEBUG</b></td><td align="left">disabled</td></tr>
<tr valign="baseline" bgcolor="#CCCCCC"><td bgcolor="#CCCCFF"><b>Thread Safety</b></td><td align="left">disabled</td></tr>
</tbody></table><br>
<table border="0" cellpadding="3" cellspacing="1" width="600" bgcolor="#000000" align="CENTER">
<tbody><tr valign="top" bgcolor="#CCCCCC"><td align="left">
This program makes use of the Zend scripting language engine:<br>Zend Engine v1.0.6, Copyright (c) 1998-2001 Zend Technologies<br><br>
</td></tr>
</tbody></table><br>
<h2 align="center">PHP License</h2>
<table border="0" cellpadding="3" cellspacing="1" width="600" bgcolor="#000000" align="CENTER">
<tbody><tr valign="top" bgcolor="#CCCCCC"><td align="left">
<p>
This program is free software; you can redistribute it and/or modify it under the terms of the PHP License as published by the PHP Group and included in the distribution in the file:  LICENSE
</p>
<p>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
</p>
<p>If you did not receive a copy of the PHP license, or have any questions about PHP licensing, please contact license@php.net.
</p>
</td></tr>
</tbody></table><br>
</body></html>
'''
    return HttpResponse(html)