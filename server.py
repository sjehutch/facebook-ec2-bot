from flask import Flask, request
import json
import requests
import boto3

app = Flask(__name__)

ec2 = boto3.setup_default_session(region_name='us-east-1')
ec2 = boto3.resource('ec2')

ACCESS_TOKEN = "Facebook Token you will get this when you create your facebook app"

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }

    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


### Use this to get the facebook webhook running - use the word secret in the webhook code
@app.route('/', methods=['GET'])
def handle_verification():
     return request.args['hub.challenge']
    
### This handles the facebook POST for the bot
@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    
   
    if message == "ec2":
        ec2.create_instances(ImageId='ami-c58c1dd3', MinCount=1, MaxCount=1, InstanceType="t2.micro")
        ec2.create_key_pair(KeyName='t2-micro-scott')
        message = "Awesome your ec2 instances are being created"

        reply(sender, message)
       
    return message


if __name__ == '__main__':
    app.run(debug=True)
