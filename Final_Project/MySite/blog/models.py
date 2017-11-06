from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title

class Comment(models.Model):
	userid = models.ForeignKey('auth.User', null=True)
	postid = models.ForeignKey('Post', null=True)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return str(self.userid) +  ' ' + str(self.body) + ' ' + str(self.postid) + ' ' + str(self.date)
