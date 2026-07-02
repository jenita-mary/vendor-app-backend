from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from products.models import Product
from vendors.models import Vendor
from .forms import VendorRegistrationForm
from django.core.paginator import Paginator
 


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)

            return redirect('dashboard')

    return render(
        request,
        'login.html'
    )


@login_required
def dashboard(request):

    if not hasattr(request.user, 'vendor_profile'):
        return render(
            request,
            'dashboard.html',
            {
                'products': [],
                'error': 'Vendor profile not found'
            }
        )

    vendor = request.user.vendor_profile

    products = Product.objects.filter(
        vendor=vendor).order_by('-created_at')
    paginator = Paginator(
                    products,
                    5
                )
    query = request.GET.get('q')

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if query:
        products = products.filter(
            name__icontains=query
        )

    context = {
        'products': products,
        'query': query,
        'page_obj': page_obj,
    }

    return render(
        request,
        'dashboard.html',
        context
    )

def register_view(request):

    if request.method == 'POST':

        form = VendorRegistrationForm(
            request.POST
        )

        if form.is_valid():

            user = form.save(
                commit=False
            )

            user.role = 'vendor'

            user.save()
            Vendor.objects.create(
                user=user,
                company_name=form.cleaned_data[
                    'company_name'
                ],
                phone=form.cleaned_data[
                    'phone'
                ],
                address=form.cleaned_data[
                    'address'
                ]
            )


            return redirect('login')

    else:

        form = VendorRegistrationForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )

def logout_view(request):

    logout(request)

    return redirect('login')