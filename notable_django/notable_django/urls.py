from django.urls import re_path, include
from django.contrib import admin
from api.resources import NoteResource

note_resource = NoteResource()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include(note_resource.urls)),
]
