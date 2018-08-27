import helper
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def fool_classifier(test_data): ## Please do not change the function defination...
    ## Read the test data file, i.e., 'test_data.txt' from Present Working Directory...
    test_dt = None
    with open(test_data, 'r') as infile:
        test_dt = [line.strip().split(' ') for line in infile]
    
    ## You are supposed to use pre-defined class: 'strategy()' in the file `helper.py` for model training (if any),
    #  and modifications limit checking
    strategy_instance = helper.strategy() 
    parameters = {
        'C': 1,
        'gamma': 'auto',
        'kernel': 'linear',
        'coef0': 0.0,
        'degree': 3
    }
    lines = [' '.join(line) for line in strategy_instance.class0] \
            + [' '.join(line) for line in strategy_instance.class1]
    
    # prepare X(samples), y(targets)
    # bag of words vectorizer
    cv = CountVectorizer()
    cv.fit(lines)
    X_train = cv.transform(lines)
    model = strategy_instance.train_svm(parameters, X_train, np.array([0] * 360 + [1] * 180))
    
    # sort the coefficients from positive to negative
    top_coef_sorted = np.argsort(model.coef_.toarray()[0])[::-1]
    top_features = np.array(cv.get_feature_names())
    ##..................................#
    modified_list = []

    # go through each test record, delete features in the records
    # which correspond to positive coefficient in the trained model
    for record in test_dt:
        record_new = record
        for coef_index in top_coef_sorted: 
            feature = top_features[coef_index]
            record_new = [word for word in record_new if word != feature]

            if len((set(record) - set(record_new)) | \
                   (set(record_new) - set(record))) == 20: # no more modifications
                break

        modified_list.append(record_new)
    
    ## Write out the modified file, i.e., 'modified_data.txt' in Present Working Directory...
    new_file = open("modified_data.txt", "w")

    for i in modified_list:
        new_file.write(' '.join(i))
        new_file.write('\n')
    new_file.close()
    
    ## You can check that the modified text is within the modification limits.
    modified_data='./modified_data.txt'
    assert strategy_instance.check_data(test_data, modified_data)
    return strategy_instance ## NOTE: You are required to return the instance of this class.
