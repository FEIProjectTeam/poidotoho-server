from ninja import ModelSchema, Field

from api.models import GamingSession, School


class GamingSessionSchema(ModelSchema):
    score: int = Field(..., ge=0, le=100)
    time_left: int = Field(..., ge=0, le=1500)
    school_id: int

    class Meta:
        model = GamingSession
        fields = ["nickname", "grade"]


class SchoolSchema(ModelSchema):
    class Meta:
        model = School
        fields = ["id", "name"]


class LeaderboardSchema(ModelSchema):
    class Meta:
        model = GamingSession
        fields = ["nickname", "score", "time_left"]
