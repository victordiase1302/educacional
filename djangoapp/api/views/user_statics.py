from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User


class UserStatistics(APIView):
    def get(self, request):
        user_obj = User.objects.prefetch_related('fav_platforms')
        total_users = user_obj.count()
        inactive_users = user_obj.filter(is_active=False).count()
        users_by_country = user_obj.values('country').annotate(count=Count('id'))
        users_by_fav_platform = user_obj.filter(fav_platforms__isnull=False).distinct().count()

        data = {
            'total_users': total_users,
            'inactive_users': inactive_users,
            'users_by_country': users_by_country,
            'users_by_fav_platform': users_by_fav_platform,
        }
        return Response(data, status=status.HTTP_200_OK)
