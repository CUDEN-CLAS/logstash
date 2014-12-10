from elasticsearch import Elasticsearch
from pprint import pprint
from textblob import TextBlob

es = Elasticsearch()

#query to find all tweets that don't have a sentiment field
query = {
    "query": {
        "filtered": {
            "filter": {
                "missing": {"field":"sentiment"}
            }
        } 
    }
}

res = es.count(index="twitter-*", doc_type=['twitter'], body=query)
if res['count'] > 0:
    res = es.search(index="twitter-*", doc_type=['twitter'], body=query)

    for tweet in res['hits']['hits']:
        doc = tweet['_source']
        sent = TextBlob(doc['message']).sentiment

        if sent.polarity < 0:
            sentiment = "negative"
        elif sent.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        doc['sentiment'] = sentiment
        doc['polarity'] = sent.polarity
        doc['subjectivity'] = sent.subjectivity

        es.index(index=tweet['_index'], doc_type=tweet['_type'], id=tweet["_id"], body=doc)
else:
    print "no items to process"
