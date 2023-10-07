def compare_words(target_word, entered_word):
    green_check = [0] * len(target_word)
    res = {}

    for key in target_word:
        res[key] = res.get(key, 0) + 1

    for element in range(len(target_word)):
        if target_word[element] == entered_word[element]:
            res[entered_word[element]] -= 1

    return green_check, res
