import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.externals import joblib
import time

#usdata = '1k_tweets.txt'
#uslabel = '1k_labels.txt'
# usdata = '5k_tweets.txt'
# uslabel = '5k_labels.txt'
# usdata = '10k_tweets.txt'
# uslabel = '10k_labels.txt'
# usdata = '20k_tweets.txt'
# uslabel = '20k_labels.txt'
# usdata = '30k_tweets.txt'
# uslabel = '30k_labels.txt'
# usdata = '40k_tweets.txt'
# uslabel = '40k_labels.txt'
# usdata = 'tweets_us.json.text'
# uslabel = 'tweets_us.json.labels'

def test(usdata,uslabel):
    a = open(usdata)
    b = open(uslabel)
    c = open(usdata)

    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(a)

    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    target = []
    for line in b.readlines():
        target.append(int(line.strip()))

    start_t = time.time()
    
    # clf = MultinomialNB().fit(X_train_tfidf, target)
    # clf = SGDClassifier().fit(X_train_tfidf, target)
    # clf = svm.SVC().fit(X_train_tfidf, target)
    # clf = LogisticRegression().fit(X_train_tfidf, target)
    # clf = KNeighborsClassifier().fit(X_train_tfidf, target)
    # clf = DecisionTreeClassifier().fit(X_train_tfidf, target)
    clf = MLPClassifier().fit(X_train_tfidf, target)
    
    end_t = time.time()
    trainingtime = end_t - start_t

    test = []
    for line in c.readlines():
        test.append(line.strip())

    print clf
    print usdata
    start_t = time.time()

    for i in range(10):
        start = i*100
        end = start + 100
        print "Range: ", start, end
        docs_test = test[start:end]
        target_test = target[start:end]
        X_new_counts = count_vect.transform(docs_test)
        X_new_tfidf = tfidf_transformer.transform(X_new_counts)
        predicted = clf.predict(X_new_tfidf)
        print "accuracy: ", np.mean(predicted == target_test)
    
    end_t = time.time()
    elapsed = end_t - start_t
    print "training time", trainingtime
    print "elapsed time", elapsed
    # X_new_counts = count_vect.transform(docs_test)
    # X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    # predicted1 = nb_clf.predict(X_new_tfidf)
    # predicted2 = sgd_clf.predict(X_new_tfidf)
    # predicted3 = svm_clf.predict(X_new_tfidf)
    # predicted4 = lr_clf.predict(X_new_tfidf)
    # predicted5 = knn_clf.predict(X_new_tfidf)
    # predicted6 = dt_clf.predict(X_new_tfidf)
    # predicted7 = nn_clf.predict(X_new_tfidf)

    # print "accuracy NB: ", np.mean(predicted1 == target_test)
    # print "accuracy Stochiastic Gradient Descent: ", np.mean(predicted2 == target_test)
    # print "accuracy SVM: ", np.mean(predicted3 == target_test)
    # print "accuracy Logistic Regression: ", np.mean(predicted4 == target_test)
    # print "accuracy Nearest Neighbor: ", np.mean(predicted5 == target_test)
    # print "accuracy Decision Tree: ", np.mean(predicted6 == target_test)
    # print "accuracy Neural Networks: ", np.mean(predicted7 == target_test)

datalabelpairs = [ ('1k_tweets.txt','1k_labels.txt'),('5k_tweets.txt','5k_labels.txt'),('10k_tweets.txt','10k_labels.txt'),('20k_tweets.txt','20k_labels.txt'),('30k_tweets.txt','30k_labels.txt'),('40k_tweets.txt','40k_labels.txt'),('tweets_us.json.text','tweets_us.json.labels')]

def main():
    for set in datalabelpairs:
        print "===============================", set
        test(set[0],set[1])


if __name__ == "__main__":
    main()
