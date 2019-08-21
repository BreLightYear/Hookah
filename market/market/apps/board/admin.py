from django.contrib import admin

from market.apps.board.models import Post

# Register the Post model to make it visible in the Django Admin page, and dictate
# the way in which it appears.
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'descricao')


admin.site.register(Post, PostAdmin)
