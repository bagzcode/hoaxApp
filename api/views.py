from django.shortcuts import render
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.metrics import accuracy_score
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class HoaxTest(views.APIView):
    
    def get (self,request):
        formatForm = {
            "text": "[change with your sentence]"
        }
        return Response(formatForm, status=status.HTTP_200_OK)

    
    def post(self, request):
        clf = pickle.load(open("./MLmodel/pac_model.pkl", "rb"))
        tf1 = pickle.load(open("./MLmodel/tfidf1.pkl", "rb"))
        
        text = request.data.pop('text');

        # Create new tfidfVectorizer with old vocabulary
        factory = StopWordRemoverFactory()
        stopwords = factory.get_stop_words()
        tf1_new = TfidfVectorizer(analyzer='word', ngram_range=(1,2), stop_words=frozenset(stopwords), lowercase = True,
                          max_features = 500000, vocabulary = tf1.vocabulary_)
        X_tf1 = tf1_new.fit_transform([text])

        pred = clf.predict(X_tf1)

        return Response(pred,status=status.HTTP_200_OK)