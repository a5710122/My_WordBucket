from django.shortcuts import redirect, render
from wordbucket.models import Item




def home_page(request):
    if request.method == 'POST':
        Item.objects.create(word=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def search_word(request):
    """ Search word at User want to find """

    word_to_find = None #defind value protect Unbound error
    items2 = None #defind value protect Unbound error

    if request.method == 'POST': #if have event request they call 'POST'
        word_to_find = request.POST.get('word_find', None) #take value from template
            
    items = Item.objects.all() #return obkect type Manager 
                               #(Manager for start creat Database operation 
    
    for i in range(len(items)): #loop find word we want
        if (word_to_find == items[i]): #compare value input with word in database
            items2 = items[i].word 
     
    context = { #variable type 'dictionary' 
       
        'items2' : word_to_find #key is name variable we declare in template
    }
    return render(request, 'search.html', context) #call function 'render' for generate HTML to Client
    
