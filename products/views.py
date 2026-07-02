from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet
from .permissions import IsVendorOwner
from .serializers import ProductSerializer
from rest_framework.parsers import (
    JSONParser,
    MultiPartParser,
    FormParser,
)
from drf_spectacular.utils import extend_schema


def home(request):
    products = Product.objects.filter(stock__gt=0)

    return render(
        request,
        'home.html',
        {'products': products}
    )

def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    return render(
        request,
        'product_detail.html',
        {'product': product}
    )

@login_required
def add_product(request):

    if request.method == 'POST':

        form = ProductForm(request.POST)

        if form.is_valid():

            product = form.save(commit=False)

            product.vendor = request.user.vendor_profile

            product.save()

            messages.success(
                request,
                "Product added successfully."
            )

            return redirect('dashboard')

    else:
        form = ProductForm()

    return render(
        request,
        'add_product.html',
        {'form': form}
    )

@login_required
def edit_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        vendor=request.user.vendor_profile
    )

    if request.method == 'POST':

        form = ProductForm(
            request.POST,
            instance=product
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Product updated successfully."
            )

            return redirect(
                'product_detail',
                product_id=product.id
            )

    else:

        form = ProductForm(
            instance=product
        )

    return render(
        request,
        'edit_product.html',
        {
            'form': form,
            'product': product
        }
    )

@login_required
def delete_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        vendor=request.user.vendor_profile
    )

    if request.method == 'POST':

        product.delete()

        messages.success(
            request,
            "Product deleted successfully."
        )
        return redirect('home')
            

    return render(
        request,
        'delete_product.html',
        {
            'product': product
        }
    )
'''
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def product_api(request):

    if request.method == 'GET':

        products = Product.objects.all()

        serializer = ProductSerializer(
            products,
            many=True
        )

        return Response(serializer.data)

    elif request.method == 'POST':

        if not request.user.is_authenticated:

            return Response(
                {
                    'error': 'Authentication required.'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not hasattr(request.user, 'vendor_profile'):

            return Response(
                {
                    'error': 'Vendor profile not found.'
                },
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = ProductSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save(vendor = request.user.vendor_profile)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
def product_detail_api(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    serializer = ProductSerializer(
        product
    )

    return Response(
        serializer.data
    )


@api_view(['PATCH'])
def update_product_api(request, pk):

    if not request.user.is_authenticated:

        return Response(
            {
                'error': 'Authentication required.'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    if not hasattr(request.user, 'vendor_profile'):

        return Response(
            {
                'error': 'Vendor profile not found.'
            },
            status=status.HTTP_403_FORBIDDEN
        )

    product = get_object_or_404(
        Product,
        pk=pk,
        vendor=request.user.vendor_profile
    )

    serializer = ProductSerializer(
        product,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['DELETE'])
def delete_product_api(request, pk):

    if not request.user.is_authenticated:

        return Response(
            {
                'error': 'Authentication required.'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    if not hasattr(request.user, 'vendor_profile'):

        return Response(
            {
                'error': 'Vendor profile not found.'
            },
            status=status.HTTP_403_FORBIDDEN
        )

    product = get_object_or_404(
        Product,
        pk=pk,
        vendor=request.user.vendor_profile
    )

    product.delete()

    return Response(
        status=status.HTTP_204_NO_CONTENT
    )

'''
class ProductListCreateAPIView(ListCreateAPIView):

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(
            vendor=self.request.user.vendor_profile
        )

    def perform_create(self, serializer):
        serializer.save(
            vendor=self.request.user.vendor_profile
        )   

    filter_backends = [
        SearchFilter,OrderingFilter,
    ]

    search_fields = [
        'name',
        'description',
    ]  
    ordering_fields = [
        'price',
        'created_at',
        'stock',
        'name',
    ]

    ordering = [
        '-created_at'
    ]
   

class ProductDetailAPIView(
    RetrieveUpdateDestroyAPIView
):

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(
            vendor=self.request.user.vendor_profile
        )     


class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer

    permission_classes = [
        IsAuthenticated,IsVendorOwner
    ]

    parser_classes = (
        MultiPartParser,
        FormParser,JSONParser,
    )

    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        'name',
        'description',
    ]

    ordering_fields = [
        'price',
        'created_at',
        'stock',
        'name',
    ]

    ordering = [
        '-created_at'
    ]

    def get_queryset(self):
        return Product.objects.filter(
            vendor=self.request.user.vendor_profile
        )

    def perform_create(self, serializer):
        serializer.save(
            vendor=self.request.user.vendor_profile
        )   

    @extend_schema(
    summary="List Products",
    description="Returns all products belonging to the authenticated vendor."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)       
    
    @extend_schema(
        summary="Create Product",
        description="Creates a new product for the currently authenticated vendor."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)    