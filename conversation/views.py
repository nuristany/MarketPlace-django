from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .models import Conversation, ConversationMessage
from . forms import ConversationMessageForm, ConversationMessageForm

# Create your views here.


@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if item.created_by == request.user:
        return redirect('dashboard:dash')
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    if conversations:
        return redirect('conversation:detailMessage', pk=conversations.first().id)
       
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
        
    
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            return redirect('item:detail', pk=item_pk)
        
    else:
            
        form = ConversationMessageForm()
            
        context = {
            'form':form
        }
                
    return render(request, 'conversation/new_message.html', context)

@login_required
def inbox(request):
    
    
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    
    context = {
        'conversations':conversations
    }
    return render(request, 'conversation/inbox.html',context)



def detailMessage(request,pk):
    
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            form.save()
            
            return redirect('conversation:detailMessage', pk=pk)
        
    else:
        form = ConversationMessageForm()
        
        
    context = {
        'conversation':conversation,
        'form':form
    }
    
    
    
    return render(request, 'conversation/detail.html', context)


@login_required(login_url='login_Page')
def deleteMessage(request, id):
    message = get_object_or_404(ConversationMessage, id=id)
 
    if request.method == 'POST':
        message.delete()
        return redirect('conversation:inbox')
        
    return render(request, 'conversation/delete_message.html',{'obj': message})
        
    
def editMessage(request, id):
    message = get_object_or_404(ConversationMessage, id=id)
    form = ConversationMessageForm(instance= message)
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('conversation:inbox')
    context = {
        'form':form,
        
    }
    return render(request, 'conversation/detail.html', context)



   

    
    
            
            
            

            
    