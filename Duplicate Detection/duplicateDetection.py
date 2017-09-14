from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn import cross_validation
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import matplotlib.pyplot as plt
import numpy as np
import math
import glob
import os

#Returns Jaccard's coefficient
def jaccard_similarity(document1, document2):
    intersection = set(document1).intersection(set(document2))
    union = set(document1).union(set(document2))
    return float(len(intersection))/len(union)

#Returns Dice's coefficient
def dice_similarity(document1, document2):
    """dice coefficient 2nt/na + nb."""
    document1_bigrams = set(document1)
    document2_bigrams = set(document2)
    overlap = len(document1_bigrams & document2_bigrams)
    return overlap * 2.0/(len(document1_bigrams) + len(document2_bigrams))

#Returns EJ coefficient
def extended_jaccard_similarity(document1, document2):
    """extended jaccard similarity = (a.b) / (|a2| + |b2| - a.b)"""
    values = range(len(document1))
    #product sum over all values
    dotProduct = sum([document1[i]*document2[i] for i in values])
    #Sum the squares
    square_sum1 = sum([pow(document1[i],2) for i in values])
    square_sum2 = sum([pow(document2[i],2) for i in values])
    return dotProduct / (square_sum1 + square_sum2 - dotProduct)

lemmatizer = WordNetLemmatizer()
vectorizer = TfidfVectorizer(min_df=1)
#Document corpus
corpus = []

#Iterate thorugh all the folders(1,2,3 ...)
for i in range(1,60):   
    path = r'../preprocessed/'+str(i)+'/*'
    files = glob.glob(path)
    for currentfile in files:
        filehandle=open(currentfile,"r")
        content = filehandle.read()
        #Append all the documents to form the corpus
        corpus.append(content)
        filehandle.close()

#Features are selected on the basis of top 600 idf values from the corpus
X = vectorizer.fit_transform(corpus)
indices = np.argsort(vectorizer.idf_)[::-1]
features = vectorizer.get_feature_names()
top_n = 600 #top k features
top_features = [features[i] for i in indices[:top_n]]

#featureDocuments[0] contain the documents, featureDocuments[1] conatin the original folder under which the document was there(Class label)
featureDocuments = [[]]
featureDocuments.append([])
featureDocuments.append([])

#Iterate thorugh all the folders(1,2,3 ...)
for i in range(1,60):
    path = r'../preprocessed/'+str(i)+'/*'
    os.mkdir("../generateddocs/"+str(i))
    files = glob.glob(path)
    counter = 0
    #Iterate through each file
    for currentfile in files:
        filehandle = open(currentfile,"r")
        filecontent = filehandle.read()
        newfilecontent = ""
        isFeatureFile = False
        counter = counter+1
        #If w is a selected feature, append
        for w in top_features:
            if w in filecontent:
                newfilecontent = newfilecontent + w + " "
            #Get all the synonyms of w    
            syns = wn.synsets(w)
            # List of all the derivatives of w
            checklist = []
            # All possible derived words from w
            allderivedwords = []
            for s in syns:
                for l in s.lemmas():
                    allderivedwords.append(l.name())
            checklist = set(allderivedwords)
            for derivedwords in checklist:
                # If derived word is in feature subset, append w
                if derivedwords in filecontent and derivedwords is not w:
                    newfilecontent = newfilecontent + w + " "
                # If lemma of derived word is in feature subset, append w    
                if lemmatizer.lemmatize(derivedwords) in filecontent and lemmatizer.lemmatize(derivedwords) is not w:
                    newfilecontent = newfilecontent + w + " "               
            if newfilecontent:
                newfile = open("../generateddocs/"+str(i)+"/"+str(counter),'w+')
                newfile.write(newfilecontent)
                newfile.close()
                isFeatureFile = True
    
        if isFeatureFile: 
            featureFile = open("../generateddocs/"+str(i)+"/"+str(counter),'r')
            featureFileContent = featureFile.read()
            featureDocuments[0].append(featureFileContent)
            featureDocuments[1].append(i)
            featureFile.close()

        filehandle.close()      

#All Matrices below are 2-D matrices where element at [i][j] represents the similarity measure of ith and the jth document
#Cosine Similarity Matrix
tfIdfMatrix = vectorizer.fit_transform(featureDocuments[0])
cosineSimilarityMatrix  = (tfIdfMatrix * tfIdfMatrix.T).A

euclmatrix = euclidean_distances(tfIdfMatrix)

jaccardmatrix = [[]]
i = 0
for doc1 in featureDocuments[0]:
    jaccardmatrix.append([])    
    for doc2 in featureDocuments[0]:
        jaccardmatrix[i].append(jaccard_similarity(doc1,doc2))      
    i = i+1     

dicematrix=[[]]
i = 0
for doc1 in featureDocuments[0]:
    dicematrix.append([])   
    for doc2 in featureDocuments[0]:
        dicematrix[i].append(dice_similarity(doc1,doc2))        
    i = i+1 

noOfFeatureDocs = i 

#Target Matrix[i][j] is 1 if documents are similar (Or had the same parent folder) 
targetmatrix=[[]]
i = 0
for doc1 in featureDocuments[0]:
    targetmatrix.append([]) 
    for doc2 in featureDocuments[0]:
        if featureDocuments[1][featureDocuments[0].index(doc1)] == featureDocuments[1][featureDocuments[0].index(doc2)] :
            targetmatrix[i].append(1)
        else:
            targetmatrix[i].append(0)       
    i = i+1     

#Now assume all the above similarity measures are attributes of a record and the label of these records is the targetmatrix
dataMatrix = []
targetColumnMatrix = []
i = 0 
row = 0
for i in range(0, noOfFeatureDocs):
    for j in range(i, noOfFeatureDocs):
        dataMatrix.append([])
        dataMatrix[row].append(cosineSimilarityMatrix[i][j])
        dataMatrix[row].append(jaccardmatrix[i][j])
        dataMatrix[row].append(dicematrix[i][j])
        dataMatrix[row].append(euclmatrix[i][j])
        targetColumnMatrix.append(targetmatrix[i][j])
        row = row + 1

#Split into test and train
X_train, X_test, y_train, y_test = cross_validation.train_test_split(dataMatrix, targetColumnMatrix, test_size = 0.1, random_state = 0)

clf = svm.SVC()
clf.fit(X_train, y_train) 

predicted = clf.predict(X_test)

#get accuracy 
accuracyScore = accuracy_score(y_test, predicted)
print "Accuracy Score - " + str(accuracyScore)
