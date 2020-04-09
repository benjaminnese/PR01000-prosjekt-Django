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

    path('specialist2/', views.spec2, name='Specialist2'),
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
    path('spec_profile/mal/', views.mal, name='mal'),

    path('specialist3/', views.spec3, name='Specialist3'),
]



