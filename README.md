# WorldCup Twitter App
A simple python application developed with flask having a search engine and classifier. The search engine uses TF-IDF and cosine similarity, while the classifier uses the Bayes theorem. To deploy the application on localhost, install the following packages in a virtualenv.

<pre>Package         Version
--------------- -------
Click           7.0    
Flask           1.1.1  
itsdangerous    1.1.0  
Jinja2          2.10.3 
joblib          0.14.0 
MarkupSafe      1.1.1  
nltk            3.4.5  
numpy           1.17.4 
pandas          0.25.3 
pip             19.3.1 
python-dateutil 2.8.1  
pytz            2019.3 
scikit-learn    0.22   
scipy           1.3.3  
setuptools      42.0.2 
simplejson      3.17.0 
six             1.13.0 
sklearn         0.0    
Werkzeug        0.16.0 
wheel           0.33.6 </pre>

Now download or clone this repo into the virtualenv and activate it.
use export FLASK_APP = DataMiningServer.py and optionally
use export FLASK_ENV=development to enable debugging.
to run the program, type in "flask run".

Code Snippets

DF calculation:

for term in self.dict:
            <pre>
		self.docF[term] = len(self.post[term])
		index += 1
		self.logObj.progress_track(index, total_term)
            </pre>

TF-IDF calculation:

def Calculate_Inverse_Document_Frequency(self,term):
        #calculate idf for given term
        #idf = log(Number of document / Number of document term appeared)
        if term in self.dict:
            return math.log(self.totalDocument/self.docF[term],2)
        else:
            return 0

Cosine Similarity:

def Calculate_similarity(self,query_vec,doc_vec):

        return dot(query_vec,doc_vec)/(norm(query_vec)*norm(doc_vec))

Naive Bayes Probability calculation:

Class Probabilty: 
 def CalculateClassProbability(self):
        for key in self.ClassF:
            self.ClassF[key] = self.ClassF[key] / self.totalDocument
Term Probabilty:

 for key in self.ClassF:
            currentProb = self.ClassF[key]
            for term in terms:
                #P(y|x1,x2,…..xn ) = P(x1|y)P(x2|y)..P(xn|y) P(y) /(P(x1)P(x2)…..P(xn)
                currentProb = currentProb * (( self.TermClassFrequency[term].get(key,0)+1) /( len(self.ClassTermCount[key]) + len( self.unique_terms)))

Reference:

https://github.com/BhaskarTrivedi/QuerySearch_Recommentation_Classification</br>
https://colorlib.com<br/>
https://github.com/amgadalmain/MovieRec<br/>

Credit

Dataset Kaggle FIFA worldcup tweets : https://www.kaggle.com/rgupta09/world-cup-2018-tweets 
An Introduction to Information Retrieval : Christopher D. Manning, Hinrich Schütze, and Prabhakar Raghavan
