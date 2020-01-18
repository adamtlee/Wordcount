from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'message':'Welcome to the home page'})

def count(request):
    fulltext = request.GET['fulltext']

    wordcount = fulltext.split()

    worddictionary = {}
    for word in wordcount:
        if word in worddictionary:
            #Increase the word count
            worddictionary[word] += 1
        else: 
            #Add to the dictionary
            worddictionary[word] = 1

    sortedWordCount = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    # worddictionary':worddictionary - 'worddictionary':worddictionary.items()
    return render(request, 'count.html', {'inputtext':fulltext, 'counter':len(wordcount), 'sortedWordCount': sortedWordCount })
    print(fulltext)

def about(request):
    return render(request, 'about.html')