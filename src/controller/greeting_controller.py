from inspira.decorators.http_methods import get, post
from inspira.decorators.path import path
from inspira.responses import TemplateResponse
from inspira.requests import Request


@path("/greeting")
class GreetingController:

    @get()
    async def index(self, request: Request):
        return TemplateResponse("index.html")

    @post()
    async def post_form(self, request: Request):
        form = await request.form()

        name = form['name']
        email = form['email']

        context = {
            "name": name,
            "email": email
        }

        return TemplateResponse("result.html", context)
