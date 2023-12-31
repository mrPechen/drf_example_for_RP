from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from RP_app.api.views import user_views, currency_views, tracked_currency_view
from django.urls import path

urlpatterns = [
    path('user/register', user_views.registration_new_user),
    path('user/login', TokenObtainPairView.as_view()),
    path('rates', currency_views.get_rates),
    path('currency/user_currency', tracked_currency_view.add_tracked_currency),
    path('currency/user_currency/<int:id>', tracked_currency_view.patch_or_delete_tracked_currency),
    path('currency/<int:id>/analytic', currency_views.analytics),
    path('test', currency_views.test),
    path('refresh', TokenRefreshView.as_view())
]
