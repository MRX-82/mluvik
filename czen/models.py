from django.db import models

class User(models.Model):
    """
    This is model for users
    """
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    my_language = models.CharField(max_length=20)
    new_language = models.CharField(max_length=20)


class Mluvi(models.Model):
    """
    This is model for language
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_word = models.CharField(max_length=25)
    new_word = models.CharField(max_length=25)

