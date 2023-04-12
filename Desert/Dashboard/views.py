from django.views.generic import TemplateView
from .models import InventoryItem

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_items'] = InventoryItem.objects.count()
        context['low_stock_items'] = InventoryItem.objects.filter(stock_quantity__lte=10)
        context['reorder_items'] = InventoryItem.objects.filter(needs_reorder=True)
        return context
