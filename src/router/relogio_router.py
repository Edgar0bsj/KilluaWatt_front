from fastapi import APIRouter, HTTPException, Request, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import httpx

router = APIRouter(prefix="/relogio", tags=["Relogio"])
templates = Jinja2Templates(directory="src/templates")


@router.get("/", name="relogio")
async def relogio_list(request: Request):

    url = "http://127.0.0.1:8080/relogio/"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)

            # Levanta uma exceção caso o status code seja de erro (ex: 404, 500)
            response.raise_for_status()

            res_dados = response.json()

        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=f"Erro na API externa: {e.response.text}",
            )
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=503,
                detail=f"Não foi possível conectar ao serviço externo: {e}",
            )

    return templates.TemplateResponse(
        request=request,
        name="relogio_view/index.html",
        context={
            "titulo": "Relogio",
            "active_page": "relogio",
            "data": res_dados,
        },
    )


#
#
#
#
#
#
@router.post("/", name="relogio_add")
async def create_relogio(
    request: Request, nome: str = Form(...), codigo: str = Form(...)
):

    url = "http://127.0.0.1:8080/relogio/"

    payload = {"nome": nome, "codigo": codigo}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url=url, json=payload)
            response.raise_for_status()

        except httpx.HTTPStatusError as e:
            print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")

        except httpx.RequestError as e:
            print(f"Erro de conexão: {e}")

        finally:
            return RedirectResponse(
                url="/relogio/", status_code=status.HTTP_303_SEE_OTHER
            )


#
#
#
#
#
#
@router.post("/edit", name="relogio_edit")
async def update_relogio(
    request: Request,
    id: str = Form(...),
    nome: str = Form(...),
    codigo: str = Form(...),
):

    url = f"http://127.0.0.1:8080/relogio/{id}"

    payload = {"nome": nome, "codigo": codigo}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.put(url=url, json=payload)
            response.raise_for_status()

        except httpx.HTTPStatusError as e:
            print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")

        except httpx.RequestError as e:
            print(f"Erro de conexão: {e}")

        finally:
            return RedirectResponse(
                url="/relogio/", status_code=status.HTTP_303_SEE_OTHER
            )


#
#
#
#
#
#
@router.post("/del", name="relogio_del")
async def delete_relogio(
    request: Request,
    id: str = Form(...),
):

    url = f"http://127.0.0.1:8080/relogio/{id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url=url)
            response.raise_for_status()

        except httpx.HTTPStatusError as e:
            print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")

        except httpx.RequestError as e:
            print(f"Erro de conexão: {e}")

        finally:
            return RedirectResponse(
                url="/relogio/", status_code=status.HTTP_303_SEE_OTHER
            )
