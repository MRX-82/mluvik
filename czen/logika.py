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


def added_word(my_word, new_word, user_id):
    """
    This function for save new words in database
    """
    user_cl = User.objects.get(id=user_id)
    words = Mluvi()
    #words.my_word()
    words.my_word = my_word
    words.new_word = new_word
    words.user = user_cl
    #words = Mluvi.objects.create(my_word = my_word, new_word = new_word)
    words.save()