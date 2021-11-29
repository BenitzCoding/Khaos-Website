from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os

web = Flask(__name__)

@web.route('/')
def index():
	return render_template('index.html')

@web.route('/home')
def home():
	return render_template('index.html')

@web.route('/tos')
def tos():
	return render_template('terms.html')

@web.route('/terms')
def terms():
	return render_template('terms.html')

@web.route('/privacy')
def privacy():
	return render_template('privacy.html')

@web.route('/policy')
def policy():
	return render_template('privacy.html')

@web.route('/discord')
def discord():
	return render_template('discord.html')

@web.route('/github')
def github():
	return render_template('github.html')

@web.route('/partner')
def partner():
	return render_template('partner.html')

@web.route('/apply')
def apply():
	return render_template('apply.html')

@web.route('/devs/pings/refresh')
def refresh():
	os.system('ls -l; git pull origin main')
	return render_template('refresh.html')

@web.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@web.errorhandler(500)
def error(e):
	print(e)
	return render_template('500.html'), 500

web.run(host="127.0.0.1", port=2000)