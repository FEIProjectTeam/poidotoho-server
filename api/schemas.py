from ninja import ModelSchema

from api.models import GamingSession


class GamingSessionSchema(ModelSchema):
    class Meta:
        model = GamingSession
        fields = ["nickname", "score", "time_left"]
