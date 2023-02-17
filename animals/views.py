from django.shortcuts import render, get_object_or_404

from comment.forms import CommentForm
from comment.models import Comment
from animals.models import Animal

def animal_list_view (request):
    animal = Animal.objects.all()
    context = {"animals_list": animal, 'page':'animals'}
    return render(request, "animals/animals_list.html", context)

def animal_id_view(request, pk):
    pk = get_object_or_404(Animal, pk=pk)
    comments = Comment.objects.filter(animal = pk, published=True)
    if request.method=="POST": #если метод запроса POST
        form = CommentForm(request.POST)
        if form.is_valid(): #если форма заполнена корректно
            comment =  form.save(commit=False) #получаем объект комментария без сохранения
            comment.animal = pk #записываем к какому посту относится данный комментарий
            comment.save() #комментарий сохраняется
            form = CommentForm() #создаём новую форму
    else:
        form = CommentForm()

    context = {"pk": pk,'page':'animals', 'comments_list':comments, 'form':form}
    return render(request, "animals/animals_id.html", context)
