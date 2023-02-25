import secrets
from django.shortcuts import render , redirect
from .models import allyuser

# Create your views here.
def index(request):
    if 'isLogin'  in request.session:
        del request.session['isLogin']
        del request.session['email']
    return render(request, 'home.html')

def signup(request):
    length= 10
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    myReferral= ''.join(secrets.choice(alphabet) for i in range(length))
    try: 
        if request.method == 'POST':
            email= request.POST['email']
            password= request.POST['password']
            referral = request.POST['referral']
            if referral != '':
                user= allyuser.objects.get(referral_code= referral)
                referral_update = user.referral_count + 1
                allyuser.objects.filter(referral_code= referral).update(referral_count=referral_update)

            saveuser= allyuser.objects.create(username=email, password=password,referral_code=myReferral, referral_count=0)
            return redirect('/login') 
    except:
        return render(request, 'signup.html', {'status': "Account already exist!!!", 'error': True})
    return render(request, 'signup.html')

def login(request):
    try:
        if request.method == 'POST':
            email= request.POST['email']
            password= request.POST['password']
            user=allyuser.objects.get(username=email)
            if len(user.username) > 0:
                if user.password == password:
                    request.session['email'] = email
                    request.session['isLogin'] = True
                    return redirect('/dashboard')
                else:
                    return render(request, 'login.html', {'status': "Password not match, try agian!!!", 'error': True})
    except:
        return render(request, 'login.html', {'status': "Account not found, you may first register.", 'error': True})
    return render(request, 'login.html')

def dashboard(request):
    email = request.session['email']
    try:
        user=allyuser.objects.get(username=email)
        data={
            'username': user.username,
            'referral_code': user.referral_code,
            'referral_count': user.referral_count
        }
    except:
        pass
    return render(request, 'dashboard.html', data)