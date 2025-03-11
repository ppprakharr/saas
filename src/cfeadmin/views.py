from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def pw_protected_view(request):
    CORRECTED_PWD = 'test'
    is_auth = request.session['code'] or 0

    if request.method=='POST':
        password = request.POST.get("code")
        if password==CORRECTED_PWD:
            is_auth=1
            request.session['code']=is_auth
    if is_auth:
        return render(request, 'protected/view.html')
    return render(request,'protected/entry.html')