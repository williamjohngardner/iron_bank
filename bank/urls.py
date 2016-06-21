"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout
from app.views import IndexView, CreateUserView, ProfileView, TransactionView, CreateTransactionView, TransferFundsView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout, name="logout"),
    url(r'^create_user/$', CreateUserView.as_view(), name="create_user"),
    url(r'^accounts/profile/$', login_required(ProfileView.as_view()), name="profile_view"),
    url(r'^transaction/(?P<pk>\d+)/$', login_required(TransactionView.as_view()), name="transaction_view"),
    url(r'^create_transaction/$', login_required(CreateTransactionView.as_view()), name="create_transaction_view"),
    url(r'^transfer/$', login_required(TransferFundsView.as_view()), name="transfer_funds_view")
]
