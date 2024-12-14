from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Dashboard
from django.contrib.auth import login,logout,authenticate
from .forms import *
# from django.http import HttpResponse


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                login(request, user)
                return redirect ('home')
        context={
            'form':form,
        }
        return render(request,'quizbase/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'quizbase/login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')
    
def homePage(request):
    context={}
    return render(request,'quizbase/home.html',context)

@login_required(login_url='login')
def start_game(request):
    if "game_data" not in request.session:
        # Initialize session with 10 random question IDs
        question_ids = list(Question.objects.values_list('id', flat=True).order_by("?")[:3])
        request.session["game_data"] = {
            "question_ids": question_ids,
            "current_index": 0,
            "score": 0,
        }

    game_data = request.session["game_data"]
    question_ids = game_data["question_ids"]
    current_index = game_data["current_index"]

    

    # Fetch current question
    try:
        question = Question.objects.get(id=question_ids[current_index])
    except Question.DoesNotExist:
        # Handle case if question doesn't exist
        del request.session["game_data"]
        return render('game')

    # Handling user answer submission
    if request.method == "POST":
        selected_answer = request.POST.get("selected_answer")
        is_correct = selected_answer == question.correct_answer

        # Update score
        if is_correct:
            game_data["score"] += 10

        # Move to next question
        game_data["current_index"] += 1
        request.session["game_data"] = game_data

       


        # If last question, show final result
        if game_data["current_index"] >= len(question_ids):
            user_game, _ = Dashboard.objects.get_or_create(user=request.user)
            user_game.points += game_data["score"]
            user_game.plays += 1
            user_game.save()
            final_score=game_data["score"]
            # Clear session data and show final score
            del request.session["game_data"]
            context={'final_score':final_score}

            
            return render(request,'quizbase/result.html',context)
    
        return render(request, "quizbase/answer_feedback.html", {
                "is_correct": is_correct,
                "correct_answer": question.correct_answer,
                "selected_answer": selected_answer,
                "next_question_index": current_index + 1,
                "total_questions": len(question_ids),
            })

        

    # Fetch choices for the current question
    choices = question.jumbled_choices()

    context = {
        "question": question,
        "choices": choices,
        "current_index": current_index + 1,  # User-friendly index
        "total_questions": len(question_ids),
    }

    return render(request, "quizbase/game.html", context)

@login_required
def dashboard(request):
    user_game,_=Dashboard.objects.get_or_create(user=request.user)
    plays=user_game.plays
    points=user_game.points
    context={"plays":plays,"points":points}
    return render(request, "quizbase/dashboard.html",context)

@login_required
def exit_game(request):
    return redirect('dashboard')


 
