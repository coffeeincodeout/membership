from django.http import Http404

from .models import Members
from rest_framework import viewsets, status
from .serializers import MembersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests

class MembersListView(APIView):
    """
    list all members accounts in the database
    """
    def get(self, request, format=None):
        members = Members.objects.all()
        serializer_class = MembersSerializer(members, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer_class = MembersSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.errors, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class MembersDetailView(APIView):
    """
    Retrieve, update or delete a members account
    """

    def get_object(self, pk):
        try:
            return Members.objects.get(pk=pk)
        except Members.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        if len(Members.objects.all()) == 0:
            api_request = requests.get('https://randomuser.me/api/?results=10&nat=us')
            if api_request.status_code == 200:
                accounts = api_request.json()
                for account in accounts['results']:
                    member_account = Members.objects.create(data=account)
        items = self.get_object(pk)
        serializer_class = MembersSerializer(items)
        return Response(serializer_class.data)

    def put(self, request, pk, format=None):
        members = self.get_object(pk)
        serializer_class = MembersSerializer(members, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
