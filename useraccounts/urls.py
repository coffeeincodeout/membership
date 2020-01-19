from django.conf.urls import url
from django.urls import path
from .views import MembersDetailView, MembersListView
from rest_framework import routers
from useraccounts import views

urlpatterns = [
    url('listview/$', MembersListView.as_view()),
    url(r'listview/(?P<pk>[0-9]+)/$', MembersDetailView.as_view()),

]

# TODO: Format the post and put method with preset fields that match with whats in key value
# TODO: fix the api root so users can navigate
# TODO: fix number of users in the data based to be cached for 30 days
# TODO: Set pagination for the get request
# TODO: Test the update, post and delete
# TODO: push to aws lambda
#