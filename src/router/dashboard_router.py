from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])
templates = Jinja2Templates(directory="src/templates")


@router.get("/", name="dashboard")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard_view/index.html",
        context={"titulo": "Dashboard", "active_page": "dashboard"},
    )
