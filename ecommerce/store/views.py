from django.shortcuts import render , redirect
from django.contrib import messages
from .models import*
def home(request):
 return render(request,"store/index.html")

def collections(request):
    categories = category.objects.filter(status=0)
    context = {'category':categories}
    return render(request,"store/collections.html",context)

def collectionsview(request, slug):
      if (category.objects.filter(slug = slug, status = 0)):
          products = Product.objects.filter(category__slug = slug )
          category_name = category.objects.filter(slug=slug).first
          context = {'products':products,'category_name':category_name}
          return render(request, "store/products/index.html",context)
      else:
           messages.warning(request, "No such category found")
           return redirect('collections')
def productview(request,cate_slug,pro_slug):
       if (category.objects.filter(slug = cate_slug, status = 0)):
          if (Product.objects.filter(slug = pro_slug, status = 0)): 
                products = Product.objects.filter(slug = pro_slug ).first
                context = {'products':products}
               
          else: 
                messages.warning(request, "No such Products found")
                return redirect('collections')
       else: 
            messages.warning(request, "No such category found")
            return redirect('collections')
       return render(request , 'store/products/view.html',context)