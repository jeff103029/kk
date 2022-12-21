import random
from flask import Flask, render_template, request, make_response, jsonify

import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/webhook3", methods=["POST"])
def webhook3():
    req = request.get_json(force=True)
    
    action =  req.get("queryResult").get("action")
    #msg =  req.get("queryResult").get("queryText")
                                                       
    if (action == "keywordchoice"):
        keyword =  req.get("queryResult").get("parameters").get("keyword")
        
        if (keyword == "物品"):
            collection_ref = db.collection("item")
            docs = collection_ref.order_by("Question").limit(10).get()
            result = ""
        
            info = "您選擇的題目是：" + "\n"
            for doc in docs:
                dict=doc.to_dict()
          
                if keyword in dict["sort"]:
                result += "題目：" + dict["Question"] + "\n"
        info += result
    return make_response(jsonify({"fulfillmentText": info}))