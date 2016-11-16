from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from core.models import Region, Customer, Provider


class HomeView(TemplateView):
    template_name = 'core/index.html'


class SearchView(TemplateView):
    template_name = 'core/providers.html'

    def get(self, request):
        customer = get_object_or_404(Customer, name=request.GET.get('name_customer'))
        providers = Provider.objects.filter(regions__in=customer.regions.all())

        return render(request, 'core/providers.html', {
            'customer': customer,
            'providers': providers
        })


class ProviderView(TemplateView):
    template_name = 'core/provider.html'

    def get(self, request, id):

        return render(request, 'core/provider.html', {
            'provider': get_object_or_404(Provider, id=id)
        })
