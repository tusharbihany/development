import os
import nltk
import enchant   
import re
import glob
import shutil
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

#Spell check
spellcheck = enchant.Dict("en_US")
#Initialize a stopword remover
stop = stopwords.words('english')
#Initialize a lemmatizer
lemmatizer = WordNetLemmatizer()

#Iterate through all the folders
for i in range(1,2):
	#Input path	
	path = r'./Sample/'+str(i)+"/"+str(i)
	#Output path, if exists then delete it
	if(os.path.exists("./preprocessed/"+str(i))):
		shutil.rmtree("./preprocessed/"+str(i))
	os.mkdir("./preprocessed/"+str(i))
	files=glob.glob(path)
	k=0
	#Iterate through all files in the current folder
	for file1 in files:
		#Required preprocessed text
		preprocessedcontent = ""
		#Read file
		filehandle=open(file1,"r")
		filecontent = filehandle.read()
		#Normalize to lower case
		filecontent = filecontent.lower()
		#Trimming stray or special characters
		filecontentclean1 = re.sub('[^a-zA-Z\n\.]', ' ', filecontent)
		#Trimming periods
		filecontentclean2 = re.sub(r'[\.]', " ", filecontentclean1)
		#Trimming tabs and newlines
		filecontentclean3 = re.sub('[\t|\n]+',' ',filecontentclean2)
		#Trimming multiple spaces
		filecontentclean4 = re.sub(' +',' ',filecontentclean3)
		#Loop through all the terms and chech for stopwords
		for term in [j for j in filecontentclean4.split() if j not in stop][2:]:
			#Spell check and length > 2
			if spellcheck.check(term) and len(term)>2:
				#Lemmatize a term to root form
				termlemmatized = lemmatizer.lemmatize(term)
				#Stemming
				PorterStemmer().stem(termlemmatized)
				preprocessedcontent = preprocessedcontent + " " + termlemmatized
		k=k+1		
		tempfile = open("/Users/tbihany/Documents/Personal/Preprocesssor/preprocessed/"+str(i)+"/"+str(k),'w')
		tempfile.write(preprocessedcontent)
		tempfile.close()
		filehandle.close()
