from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Upload(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title


class LinkShare(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    linkAuthor = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class InternalReport(models.Model):
    titleReports = models.CharField(max_length=50, unique=True)
    slugReports = models.SlugField(max_length=50, unique=True)
    authorReports = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_onReports = models.DateTimeField(auto_now=True)
    contentReports = models.TextField()
    created_onReports = models.DateTimeField(auto_now_add=True)
    statusReports = models.IntegerField(choices=STATUS, default=0)


class Meeting(models.Model):
    titleMeeting = models.CharField(max_length=50, unique=True)
    slugMeeting = models.SlugField(max_length=50, unique=True)
    authorMeeting = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_onMeeting = models.DateTimeField(auto_now=True)
    contentMeeting = models.CharField(max_length=100)
    created_onMeeting = models.DateTimeField()
    statusMeeting = models.IntegerField(choices=STATUS, default=0)
