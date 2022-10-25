from rest_framework import serializers

from accounts.models import Profile

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError("Passwords don't match.")
        if attrs['old_password'] == attrs['new_password'] or attrs['old_password'] == attrs['new_password2']:
            raise serializers.ValidationError("New password(s) must be different.")
        return attrs

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'username',
            'profile_picture'
        ]