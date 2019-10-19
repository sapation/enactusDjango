from django.contrib import admin
from .models import Post,ImageUpload


class postAdmin(admin.ModelAdmin):
    list_display =["title","slug", "draft","published"]
    list_filter = ["timestamp"]
    search_fields = ["title","content"]
    #prepopulated_fields = {"slug": ("title",)}
    #exclude= ['slug']
    class meta:
        model = Post

class imageAdmin(admin.ModelAdmin):
    list_display =["title","image","timestamp"]
    list_filter = ["timestamp"]        


admin.site.site_header = 'Enactus Site Dashboard'
admin.site.register(Post,postAdmin)
admin.site.register(ImageUpload,imageAdmin)

