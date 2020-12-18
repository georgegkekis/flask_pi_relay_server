import os

os.environ['FLASK_APP'] = "/home/pi/8relay-rpi/python/8relay/flask_server.py"
os.environ['FLASK_ENV'] = "development"
import subprocess
os.system("flask run --host=0.0.0.0")
#subprocess.Popen("flask run --host=0.0.0.0")

