''' This will be the URL Dispatcher, i.e., the file that will be in charge of
linking the pages to the controller '''

from django.urls import path
from django.contrib.auth import views as auth_views
from yalladevelop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('', views.index, name='index'),
               path('signup/', views.signup_user, name="signup"),
               path('login/', auth_views.LoginView.as_view(template_name='yalladevelop/login.html'), name="login"),
               path('logout/', views.logout_user, name="logout"),
               path('project/<int:project_id>/', views.showProject, name='showProject'),
               path('profile/<int:profile_id>/', views.showProfile, name='showProfile'),
               path('profile/', views.showProfile, name='showProfile'),
               path('addproject/', views.addProject, name='addProject'),
               path('forgotpassword/', views.forgotPassword, name='forgotPassword'),
               path('profile_settings/', views.profileSettings, name='profileSettings'),

               path('userorcompany/', views.userorcompany, name="userorcompany"),
               path('user-signup/', views.signup_user, name="signup_user"),
               path('track/', views.track, name="track"),
               path('company-signup/', views.signup_company, name="signup_company"),

               path('search_skills/', views.search_skills, name="search_skills"),
               path('search_skills/<int:skill_id>/', views.search_skills, name="search_skills"),

               # Functions dispatcher
               path('project/(<int:project_id>/likeProject', views.likeProject, name='likeProject'),
               path('project/(<int:project_id>/helpProject', views.helpProject, name='helpProject'),
               path('project/(<int:project_id>/donate/', views.donate, name='donate'),
               path('project/(<int:project_id>/promote/', views.promote, name='promote'),

               path('project/<int:project_id>/edit', views.editProject, name='editProject'),

               path('post_comment/', views.postComment, name='postComment'),
               path('user_upload/', views.user_upload, name='user_upload'),

               # Static Pages Dispatcher
               path('about/', views.about, name="about"),
               path('contact/', views.contact, name="contact"),
               path('explore/', views.explore, name="explore"),
               path('allprojects/', views.allprojects, name="allprojects"),
               path('allusers/', views.allusers, name="allusers"),
               path('allcompanies/', views.allcompanies, name="allcompanies"),
               path('faq/', views.faq, name="faq"),
               path('help/', views.help, name="help"),
               path('privacy/', views.privacy, name="privacy"),
               path('sitemap/', views.sitemap, name="sitemap"),
               path('terms/', views.terms, name="terms"),
               path('rankings/', views.rankings, name='rankings'),

               path('getProfilePicture/<int:user_id>/', views.getProfilePicture,
                    name='getProfilePicture'),
               path('getProjectPicture/<int:project_id>/', views.getProjectPicture,
                    name='getProjectPicture'),

               # DEVELOEPR HELP
               path('developerhelp/', views.dhelp, name='dhelp'),
               ]
