from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin as LoginRequiredMixin1
from django.contrib.auth.decorators import login_required,permission_required
from .forms import UserCreateForm,PostForm,CommentForm
from django.contrib.auth.models import Group,User
from .models import Post,Contact,Description,HealthStatus,Comment
from django.contrib.auth import authenticate,login,logout
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
# def group_required(*group_names):
#     """Requires user membership in at least one of the groups passed in."""
#     def in_groups(u):
#         if u.is_authenticated():
#             if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
#                 return True
#         #return False
#         raise PermissionDenied
#         #redirect('assistant:home')
#     return user_passes_test(in_groups)
# Create your views here.
class SignUp(CreateView):
    form_class = UserCreateForm

    def get_success_url(self):
        g = Group.objects.get(name='user')
        g.user_set.add(self.object)
        uid = User.objects.latest('id')
        h ,created = HealthStatus.objects.get_or_create(
            patientid = uid,
            defaults = {'status':'new user!'}
        )
        return reverse_lazy("assistant:login")
    #success_url = reverse_lazy("assistant:login")
    template_name = "assistant/signup.html"

class HomeView(TemplateView):
    template_name = 'home.html'



# def class_view_decorator(function_decorator):
#     """Convert a function based decorator into a class based decorator usable
#     on class based Views.

#     Can't subclass the `View` as it breaks inheritance (super in particular),
#     so we monkey-patch instead.
#     """
#     def simple_decorator(View):
#         View.dispatch = method_decorator(function_decorator)(View.dispatch)
#         return View

#     return simple_decorator

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

#@class_view_decorator(permission_required('create_post'))
#@method_decorator(group_required('doctor'),name='dispatch')
class LoginRequiredMixin(object):
    @method_decorator(permission_required('assistant.create_post',raise_exception=True))
    #@method_decorator(group_required('doctor'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'assistant/post_detail.html'

    form_class = PostForm

    model = Post

@login_required
def Post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('assistant:post_detail', pk=pk)

class ContactListView(ListView):
    model = Contact

    def get_queryset(self):
        return Contact.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class DescriptionListView(ListView):
    model = Description

    def get_queryset(self):
        return Description.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class HealthDetailView(DetailView):
    model = HealthStatus

#@permission_required('assistant.create_review')
def add_comment_to_post(request, pk):
    post = get_object_or_404(HealthStatus, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('assistant:healthstatus', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'assistant/progress_form.html', {'form': form})    

class HealthListView(ListView):
    model = HealthStatus

    def get_queryset(self):
        return HealthStatus.objects.order_by('-patientid')


def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('assistant:healthstatus', pk=comment.post.pk)



def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('assistant:healthstatus', pk=post_pk)