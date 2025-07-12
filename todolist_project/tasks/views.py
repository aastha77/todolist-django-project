from django.shortcuts import render

# ✅ This serves your index.html frontend
def frontend(request):
    return render(request, 'tasks/index.html')
