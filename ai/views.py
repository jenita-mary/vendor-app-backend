from django.conf import settings

from google import genai

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema
from rest_framework import serializers


client = genai.Client(api_key=settings.GEMINI_API_KEY)

class GenerateDescriptionRequestSerializer(serializers.Serializer):
    name = serializers.CharField()


class GenerateDescriptionResponseSerializer(serializers.Serializer):
    description = serializers.CharField()

@extend_schema(
    request=GenerateDescriptionRequestSerializer,
    responses={200: GenerateDescriptionResponseSerializer},
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def generate_description(request):

    product_name = request.data.get("name", "").strip()

    if not product_name:
        return Response(
            {"error": "Product name is required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    prompt = f"""
    Write a professional e-commerce product description.

    Product Name:
    {product_name}

    Requirements:
    - Around 60-100 words
    - Professional tone
    - Mention quality and benefits
    - Don't exaggerate
    """

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return Response({
            "description": response.text
        })

    except Exception as e:

        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )