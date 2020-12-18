from flask import Flask
app = Flask(__name__)


import lib8relay

@app.route('/')
def landing_page():
	return "INSTRUCTIONS:\
	<br/>Use as following: \"IP ADDR\":5000/SET/\"RELAY NUM\"/\"ACTION\"\
	<br/>Where RELAY NUM is the relay number from 1 to 8\
	<br/>ACTION can be 1 for ON or 0 for OFF\
	<br/>Examples:\
	<br/> 127.0.0.1:5000/SET/1/1  Turn ON relay 1\
	<br/> 127.0.0.1:5000/SET/1/0  Turn OFF relay 1\
	<br/> 127.0.0.1:5000/SET/2/1  Turn ON relay 2\
	<br/> 127.0.0.1:5000/SET/2/0  Turn OFF relay 2\
	<br/> 127.0.0.1:5000/SET/8/1  Turn ON relay 8\
	<br/> 127.0.0.1:5000/SET/8/0  Turn OFF relay 8\
	<br/>\
	<br/>\
	<br/> 127.0.0.1:5000/GET  Get the state of all relays"

def parse_relay_status(status):
	array = []
	for i in range(7,-1,-1):
		if 2**i > status:
			pass
		elif 2**i <= status:
			array.append(i+1)
			status = status - 2**i
	return array

@app.route('/SET/<int:number>/<int:action>')
def set(number, action):
	if number > 8 or number < 1:
		return "Relay numbers can only be up to 8"
	if action != 1 and action != 0:
		return "Please use 0 to turn OFF or 1 to turn ON the relay"
	lib8relay.set(0, number, action)
	if action == 1:
		onoff = "ON"
	elif action == 0:
		onoff = "OFF"
	else:
		return "This should never happen. Action is not 0 or 1"
	ret = parse_relay_status(lib8relay.get_all(0))
	return "Switched %s  relay number: %d <br/>Relays ON:%s" %(onoff, number, ret)



@app.route('/GET')
def gett():
	ret = parse_relay_status(lib8relay.get_all(0))
	return "Relays ON:%s" %ret
	#lib8relay.get_all(0)


			
