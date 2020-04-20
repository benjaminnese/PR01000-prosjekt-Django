from django.http import HttpResponse
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

def mal(request):
    return render(request, 'spec_profile/mal.html', {})


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


def profSivashanthiniKuganathan(request):
    return render(request, 'spec_profile/profSivashanthiniKuganathan.html', {})

def EngMissThakshajiniLogeswaran(request):
    return render(request, 'spec_profile/EngMissThakshajiniLogeswaran.html', {})

def zakharMaletskyi(request):
    return render(request, 'spec_profile/zakharMaletskyi.html', {})

def profFrancisMutua(request):
    return render(request, 'spec_profile/profFrancisMutua.html', {})

def profKDWNandalal(request):
    return render(request, 'spec_profile/profKDWNandalal.html', {})

def dalmasOmia(request):
    return render(request, 'spec_profile/dalmasOmia.html', {})

def toneJoranOredalen(request):
    return render(request, 'spec_profile/toneJoranOredalen.html', {})

def profKPPPathirana(request):
    return render(request, 'spec_profile/profKPPPathirana.html', {})

def drMdMafizurRahman(request):
    return render(request, 'spec_profile/drMdMafizurRahman.html', {})

def drDoungRatha(request):
    return render(request, 'spec_profile/drDoungRatha.html', {})

def harshaRatnaweera(request):
    return render(request, 'spec_profile/harshaRatnaweera.html', {})

def hansRenssen(request):
    return render(request, 'spec_profile/hansRenssen.html', {})

def drMonaSabo(request):
    return render(request, 'spec_profile/drMonaSabo.html', {})

def toreSaetersdal(request):
    return render(request, 'spec_profile/toreSaetersdal.html', {})

def engDSaliyaSampath(request):
    return render(request, 'spec_profile/engDSaliyaSampath.html', {})

def nimalkaSanjeewani(request):
    return render(request, 'spec_profile/nimalkaSanjeewani.html', {})

def ronaldPaulDdumbaSemyalo(request):
    return render(request, 'spec_profile/ronaldPaulDdumbaSemyalo.html', {})

def drSubramaniamSivakumar(request):
    return render(request, 'spec_profile/drSubramaniamSivakumar.html', {})

def liveSembVestgarden(request):
    return render(request, 'spec_profile/liveSembVestgarden.html', {})

def profSBWeerakoon(request):
    return render(request, 'spec_profile/profSBWeerakoon.html', {})
