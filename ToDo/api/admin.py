from django.contrib import admin
from api.models import Task,User,UserManager

admin.site.register(Task)
admin.site.register(User)
# admin.site.register(UserManager)