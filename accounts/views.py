from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def login_view(request):


    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.groups.filter(
                name='Operator'
            ).exists():

                return redirect(
                    '/tickets/operator-dashboard/'
                )

            elif user.groups.filter(
                name='Mechanic'
            ).exists():

                return redirect(
                    '/tickets/maintenance-dashboard/'
                )

            elif user.groups.filter(
                name='Purchasing'
            ).exists():

                return redirect(
                    '/tickets/purchasing-dashboard/'
                )

            elif user.is_superuser:

                return redirect('/tickets/')

            else:

                return redirect('/tickets/')

    return render(
        request,
        'accounts/login.html'
    )


def logout_view(request):


        logout(request)

        return redirect('/login/')

