from typing import List

from ninja import NinjaAPI

from api.models import GamingSession
from api.schemas import GamingSessionSchema

api = NinjaAPI()


@api.get("/gaming-sessions", response=List[GamingSessionSchema])
def list_gaming_sessions(request):
    qs = GamingSession.objects.all()
    return qs


@api.post("/gaming-sessions/create")
def create_gaming_session(request, payload: GamingSessionSchema):
    GamingSession.objects.create(**payload.dict())
    return {"success": True}
