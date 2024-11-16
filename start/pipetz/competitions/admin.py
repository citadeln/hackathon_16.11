from django.contrib import admin
from .models import Competitions, Test, Task, Submission
# Register your models here.


admin.site.register(Competitions),
admin.site.register(Test),
admin.site.register(Task),
admin.site.register(Submission),