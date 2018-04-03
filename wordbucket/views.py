from django.shortcuts import redirect, render
from wordbucket.models import Word, Explanation, Like_and_dislike

def home_page(request):
    d_message = ""
    words = Word.objects.order_by('-date_pub')[:5]
    if request.method == 'POST':
        word_reference = str(request.POST['word_input'])
        # query for duplicate word
        d_query = Word.objects.filter(word=word_reference)
        if not d_query :
            word_ = Word.objects.create(word = request.POST['word_input'])
            Explanation.objects.create(explanation_text=request.POST['explanation_input'], word=word_)
            return redirect('/')
        else :
            # duplacate word id
            dword_id = Word.objects.get(word = word_reference)
            Explanation.objects.create(explanation_text=request.POST['explanation_input'], word=dword_id)
            d_message = "duplicate word, your explanation add to existing word."
            return render(request, 'home.html', {'words': words, 'd_message': d_message})
    return render(request, 'home.html', {'words': words, 'd_message': d_message})

def view_word(request, word_id):
    word_ = Word.objects.get(id=word_id)
    return render(request, 'detail.html', {'word': word_})

def add_word(request):
    pass

def add_explanation(request):
    pass

def vote_like(request):
    pass

def vote_dislike(request):
    pass

def search(request):
    pass
