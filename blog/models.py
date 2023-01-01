from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    statuschoices=(
        ("Private","Private"),
        ("Publique","Publique"),
    )
    publication_date = models.DateTimeField(("Date de publication"),default=timezone.now)
    title = models.CharField(("Titre"), max_length=50)
    articles = models.TextField(("Article"))
    author=models.ForeignKey(settings.AUTH_USER_MODEL, 
            verbose_name=("Auteur"), on_delete=models.CASCADE)
    status = models.CharField(choices=statuschoices,default="Publique", max_length=8)


 
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-publication_date"]
 
    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
 
