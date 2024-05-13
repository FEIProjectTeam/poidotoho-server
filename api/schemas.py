from ninja import ModelSchema

from api.models import GamingSession


class GamingSessionSchema(ModelSchema):
    class Meta:
        model = GamingSession
        fields = ["nickname", "grade", "score", "time_left"]
