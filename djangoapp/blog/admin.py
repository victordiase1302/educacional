# from django.contrib import admin
# from blog.models import Posts
# from django_summernote.admin import SummernoteModelAdmin
# from django.conf import settings


# @admin.register(Posts)
# class PostsAdmin(SummernoteModelAdmin):
#     print(settings.DOMAIN)
#     list_display = 'id', 'title', 'order', 'is_active'
#     summernote_fields = 'post',
#     list_display_links = 'id', 'title'
#     search_fields = 'id', 'title'
#     # inlines = CardTargetPlatformInline,
#     readonly_fields = 'link_direto','created_at', 'updated_at'

#     def link_direto(self, obj):
#         return f"{settings.DOMAIN}/{obj.slug}"
#     link_direto.short_description = 'Link Direto'
