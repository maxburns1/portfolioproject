from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project
from .forms import ContactForm


def home(request):
    featured = Project.objects.filter(is_featured=True)[:3]
    if not featured.exists():
        # Graceful fallback before any project is marked featured
        featured = Project.objects.all()[:3]
    return render(request, "home.html", {"featured_projects": featured})


def about(request):
    return render(request, "about.html")


def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "projects/project_detail.html", {"project": project})


def skills(request):
    return render(request, "skills.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks for reaching out — I'll get back to you within 48 hours.",
            )
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
