from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse('Hello world!')

def mytemplate(request):
	t = get_template('template1.html')
	html = t.render(Context({'myname': 'Saji'}))
	return HttpResponse(html)

