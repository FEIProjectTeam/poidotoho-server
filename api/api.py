from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from ninja.pagination import paginate

from api.models import GamingSession, School
from api.schemas import GamingSessionSchema, SchoolSchema, LeaderboardSchema

api = NinjaAPI(docs_url=None)


@api.get("/leaderboard/", response=list[LeaderboardSchema])
@paginate
def list_leaderboard(request):
    return GamingSession.objects.all().order_by("-score", "-time_left")


@api.post("/gaming-sessions/create/")
def create_gaming_session(request, payload: GamingSessionSchema):
    get_object_or_404(School, id=payload.school_id)
    GamingSession.objects.create(**payload.dict())
    return {"success": True}


@api.get("/schools/", response=list[SchoolSchema])
def list_schools_by_name(request, name: str):
    qs = School.objects.filter(name__icontains=name)[:30]
    return qs
