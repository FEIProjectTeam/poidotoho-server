from ninja import ModelSchema, Field

from api.models import GamingSession


class GamingSessionSchema(ModelSchema):
    grade: int = Field(..., ge=1, le=9)

    class Meta:
        model = GamingSession
        fields = ["nickname", "score", "time_left"]
