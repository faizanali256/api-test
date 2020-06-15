from flask import Flask, request, jsonify
import os
import traceback
import pandas as pd
import wikipedia
app = Flask(__name__)

@app.route('/')
def hello_world():
	return("Hello!")
@app.route('/wiki/English', methods=['POST'])
def predict():
	try:
		json_ = request.get_json()
		bot_id=json_['bot_id']
		user_id=json_['user_id']
		module_id=json_['module_id']
		channel=json_['channel']
		incoming=json_['incoming_message']
		search=wikipedia.search(incoming)
		message="here are some wiki suggestions "
		for i in range(0,2):
			ny = wikipedia.page(search[i])
			message+=ny.url+" \n "

		response=[{
		'user_id':user_id,
		'bot_id':bot_id,
		'module_id':module_id,
		 'message':message,
		 'suggested_replies':["Menu","Faqs"],
		 'blocked_input':False,
		}]
		return jsonify(response),200
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/wiki/French', methods=['POST'])
def predict1():
	try:
		json_ = request.get_json()
		bot_id=json_['bot_id']
		user_id=json_['user_id']
		module_id=json_['module_id']
		channel=json_['channel']
		incoming=json_['incoming_message']
		wikipedia.set_lang("fr")
		search=wikipedia.search(incoming)
		message="here are some wiki suggestions "
		for i in range(0,3):
			ny = wikipedia.page(search[i])
			message+=ny.url+" \n "
		response=[{
		'user_id':user_id,
		'bot_id':bot_id,
		'module_id':module_id,
		 'message':message,
		 'suggested_replies':["Menu","Faqs"],
		 'blocked_input':False,
		}]
		return jsonify(response),200
	except:
		return jsonify({'trace': traceback.format_exc()})
if __name__=='__main__':
    app.run( debug=True)