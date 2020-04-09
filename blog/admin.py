from django.contrib import admin
from .models import Post, Upload, LinkShare, InternalReport, Meeting


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class PostList(admin.ModelAdmin):
    list_display = ('title', 'linkAuthor')
    search_fields = ['link']


class PostUpload(admin.ModelAdmin):
    list_display = ('title', 'upload')


class PostInternalReports(admin.ModelAdmin):
    list_display = ('titleReports', 'slugReports', 'statusReports', 'created_onReports')
    list_filter = ("statusReports",)
    search_fields = ['titleReports', 'contentReports']
    prepopulated_fields = {'slugReports': ('titleReports',)}


class PostMeetings(admin.ModelAdmin):
    list_display = ('titleMeeting', 'slugMeeting', 'statusMeeting', 'created_onMeeting')
    list_filter = ("statusMeeting",)
    search_fields = ['title', 'contentMeeting']
    prepopulated_fields = {'slugMeeting': ('titleMeeting',)}


admin.site.register(Post, PostAdmin)

admin.site.register(Upload, PostUpload)

admin.site.register(LinkShare, PostList)

admin.site.register(InternalReport, PostInternalReports)

admin.site.register(Meeting, PostMeetings)
