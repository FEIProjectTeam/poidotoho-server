from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from api.models import GamingSession, School
from api.schemas import GamingSessionSchema, SchoolSchema

api = NinjaAPI()


@api.get("/gaming-sessions", response=list[GamingSessionSchema])
def list_gaming_sessions(request):
    qs = GamingSession.objects.all()
    return qs


@api.post("/gaming-sessions/create")
def create_gaming_session(request, payload: GamingSessionSchema):
    get_object_or_404(School, id=payload.school_id)
    GamingSession.objects.create(**payload.dict())
    return {"success": True}


@api.get("/schools", response=list[SchoolSchema])
def list_schools_by_name(request, name: str):
    qs = School.objects.filter(name__icontains=name)[:30]
    return qs
