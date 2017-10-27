from django.conf.urls import url
from assistant import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required
app_name = 'assistant'

urlpatterns = [
    
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^home',views.HomeView.as_view(),name='home'),
    url(r'^post/new/$',views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.Post_publish, name='post_publish'),
    url(r"^login/$", auth_views.LoginView.as_view(template_name="assistant/login.html"),name='login'),
    url(r"^logout/$", login_required(auth_views.LogoutView.as_view()), name="logout"),
    url(r"^signup/$", views.SignUp.as_view(), name="signup"),
    url(r"^contact/$", permission_required('assistant.view_contact',raise_exception=True)(views.ContactListView.as_view()), name="contact"),
    url(r"^description/$", login_required(views.DescriptionListView.as_view()), name="description"),
    url(r'^healthstatus/(?P<pk>\d+)$',login_required(views.HealthDetailView.as_view()),name='healthstatus'),
    url(r'^healthlist/$',permission_required('assistant.create_review')(views.HealthListView.as_view()),name="health_list"),
    url(r'^healthstatus/(?P<pk>\d+)/comment/$', permission_required('assistant.create_review')(views.add_comment_to_post), name='add_comment_to_post'),
    url(r'^healthstatus/(?P<pk>\d+)/approve/$', permission_required('assistant.create_review')(views.comment_approve), name='comment_approve'),
    url(r'^healthstatus/(?P<pk>\d+)/remove/$', permission_required('assistant.create_review')(views.comment_remove), name='comment_remove'),
]