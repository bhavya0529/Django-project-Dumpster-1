from django.db import models


from django.cor.urlresolvers import reverse
from django.conf import settings
import misaka

from group.models import Group


from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):

    user = models.ForeignKey(User,related_name='posts')
    created_at = models.dataTimeField(auto_now=True)
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=True)



    def __str__(self):
        return self.message_html


    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})


    class Meta:
        ordering = ['-created_at']
        unique_together =  ['user','message']     
