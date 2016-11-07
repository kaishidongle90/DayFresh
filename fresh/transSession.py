from django.shortcuts import *
def transSession(fn):
    def func(request,*args):
        username = request.session.get('username','')
        dic = {
            "username":username,        
            }
        return fn(request,dic,*args)
    return func


def longin_test(fn):
	def func(request):
		if request.session.has_key('username'):
			return fn(request)
		else:
			return redirect('/login/')
	return func

