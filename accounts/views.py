from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import UserDevice


class LoginWithFingerprintView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        fingerprint = request.data.get('fingerprint')
        device_name = request.data.get('device_name')

        user = authenticate(username=username, password=password)

        if user:
            device_exists = UserDevice.objects.filter(user=user, device_id=fingerprint).exists()

            if not device_exists:
                count = UserDevice.objects.filter(user=user).count()
                if count >= 2:
                    return Response({
                        "error": "Limitga yetdingiz! Faqat 2 ta qurilmaga ruxsat berilgan. Iltimos, eski qurilmalarni o'chiring."
                    }, status=403)

                UserDevice.objects.create(
                    user=user,
                    device_id=fingerprint,
                    device_name=device_name
                )
                return Response({"message": "Yangi qurilma qo'shildi va tizimga kirildi!"}, status=200)

            return Response({"message": "Xush kelibsiz! (Tanish qurilma)"}, status=200)

        return Response({"error": "Login yoki parol noto'g'ri"}, status=401)