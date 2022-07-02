from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Lecture, Quiz


# Register your models here.
class LectureTutorials(AdminVideoMixin, admin.ModelAdmin):
    pass

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Lecture, LectureTutorials)
admin.site.register(Quiz)
