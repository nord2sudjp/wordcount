from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  return render(request, 'home.html')

def count(request):
  fulltext = request.GET['fulltext']
  print(fulltext)

  wordlist = fulltext.split()

  wordlistdic = {}
  for word in wordlist:
    if word in wordlistdic:
      wordlistdic[word] += wordlistdic[word] 
    else:
      wordlistdic[word] = 1

  s_wordlistdic = sorted(wordlistdic.items(), key=lambda x:x[1], reverse=True)
  return render(request, 'count.html', {'fulltext':fulltext, 'wordcount': len(wordlist), 'wordlistdic': s_wordlistdic})
