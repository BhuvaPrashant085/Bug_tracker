from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Issue
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import IssueForm
from django.utils import timezone





@login_required(login_url='login')
def home(request):
    issues = Issue.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'issues': issues})

@login_required(login_url='login')
def filter_search(request):
    issues = Issue.objects.all().order_by('-created_at')
    status_filter = request.GET.get('status')
    priority_filter = request.GET.get('priority')
    search = request.GET.get('search')

    if status_filter and status_filter != 'All':
        issues = issues.filter(status=status_filter)
    if priority_filter and priority_filter != 'All':
        issues = issues.filter(priority=priority_filter)
    if search:
        issues = issues.filter(title__icontains=search)

    return render(request, 'filter_search.html', {'issues': issues})




@login_required(login_url='login')
def dashboard(request):
    issues = Issue.objects.all().order_by('-created_at')

    # Dashboard summary data
    total_issues = Issue.objects.count()
    open_issues = Issue.objects.filter(status='Open').count()
    in_progress_issues = Issue.objects.filter(status='In Progress').count()
    closed_issues = Issue.objects.filter(status='Closed').count()

    # Filters
    status_filter = request.GET.get('status')
    priority_filter = request.GET.get('priority')

    if status_filter and status_filter != 'All':
        issues = issues.filter(status=status_filter)

    if priority_filter and priority_filter != 'All':
        issues = issues.filter(priority=priority_filter)

    context = {
        'issues': issues,
        'total_issues': total_issues,
        'open_issues': open_issues,
        'in_progress_issues': in_progress_issues,
        'closed_issues': closed_issues,
    }

    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def create_issue(request):
    
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.created_by = request.user
            issue.save()
            return redirect('dashboard')
    else:
        form = IssueForm()


    return render(request, 'create_issue.html', {'form': form})



@login_required(login_url='login')
def history(request):
    issues = Issue.objects.all().order_by('-created_at')
    return render(request, 'history.html', {'issues': issues})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials or user does not exist')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists, please login')
            return redirect('login')

        User.objects.create_user(username=username, password=password1)
        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login')

    return render(request, 'signup.html')



def user_logout(request):
    logout(request)
    return redirect('login')




@login_required
def start_issue(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)

    # Check if user already has an issue in progress
    already_working = Issue.objects.filter(
        assigned_to=request.user,
        status='In Progress'
    ).exists()

    if already_working:
        messages.error(
            request,
            "You already have an issue in progress. Please close it first."
        )
        return redirect('dashboard')

    issue.status = 'In Progress'
    issue.assigned_to = request.user
    issue.save()

    messages.success(request, "Issue moved to In Progress")
    return redirect('dashboard')



@login_required
def close_issue(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)

    if issue.assigned_to != request.user:
        messages.error(request, "You are not allowed to close this issue")
        return redirect('dashboard')

    issue.status = 'Closed'
    issue.save()

    messages.success(request, "Issue closed successfully")
    return redirect('dashboard')


def update_issue_status(request, issue_id, new_status):
    issue = get_object_or_404(Issue, id=issue_id)

    if new_status == 'In Progress':
        active_issue = Issue.objects.filter(
            assigned_to=request.user,
            status='In Progress'
        ).exclude(id=issue.id).first()

        if active_issue:
            messages.error(
                request,
                "You already have an issue In Progress. Close it first."
            )
            return redirect('dashboard')

        issue.status = 'In Progress'
        issue.assigned_to = request.user
        issue.started_at = timezone.now()   # ✅ START TIME
        issue.save()

    elif new_status == 'Closed':
        if issue.assigned_to != request.user:
            messages.error(request, "You cannot close this issue.")
            return redirect('dashboard')

        issue.status = 'Closed'
        issue.closed_at = timezone.now()    # ✅ END TIME
        issue.save()

    return redirect('dashboard')


@login_required
def view_issue(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)

    context = {
        'issue': issue
    }

    return render(request, 'view_issue.html', context)
