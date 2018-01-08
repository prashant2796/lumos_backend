from django.db import models

# Create your models here.

class Technology(models.Model):
	language_name=models.CharField(max_length=20)

	def __str__(self):
		return self.language_name


class Domain(models.Model):
	domain_name=models.CharField(max_length=20)

	def __str__(self):
		return self.domain_name

class KnowledgeArena(models.Model):
	SKILL_BEGINNER = 'beg'
	SKILL_INTERMEDIATE = 'int'
	SKILL_ADVANCE= 'adv'

	skill_levels = (
	('SKILL_BEGINNER', 'Beginners'),
	('SKILL_INTERMEDIATE', 'Intermediate'),
	('SKILL_ADVANCE', 'Advance')
	)

	title = models.CharField(max_length=30,null=False,blank=False)
	description = models.TextField(null=False,blank=False)
	language= models.ManyToManyField(Technology)
	domain= models.ForeignKey(Domain)
	multi_language= models.BooleanField(default=False)
	skill_level= models.CharField(max_length=20,choices=skill_levels)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title

class Video(KnowledgeArena):
	video_id = models.IntegerField()

class Playlist(KnowledgeArena):
	playlist_id = models.IntegerField()

class Course_link(KnowledgeArena):
	link_url = models.URLField(null=False, blank=False)
	paid = models.BooleanField(default=False)



