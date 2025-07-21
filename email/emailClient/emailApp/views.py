from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def index(request):
    pass
def compose_new_email(request):
    if not request.user.is_authenticated:
        return redirect('login_view')
    
    if request.method != 'POST':
        return JsonResponse({'error': 'POST request required.'}, status=405)
    
    emailPayLoad = json.loads(request.body)

    recipients = emailPayLoad.get['recipients', '']
    subject = emailPayLoad.get['subject', '']
    body = emailPayLoad.get['body', '']

    if not recipients or not subject or not body:
        return JsonResponse({'error': 'Do not leave empty fields.'}, status=400)
    
    

    return HttpResponse('Compose a new email')
def load_mailbox(request, mailbox):
    return HttpResponse('Load specific mailbox.')
def email_detail(request, email_id):
    return HttpResponse('Display email detail.')
def register_new_account(request):
    return HttpResponse('Register a new account.')
def login_view(request):
    return HttpResponse('Log in.')
def logout_view(request):
    return HttpResponse('Log out.')