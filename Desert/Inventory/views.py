from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import InventoryItem
from .forms import InventoryItemForm

class InventoryItemCreateView(CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory_item_form.html'
    success_url = reverse_lazy('dashboard')

class InventoryItemUpdateView(UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory_item_form.html'
    success_url = reverse_lazy('dashboard')

class InventoryItemDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventory_item_confirm_delete.html'
    success_url = reverse_lazy('dashboard')
