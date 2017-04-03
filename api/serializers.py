from rest_framework import serializers

from contests.models import Contest


class ContestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contest
        fields = ('hashtag_1', 'c1', 'hashtag_2','c2','result')