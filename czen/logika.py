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
    words.my_word = my_word
    words.new_word = new_word
    words.user = user_cl
    words.save()


def word_learning(user_id):
    """
    This function load word for learning, one session = 20 small status_word word
    """
    word_lern = []
    words_all_first = Mluvi.objects.all()
    words_all = words_all_first.filter(user_id=user_id)
    for word in words_all:
        word_lern.append((word.new_word, word.my_word, word.status_word))
    word_lern_full_sort = sorted(word_lern, key=lambda x: x[2])
    word_lern_full_sort = word_lern_full_sort[:21]
    return word_lern_full_sort


