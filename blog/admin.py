from django.contrib import admin
from .models import Post,Comment

# ajoute la ligne de commemtaire au de sus de la publication
# uitlesr TabularInline ou StackeInline
class CommentInline(admin.TabularInline):
    model= Comment
    #nom de commentaire a affiche
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)        
