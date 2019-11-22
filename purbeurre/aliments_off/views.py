from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, RedirectView

from django.contrib.auth.models import User
from .models import Products, SaveProducts


class SearchView(ListView):
    """Return products from DB from query."""
    template_name = 'aliments_off/search.html'
    paginate_by = 9

    def get_queryset(self):
        return Products.objects.filter(
            product_name__icontains=self.request.GET['query']).\
                order_by('product_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.request.GET['query']
        context['target'] = 'aliments_off:result'
        return context


class ResultView(ListView):
    """Return substitutes with same category and better/equal nutrigrade."""
    template_name = 'aliments_off/result.html'

    def get_queryset(self):
        self.product = Products.objects.get(pk=self.kwargs['product_id'])
        return Products.objects\
            .filter(category_name=self.product.category_name)\
            .filter(nutritional_score__lte=self.product.nutritional_score)\
            .exclude(id=self.kwargs['product_id'])\
            .order_by('nutritional_score')[:9]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'allreadysaved' in self.request.GET:
            context['message'] = 'Déjà enregistré'
        context['query'] = self.product.product_name
        context['product'] = self.product
        context['title'] = self.product
        context['target'] = 'aliments_off:detail'
        return context


class DetailProductView(DetailView):
    """Show product details."""
    template_name = 'aliments_off/detail.html'
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = kwargs['object'].product_name
        return context


@login_required
def SaveView(request):
    """Save product/substitute."""
    if request.method == 'POST':
        # get data from POST
        id_product = request.POST['id_product_sub']
        next_url = request.POST['next']
        # get data from DB
        product_obj = Products.objects.get(pk=id_product)
        user_obj = User.objects.get(pk=request.user.id)
        # test if all obj are sets
        if product_obj and user_obj:
            # create Substitute or return "allreadysaved"
            obj, created = SaveProducts.objects.get_or_create(
                user_id=user_obj,
                id_product=product_obj,
                )
            if created:
                return redirect('aliments_off:myproducts')
            else:
                return redirect(next_url+"?allreadysaved")
    return redirect('homepage')


class MyProductsView(LoginRequiredMixin, ListView):
    """Show saved products."""
    template_name = 'aliments_off/my_products.html'
    paginate_by = 4

    def get_queryset(self):
        return SaveProducts.objects.filter(
            user_id=self.request.user.id).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mes produits'
        context['target'] = 'aliments_off:result'
        return context