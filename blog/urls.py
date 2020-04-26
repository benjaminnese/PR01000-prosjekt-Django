from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,  name='home'),
    path('news_page/', views.PostList.as_view(), name='news_page'),
    path('Specialist/', views.spes, name='Specialist'),
    path('project/', views.project, name='project'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name="login"),
    path('news_page/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('links/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

    path('projects/asia/', views.asia, name='asia'),
    path('projects/africa/', views.africa, name='africa'),


    path('spec_profile/mal/', views.mal, name='mal'),
    path('spec_profile/johnAriki/', views.johnAriki, name='johnAriki'),
    path('spec_profile/profYacobArsanoAtito/', views.profYacobArsanoAtito, name='profYacobArsanoAtito'),
    path('spec_profile/runeBakke/', views.runeBakke, name='runeBakke'),
    path('spec_profile/waiswaDaudaBatega/', views.waiswaDaudaBatega, name='waiswaDaudaBatega'),
    path('spec_profile/drJarleTBjerkhot/', views.drJarleTBjerkhot, name='drJarleTBjerkhot'),
    path('spec_profile/drWCTKGunawardana/', views.drWCTKGunawardana, name='drWCTKGunawardana'),
    path('spec_profile/drGBBHerath/', views.drGBBHerath, name='drGBBHerath'),
    path('spec_profile/drKBSJinadasa/', views.drKBSJinadasa, name='drKBSJinadasa'),
    path('spec_profile/balachandranKetheesan/', views.balachandranKetheesan, name='balachandranKetheesan'),
    path('spec_profile/nickKilimani/', views.nickKilimani, name='nickKilimani'),
    path('spec_profile/edwardKirumira/', views.edwardKirumira, name='edwardKirumira'),
    path('spec_profile/synneKleiven/', views.synneKleiven, name='synneKleiven'),
    
    path('specialist2/', views.spec2, name='Specialist2'),
    path('spec_profile/profSivashanthiniKuganathan/', views.profSivashanthiniKuganathan, name='profSivashanthiniKuganathan'),
    path('spec_profile/EngMissThakshajiniLogeswaran/', views.EngMissThakshajiniLogeswaran, name='EngMissThakshajiniLogeswaran'),
    path('spec_profile/zakharMaletskyi/', views.zakharMaletskyi, name='zakharMaletskyi'),
    path('spec_profile/profFrancisMutua/', views.profFrancisMutua, name='profFrancisMutua'),
    path('spec_profile/profKDWNandalal/', views.profKDWNandalal, name='profKDWNandalal'),
    path('spec_profile/dalmasOmia/', views.dalmasOmia, name='dalmasOmia'),
    path('spec_profile/toneJoranOredalen/', views.toneJoranOredalen, name='toneJoranOredalen'),
    path('spec_profile/profKPPPathirana/', views.profKPPPathirana, name='profKPPPathirana'),
    path('spec_profile/drMdMafizurRahman/', views.drMdMafizurRahman, name='drMdMafizurRahman'),
    path('spec_profile/drDoungRatha/', views.drDoungRatha, name='drDoungRatha'),
    path('spec_profile/harshaRatnaweera/', views.harshaRatnaweera, name='harshaRatnaweera'),
    path('spec_profile/hansRenssen/', views.hansRenssen, name='hansRenssen'),
    
    path('specialist3/', views.spec3, name='Specialist3'),
    path('spec_profile/drMonaSabo/', views.drMonaSabo, name='drMonaSabo'),
    path('spec_profile/toreSaetersdal/', views.toreSaetersdal, name='toreSaetersdal'),
    path('spec_profile/engDSaliyaSampath/', views.engDSaliyaSampath, name='engDSaliyaSampath'),
    path('spec_profile/nimalkaSanjeewani/', views.nimalkaSanjeewani, name='nimalkaSanjeewani'),
    path('spec_profile/ronaldPaulDdumbaSemyalo/', views.ronaldPaulDdumbaSemyalo, name='ronaldPaulDdumbaSemyalo'),
    path('spec_profile/drSubramaniamSivakumar/', views.drSubramaniamSivakumar, name='drSubramaniamSivakumar'),
    path('spec_profile/liveSembVestgarden/', views.liveSembVestgarden, name='liveSembVestgarden'),
    path('spec_profile/profSBWeerakoon/', views.profSBWeerakoon, name='profSBWeerakoon'),
    

]



