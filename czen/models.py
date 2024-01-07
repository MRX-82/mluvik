from django.db import models

class User(models.Model):
    """
    This is model for users
    """
    login = models.CharField(min_length=4, max_length=20)
    password = models.CharField(min_length=4, max_length=20)
    my_language = models.CharField(max_length=20)
    new_language = models.CharField(max_length=20)


class Mluvi(models.Model):
    """
    This is model for language
    """
    user = models.ForeingKey(User, on_delete=models.CASCADE)
    my_word = models.CharField(max_length=25)
    new_word = models.CharField(max_length=25)

