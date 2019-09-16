from django.contrib import admin
from user.models import Follow
from blog.models import Question

admin.site.register(Follow)
admin.site.register(Question)
