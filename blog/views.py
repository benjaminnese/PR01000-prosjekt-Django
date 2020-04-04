from django.views import generic
from .models import Post
from django.shortcuts import render


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'


def home(request):
    return render(request, 'index.html', {})


def spes(request):
    return render(request, 'specialist.html', {})


def project(request):
    return render(request, 'description.html', {})


def about(request):
    return render(request, 'about.html', {})


def login(request):
    return render(request, 'admin/login.html', {})


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'








def spec2(request):
    return render(request, 'specialist2.html', {})

def spec3(request):
    return render(request, "specialist3.html", {})

def johnAriki(request):
    return render(request, 'spec_profile/johnAriki.html', {})

def profYacobArsanoAtito(request):
    return render(request, 'spec_profile/profYacobArsanoAtito.html', {})

def runeBakke(request):
    return render(request, 'spec_profile/runeBakke.html', {})

def waiswaDaudaBatega(request):
    return render(request, 'spec_profile/waiswaDaudaBatega.html', {})

def drJarleTBjerkhot(request):
    return render(request, 'spec_profile/drJarleTBjerkhot.html', {})

def drWCTKGunawardana(request):
    return render(request, 'spec_profile/drWCTKGunawardana.html', {})

def drGBBHerath(request):
    return render(request, 'spec_profile/drGBBHerath.html', {})

def drKBSJinadasa(request):
    return render(request, 'spec_profile/drKBSJinadasa.html', {})

def balachandranKetheesan(request):
    return render(request, 'spec_profile/balachandranKetheesan.html', {})

def nickKilimani(request):
    return render(request, "spec_profile/nickKilimani.html", {})

def edwardKirumira(request):
    return render(request, 'spec_profile/edwardKirumira.html', {})

def synneKleiven(request):
    return render(request, 'spec_profile/synneKleiven.html', {})

def mal(request):
    return render(request, 'spec_profile/mal.html', {})








