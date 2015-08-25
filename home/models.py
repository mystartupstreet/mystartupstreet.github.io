from django.db import models

# Create your models here.
class Posts(models.Model):
    post_title = models.CharField(max_length=100)
    post_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('Date Published')

    def __unicode__(self):
        return self.post_title

class Response(models.Model):
    post = models.ForeignKey(Posts)
    post_likes = models.IntegerField(default=0)
    post_comments = models.CharField(max_length=200)

