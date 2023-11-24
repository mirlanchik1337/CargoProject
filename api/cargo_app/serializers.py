from rest_framework import serializers

from api.cargo_app.models import Status, TrackCode, Group






class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class StatusForTrackCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = 'name_status'


class TrackCodeSerializer(serializers.ModelSerializer):
    status_id = serializers.IntegerField(write_only=True, required=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = TrackCode
        fields = '__all__'

    def create(self, validated_data):
        status_id = validated_data.pop('status_id')
        status = Status.objects.get(id=status_id)
        track_code = validated_data['track_code']
        date = validated_data['date']
        track_code_instance = TrackCode.objects.create(track_code=track_code, status=status, date=date)
        return track_code_instance

    def get_status(self, obj):
        return f"{obj.status.name_status}"


class GroupSerializer(serializers.ModelSerializer):
    track_codes = TrackCodeSerializer(many=True)
    statuses = StatusSerializer()

    class Meta:
        model = Group
        fields = '__all__'


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


