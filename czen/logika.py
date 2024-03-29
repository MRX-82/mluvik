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
    word_lern_full_sort = word_lern_full_sort[:1]
    return word_lern_full_sort


def word_status(user_id, translate_word):
    """
    This function control word status hight
    """
    all_words = Mluvi.objects.all()
    one_word = all_words.get(user_id=user_id, my_word=translate_word)
    one_word.status_word+=1
    one_word.save()
    user = User.objects.get(id=user_id)
    user.experience+=1
    user.save()


def word_repetition_check(user_id, word):
    """
    This function do it control word repetition check
    """
    all_words = Mluvi.objects.all()
    one_word = all_words.filter(user_id=user_id, my_word=word).exists()
    if one_word:
        return "Ok"
    else:
        return "No"


def word_repetition_status(user_id):
    """
    This function do it examination status of word and delete all words have status more
    then 100.
    """
    all_words = Mluvi.objects.all()
    user_word = all_words.filter(user_id=user_id, status_word__gt=100)
    user_word.delete()




