from django.contrib import admin
from .models import LikePost, profile, post, FollowersCount

# Register your models here.
admin.site.register(profile)
admin.site.register(post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
