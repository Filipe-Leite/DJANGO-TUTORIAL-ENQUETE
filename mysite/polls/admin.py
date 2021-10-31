from django.contrib import admin
from django.utils.translation import ugettext
from .models        import Question

admin.site.register(Question)