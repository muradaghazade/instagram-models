from django.db import models
from accounts.models import User

class Post(models.Model):
    description = models.CharField('Description',max_length=300, null=True)
    username = models.CharField('Username',max_length=300, null=True)
    likes = models.IntegerField(null=True, blank=True, default=0)
    image = models.ImageField('Image',upload_to='banners/', null=True, blank=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='posts', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
