from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import TextSerializer
import json
from rest_framework.response import Response
from rest_framework import status
from .converter import convert
from rest_framework import renderers


class TextConverter(GenericAPIView):
    serializer_class = TextSerializer
    renderer_classes = [renderers.StaticHTMLRenderer]

    def post(self, request):
        text = json.loads(request.body.decode('utf-8'), strict=False)["text"]
        converted_text = convert(text)
        return Response(converted_text, status=status.HTTP_200_OK)

    def get(self, request):
        return Response("Enter text to receive HTML")
