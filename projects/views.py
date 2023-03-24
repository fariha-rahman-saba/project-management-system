from django.shortcuts import render
from .models import Project
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView)
from .forms import ProjectForm

def home(request):
    return render(request,'projects/home.html')


def about(request):
    return render(request, 'projects/about.html')


class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetail, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        Liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            Liked = True

        context["total_likes"] = total_likes
        context["liked"] = Liked
        return context


class AddProject(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/add_project.html'


class Delete(DeleteView):
    model = Project
    template_name = 'delete_project.html'
    success_url = reverse_lazy('home')


def LikeView(request, pk):
    Project = get_object_or_404(Project, id=request.POST.get('project_id'))
    liked = False
    if Project.likes.filter(id=request.user.id).exists():
        Project.likes.remove(request.user)
        liked = False
    else:
        project.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
