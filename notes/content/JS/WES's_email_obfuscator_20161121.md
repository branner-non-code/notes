## WES's email obfuscator

From http://69.164.222.43/antispam.html (20161121)

### Script

```js
  function genScript()
  {
  var s = new String()
  var a = new Array()
  var a2 = new Array()
  var emstr = document.getElementById("textemail").value
  
  for(i=0; i<emstr.length; i++)
  {
  a[i] = Math.floor(Math.random()*255)
  a2[i] = emstr.charCodeAt(i) - a[i]
  }
  
  
  s = "<script type=" + String.fromCharCode(34) + "text/javascript" + String.fromCharCode(34) + ">\n\n"
  s = s + "function dispEmail()\n{\nvar s=new String()\nvar a=new Array()\nvar a2=new Array()\n"
  for(i=0; i<emstr.length; i++)
  {
  s = s + "a[" + i + "] = " + a[i] + "\n"
  }
  
  for(i=0; i<emstr.length; i++)
  {
  s = s + "a2[" + i + "] = " + a2[i] + "\n"
  }
  
  s = s + "s = String.fromCharCode("
  
  for(i=0; i<emstr.length-1; i++)
  {
  s = s + "a[" + i + "]+a2[" + i + "],"
  }
  s = s + "a[" + i + "]+a2[" + i + "])\n"
  
  s = s + "var x=document.getElementById(" + String.fromCharCode(34) + "emaddrtext" + String.fromCharCode(34)+")\n"
  s = s + "x.value = s\n"
  s = s + "x.select()\n}\n\n"
  s = s + "<" + String.fromCharCode(47) + "script>\n\n\n\n"
  s = s + "<html>\n<body>\n\n<input type=" + String.fromCharCode(34) + "button" + String.fromCharCode(34)
  s = s + "\nonclick=" + String.fromCharCode(34) + "dispEmail()" + String.fromCharCode(34)
  s = s + "\nvalue=" + String.fromCharCode(34) + "E-Mail:" + String.fromCharCode(34) + String.fromCharCode(47) + ">\n"
  
  s = s + "<input type=" + String.fromCharCode(34) + "text" + String.fromCharCode(34)
  s = s + "\nid=" + String.fromCharCode(34) + "emaddrtext" + String.fromCharCode(34)
  s = s + "\nreadonly=" + String.fromCharCode(34) + "readonly" + String.fromCharCode(34) + "\n"
  s = s + "size=" + String.fromCharCode(34) + emstr.length + String.fromCharCode(34)
  s = s + "\n" + String.fromCharCode(47) + ">\n\n"
  s = s + "<" + String.fromCharCode(47) + "body>\n"
  s = s + "<" + String.fromCharCode(47) + "html>"
  
  document.getElementById("scriptOutput").value = s
  
  
  s = String.fromCharCode(a2[0]+a[0],a2[1]+a[1],a2[2]+a[2],a2[3]+a[3],a2[4]+a[4])
  
  var x=document.getElementById("textemail")
  x.value = emstr
  }
```

### HTML page

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  <title>Email obfuscator</title>
  <style type="text/css">code{white-space: pre;}</style>
  <link rel="stylesheet" href="light.css" type="text/css" />
  
  <script type="text/javascript">
  
  function genScript()
  {
  var s = new String()
  var a = new Array()
  var a2 = new Array()
  var emstr = document.getElementById("textemail").value
  
  for(i=0; i<emstr.length; i++)
  {
  a[i] = Math.floor(Math.random()*255)
  a2[i] = emstr.charCodeAt(i) - a[i]
  }
  
  
  s = "<script type=" + String.fromCharCode(34) + "text/javascript" + String.fromCharCode(34) + ">\n\n"
  s = s + "function dispEmail()\n{\nvar s=new String()\nvar a=new Array()\nvar a2=new Array()\n"
  for(i=0; i<emstr.length; i++)
  {
  s = s + "a[" + i + "] = " + a[i] + "\n"
  }
  
  for(i=0; i<emstr.length; i++)
  {
  s = s + "a2[" + i + "] = " + a2[i] + "\n"
  }
  
  s = s + "s = String.fromCharCode("
  
  for(i=0; i<emstr.length-1; i++)
  {
  s = s + "a[" + i + "]+a2[" + i + "],"
  }
  s = s + "a[" + i + "]+a2[" + i + "])\n"
  
  s = s + "var x=document.getElementById(" + String.fromCharCode(34) + "emaddrtext" + String.fromCharCode(34)+")\n"
  s = s + "x.value = s\n"
  s = s + "x.select()\n}\n\n"
  s = s + "<" + String.fromCharCode(47) + "script>\n\n\n\n"
  s = s + "<html>\n<body>\n\n<input type=" + String.fromCharCode(34) + "button" + String.fromCharCode(34)
  s = s + "\nonclick=" + String.fromCharCode(34) + "dispEmail()" + String.fromCharCode(34)
  s = s + "\nvalue=" + String.fromCharCode(34) + "E-Mail:" + String.fromCharCode(34) + String.fromCharCode(47) + ">\n"
  
  s = s + "<input type=" + String.fromCharCode(34) + "text" + String.fromCharCode(34)
  s = s + "\nid=" + String.fromCharCode(34) + "emaddrtext" + String.fromCharCode(34)
  s = s + "\nreadonly=" + String.fromCharCode(34) + "readonly" + String.fromCharCode(34) + "\n"
  s = s + "size=" + String.fromCharCode(34) + emstr.length + String.fromCharCode(34)
  s = s + "\n" + String.fromCharCode(47) + ">\n\n"
  s = s + "<" + String.fromCharCode(47) + "body>\n"
  s = s + "<" + String.fromCharCode(47) + "html>"
  
  document.getElementById("scriptOutput").value = s
  
  
  s = String.fromCharCode(a2[0]+a[0],a2[1]+a[1],a2[2]+a[2],a2[3]+a[3],a2[4]+a[4])
  
  var x=document.getElementById("textemail")
  x.value = emstr
  }
  
  </script>
</head>
<body>
<div id="header">
<h1 class="title">Email obfuscator</h1>
</div>
<h2 id="synopsis">Synopsis</h2>
<p>An alternative method for obfuscating your email address from robots.</p>
<h2 id="motivation-copy-paste">Motivation: copy + paste</h2>
<p>In contrast to the typical <em>[my first name] at blah blah blah [dot] net</em> strategy, or posting your email address as a small image instead of text, this offers the advantage of being (copy + paste)-able.</p>
<h2 id="the-method">The method</h2>
<p>Upon user action (say, clicking a button), construct your email address as text from a semi-obfuscated mess which looks nothing at all like an email address. This prevents simple robots that do not understand javascript from grabbing your email, and even robots that do understand js would have to actively explore the document, running various functions. This seems unlikely, but who knows…</p>
<h2 id="how-can-i-use-it">How can I use it?</h2>
<p>Just enter an email address in the box below, hit the button, and a script will be generated (just for you!). Then copy and paste the script and the html form into your own page.<a href="#fn1" class="footnoteRef" id="fnref1"><sup>1</sup></a> Here’s an <a href="http://www.binaryskeith.com/">example of what it will look like</a>.</p>
<form>
Enter an email address: <br /> <input type="text" id="textemail" size="40" /> <br /> <input type="button" onclick="genScript()" value="Generate Script" /> <br />
<textarea id="scriptOutput" cols="68" rows="25"></textarea>
<br />
</form>


<div class="footnotes">
<hr />
<ol>
<li id="fn1"><p>Note that the output contains a complete-ish html document, so watch out not to copy unneeded tags.<a href="#fnref1">↩</a></p></li>
</ol>
</div>
</body>
</html>
```

[end]