from elasticsearch import Elasticsearch
from flask import Flask
from flask import render_template
from flask import request
import os
host = os.environ.get('ES_PORT_9200_TCP_ADDR')
es = Elasticsearch([{'host': host}])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        myvar = request.args.get("q")
        res = es.search(index="test", body={"query": {"query_string": {"query": myvar}}})
        hits = res['hits']['total']
        items=res['hits']['hits']
        results = [each['_source']['text'] for each in items]
        context = {'results': results}
      
        return render_template('results.html', **context)
	
        
@app.route('/index', methods=['GET','POST'])
def data():
    
    
    if request.method == 'POST':
        myindex = request.form["a"]
        doc = {'text':myindex}
  	es.index(index ="test",doc_type='page',body=doc)
  	return "indexed"
#res = es.search(index="pagemango", body={"query": {"match_all": {}}})
#print res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
