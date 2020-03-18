from flask import Blueprint, redirect, request
from bulletin import app
#from bulletin.views import ListView, DetailView, api_adverts_get, api_adverts_post, api_ad_detail_get, api_comment_add, api_tag_add, api_ad_stat
from bulletin.views import *

adverts = Blueprint('adverts', __name__, template_folder='templates')

# Register the urls for views
adverts.add_url_rule('/ru/', view_func=ListView.as_view('list'))
adverts.add_url_rule('/ru/<slug>/', view_func=DetailView.as_view('detail'))

@app.route('/')
def index():
    return render_template('index.html')

# Register the urls for API
@app.route('/api/', methods=['GET', 'POST'])
def adverts_api():
    if request.method == 'GET':
        result = api_adverts_get()

    elif request.method == 'POST':
        result = api_adverts_post()

    return result

@app.route('/api/<slug>/', methods=['GET'])
def ad_detail_api(slug):
    result = api_ad_detail_get(slug)
    return result

@app.route('/api/<slug>/comment/add/', methods=['POST'])
def add_comment_api(slug):
    result = api_comment_add(slug)
    return result

@app.route('/api/<slug>/tag/add/', methods=['POST'])
def add_tag_api(slug):
    result = api_tag_add(slug)
    return result

@app.route('/api/<slug>/stat', methods=['GET'])
def ad_stat_api(slug):
    result = api_ad_stat(slug)
    return result