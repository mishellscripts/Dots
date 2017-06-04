import nltk


def get_words(posts):
    # list containing all words from all posts
    all_words = []
    # append words to list
    for post in posts:
        for word in nltk.word_tokenize(post.text):
            all_words.append(word.lower())
    all_words = nltk.FreqDist(all_words)
    return all_words

def find_features(post, features):
    set_words = set(nltk.word_tokenize(post.text))
    post_features = {}
    for feature in features:
        post_features[feature] = {feature in set_words}
    return post_features
