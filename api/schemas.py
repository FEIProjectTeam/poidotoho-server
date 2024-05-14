from ninja import ModelSchema, Field

from api.models import GamingSession, School


class GamingSessionSchema(ModelSchema):
    grade: int = Field(..., ge=1, le=9)
    school_id: int

    class Meta:
        model = GamingSession
        fields = ["nickname", "score", "time_left"]


class SchoolSchema(ModelSchema):
    class Meta:
        model = School
        fields = ["id", "name"]
