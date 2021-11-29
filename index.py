from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import cv2
import os

web = FastAPI()
templates = Jinja2Templates(directory="templates")

@web.get('/')
async def index(request: Request):
	return templates.TemplateResponse('index.html', {'request': request})

@web.get('/home')
async def home(request: Request):
	return templates.TemplateResponse('index.html', {'request': request})

@web.get('/tos')
async def tos(request: Request):
	return templates.TemplateResponse('terms.html', {'request': request})

@web.get('/terms')
async def terms(request: Request):
	return templates.TemplateResponse('terms.html', {'request': request})

@web.get('/privacy')
async def privacy(request: Request):
	return templates.TemplateResponse('privacy.html', {'request': request})

@web.get('/policy')
async def policy(request: Request):
	return templates.TemplateResponse('privacy.html', {'request': request})

@web.get('/discord')
async def discord(request: Request):
	return templates.TemplateResponse('discord.html', {'request': request})

@web.get('/github')
async def github(request: Request):
	return templates.TemplateResponse('github.html'), {'request': request}

@web.get('/partner')
async def partner(request: Request):
	return templates.TemplateResponse('partner.html', {'request': request})

@web.get('/apply')
async def apply(request: Request):
	return templates.TemplateResponse('apply.html', {'request': request})

@web.get('/devs/pings/refresh')
async def refresh(request: Request):
	os.system('ls -l; git pull origin main')
	return templates.TemplateResponse('refresh.html')

# @web.errorhandler(404)
# async def page_not_found(e):
# 	return templates.TemplateResponse('404.html'), 404

# @web.errorhandler(500)
# async def error(e):
# 	print(e)
# 	return templates.TemplateResponse('500.html'), 500

if __name__ == '__main__':
	uvicorn.run(web, host="127.0.0.1", port=2000)