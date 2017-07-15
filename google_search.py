from google import google
import search2

from flask import request
import json
from flask import Flask
from flask import jsonify
app = Flask(__name__)

'''
Basically make this a service.
Add account api calls in there?
'''

@app.route("/get_urls",methods=["POST"])
def get_urls():
    terms = request.get_json()
    """
        get results from google for search terms
    """
    res_set = set()
    results = []
    # First try google search API
    for term in terms:
        search_results = google.search(term["query"], term["num_pages"])
        for x in search_results:
            if x.link not in res_set:
                results.append({"q":term["query"],"url":x.link,"language":term["language"]})
                res_set.add(x.link)

    print len(results)
    # If it's not working, we might be blocked. Get results through browser
    if results:
        results = search2.do_search(terms)
    return jsonify(results)

if __name__ == '__main__':
    app.run()
