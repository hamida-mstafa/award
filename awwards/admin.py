from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile,Posts
# Register your models here.
admin.site.register(Profile)
admin.site.register(Posts)