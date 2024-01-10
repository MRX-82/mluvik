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


def word_learning(user_id):
    """
    This function load word for learning
    """
    word_lern = []
    words_all = Mluvi.objects.all()
    for word in words_all:
        word_lern.append((word.new_word, word.my_word, word.status_word))
    word_lern_full_sort = sorted(word_lern, key=lambda x: x[2])
    return word_lern_full_sort


