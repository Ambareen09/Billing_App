from django.shortcuts import render, redirect
from django.views import View

# Create your views here.


def index(request):
    return render(request, "adminpanel/index.html")


class InventoryView(View):
    def get(self, request):
        return render(request, "adminpanel/viewinventory.html")
