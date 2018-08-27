## import modules here 
from collections import defaultdict

################# Question 1 #################

def multinomial_nb(training_data, sms):# do not change the heading of the function
    pass # **replace** this line with your code
    prior, cond_prob = nb_train(training_data)
    prob_ham = prior['ham']
    prob_spam = prior['spam']
    for word in sms:
        if word in cond_prob['ham']:
            prob_ham *= cond_prob['ham'][word]
        if word in cond_prob['spam']:
            prob_spam *= cond_prob['spam'][word]
    return prob_spam / prob_ham

from collections import defaultdict

def nb_train(training_data):
    ham_dd = defaultdict(int)
    ham_count = 0
    spam_dd = defaultdict(int)
    spam_count = 0
    for row in training_data:
        if row[1] == 'ham':
            ham_count += 1
            for k, v in row[0].items():
                ham_dd[k] += v
                
        else:
            spam_count += 1
            for k, v in row[0].items():
                spam_dd[k] += v
    V = set(list(ham_dd.keys()) + list(spam_dd.keys()))
    total_terms = len(V) 
    N = len(training_data)
    ham_total_words = sum(ham_dd.values())
    spam_total_words = sum(spam_dd.values())
    prior = {}
    cond_prob = {}
    for c in ['ham', 'spam']:
        prior[c] = ham_count / N if c == 'ham' else spam_count / N
        cond_prob[c] = {}
        for word in V:
            if c == 'ham':
                cond_prob[c][word] = (ham_dd[word] + 1) / (ham_total_words + total_terms)
            else:
                cond_prob[c][word] = (spam_dd[word] + 1) / (spam_total_words + total_terms)
    return (prior, cond_prob)