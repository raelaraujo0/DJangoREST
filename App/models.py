from django.db import models

class Books(models.Model):
    name = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    readed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name