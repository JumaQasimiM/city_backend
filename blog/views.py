from django.shortcuts import render

# Create your views here.
    # muss in der view schreiben.
def perform_create(self, serializer):
    serializer.save(user=self.request.user)
    