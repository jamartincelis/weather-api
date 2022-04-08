from notification.models import Notification, Notification
from rest_framework import serializers

class NotificationSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de una notificacion.
    """
    class Meta:
        model = Notification
        fields = '__all__'