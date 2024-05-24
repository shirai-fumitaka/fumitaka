from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    share_id = models.IntegerField(default=1)
    good_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)+'('+str(self.owner)+')'
    def get_share(self):
        return Message.object.get(id=self.share_id)
    class Meta:
        ordering = ('-pub_date',)

class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return '<'+self.title+'('+str(self.owner)+')>'

class Friend(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.owner)+'(group:"'+str(self.group)+'")' 
    
class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return "good" + ':' + str(self.owner) + ':' + str(self.message)


# Create your models here.
