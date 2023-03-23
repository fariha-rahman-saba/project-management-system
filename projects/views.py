from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

def home(request):
    return render(request,'projects/home.html')


class HomeView(ListView):
    # model = Post
    template_name = 'projects/home.html'
    # ordering = ['-id']
    # ordering = ['-post_date']

    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context
