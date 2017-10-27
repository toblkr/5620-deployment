from django.contrib import admin
from .models import Post,Contact,Description,HealthStatus,Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Description)
admin.site.register(HealthStatus)
admin.site.register(Comment)