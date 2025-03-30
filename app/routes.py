from flask import Blueprint, render_template, request, jsonify
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
index_name = "public_dataset"

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', title='Home')

@bp.route('/api/search', methods=['GET'])
def api_search():
    query = request.args.get('q', '')
    size = request.args.get('size', '10')
    results = []
    if len(query) > 2:
        search_body = {
            "size": int(size) or 3,
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["first_name", "last_name", "job_title"],
                    "type": "phrase_prefix"
                }
            }
        }

        response = es.search(index=index_name, body=search_body)
        
        hits = response.get('hits', {}).get('hits', [])
        results = [hit['_source'] for hit in hits]
    return jsonify(results)