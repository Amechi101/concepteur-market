from __future__ import unicode_literals

from django.http import Http404, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView

from django.contrib import auth, messages
from django.contrib.sites.models import get_current_site
from django.shortcuts import render

from products.forms import ProductForm, ProductCategoryForm

from products.models import Product, ProductCategory

class ProductListView(ListView):
	template_name="banner_base.html"
	model = Product
	context_object_name = "product_list"




# class ProductCategoryView(FormView):

# 	form_class = ProductCategoryForm
# 	template_var={}
	

# 	def __init__(self, *arg):
# 		super(ProductCategory, self).__init__()
# 		self.arg = arg