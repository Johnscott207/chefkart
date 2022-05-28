from logging import exception
from multiprocessing import context
from turtle import color
from urllib import request
from django.shortcuts import redirect
from django.views.generic import TemplateView,DetailView,ListView
from .models import  Cart, CartItems, Order, Product,Product_Variant,Order

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all();
        return context

class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        v = Product_Variant.colors;
        cc = Product_Variant.objects.filter(product=self.object).values('color').distinct()
        clr = []
        for i in cc:
            clr.append(v[int(i['color'])-1][1])
        context['colors'] = clr;

        c = Product_Variant.size;
        ce = Product_Variant.objects.filter(product=self.object).values('variant').distinct()
        varr = []
        for i in ce:
            varr.append(c[int(i['variant'])-1][1])
        context['variants'] = varr;

        context['variant'] = Product_Variant.objects.filter(product=self.object).latest;

        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        

        
        if request.GET.get('color') != None:
            context['color'] = int(request.GET.get('color'))
        else:
             context['color'] = 1
        

        if request.GET.get('color') != None:
            context['variant'] = int(request.GET.get('varaint'))
        else:
             context['variant'] = 1

        return self.render_to_response(context)

class  AddCartView(ListView):
    template_name = "cart.html"
    model = Cart


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not request.user.is_authenticated:
            return redirect('account_login')
        context = self.get_context_data()


        try:
            if(not request.GET.get('color')):
                context['products'] = CartItems.objects.filter(user=request.user)
                return self.render_to_response(context)
            cl = Product_Variant.colors
            for i,j in cl:
                if request.GET.get('color') == j:
                    cl=i
            vr = Product_Variant.size
            for i,j in vr:
                if request.GET.get('varaint') == j:
                    vr=i
            prod = Product.objects.filter(id=request.GET.get('id'))[0]
            varr = Product_Variant.objects.filter(product=prod,color=cl,variant=vr)[0]
            item = CartItems.objects.filter(product=prod,variant= varr,user=request.user)
      
            if request.GET.get('buy') == "buy":
                context["buy"] = "true"
                context["product"] = prod
                context["varr"] = varr
                print(varr)
                print(request.GET.get('buy')=="buy")
            else:
            
                cart = Cart.objects.filter(user = request.user)
                if len(cart) < 1:
                    Cart.objects.create(user = request.user)
                    pass


                if len(item) < 1:
                    cart = Cart.objects.filter(user = request.user)[0]
                    CartItems.objects.create(product=prod,variant= varr,user=request.user,cart = cart)
                    item = CartItems.objects.filter(product=prod,variant= varr,user=request.user)[0]
                else:
                    item = item[0]
        except:
            pass
        
        

        # print(CartItems.objects.filter(color=request.GET.get('color')))
        context['products'] = CartItems.objects.filter(user=request.user)
        return self.render_to_response(context)
    

class OrderView(TemplateView):
    template_name = "Order.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
   
        if not request.user.is_authenticated:
            return redirect('account_login')
        

        prod = Product.objects.filter(id=request.GET.get('id'))[0]
        varr = Product_Variant.objects.filter(product=prod,color=request.GET.get('color'),variant=request.GET.get('varaint'))[0]
       

        context["product"] = prod
        context["varr"] = varr
        if(request.GET.get('order')=="order"):
            # return redirect("home:home")
            Order.objects.create(product=prod,variant = varr,user = request.user,address=request.GET.get('address'))
            return redirect("home:myorder")
        # print(request.GET.get('buy')=="buy")
        
        
     
        return self.render_to_response(context)

class MyOrderList(TemplateView):
    template_name = "myorder.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all();
        return context