from .models import User, Mluvi


def verifications(login, password, old_login, old_password):
    """
    This is verifications functions
    """
    if login == old_login and password == old_password:
        word_verifications = str('verification')
        return word_verifications
    else:
        word_verifications = str('not verifications')
        return word_verifications


def added_word(my_word, new_word):
    """
    This function for save new words in database
    """
    words = User.objects.create(my_word = my_word, new_word = new_word)
    words.save()