from django.shortcuts import render,get_object_or_404
from tweet.models import Tweet
from tweet.forms import Tweetform,userRegistarionForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


#Registartion 

def register(request):
    if request.method == "POST":
        form = userRegistarionForm(request.POST)
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.set_password(form.cleaned_data["password1"])
            user_data.save()
            login(request,user_data)
            return redirect("tweet_list")
        pass
    else:
        form = userRegistarionForm()
        
    register_form_dict = {
        "form" : form
    }
    return render(request,"registration/register.html",register_form_dict)

# Create your views here.

def home(request):
    return render(request, 'home.html')


# display a list of tweets

def tweet_list(request):
    
    tweet_data = Tweet.objects.all().order_by("created_at")
    
    tweet_details_dict = {
        "details" : tweet_data
    }
    
    return render(request,"tweet_list.html",tweet_details_dict)


# create a new tweet
@login_required
def create_tweet(request):
    if request.method == "POST":
        form = Tweetform(request.POST , request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = Tweetform()
        
    return render(request,"tweet_form.html",{"form":form})
    
@login_required   
def edit_tweet(request , tweet_id):
    tweet = get_object_or_404(Tweet , id = tweet_id, user = request.user)
    if request.method == "POST":
        form = Tweetform(request.POST , request.FILES , instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = Tweetform(instance = tweet)
        
    return render(request,"tweet_form.html",{"form":form})

@login_required
def delete_tweet(request,tweet_id):
    tweet = get_object_or_404(Tweet,id=tweet_id,user = request.user)
    tweet_text = tweet.text[:150]
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    
    delete_tweet_list = {
        "tweet" : tweet_text
    }
    return render(request,"tweet_delete.html",delete_tweet_list)    