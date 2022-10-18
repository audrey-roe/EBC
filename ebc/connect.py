'''
API COMMUNICATION WITH META

This is used for handling the data from the facebook graph API
'''

import requests

AUTH ='Bearer ' + 'EAAJRq1e1wC4BAGfyaKKeAWWEZAHXVoClfFCoUaLNNxtZCl1QkWTlEaXyQ7v80TpaaroWxWZAzZB6o9uHZAEhnXHvOcUQbhyCgjKkyjhmgMEnMbVeaRuOPsy5U4CGTSK8ZCZBDMOFR6CoisaPjrRFaZCFq9CVKaMiSOCnMVpoTiradTkRR85OjPzZCBDMbiMwyZC7OaRAnNucRNBMFYCs8VXSZCZC'


class whatsapp:
    def __init__(self,**kwargs):#bot_id,message,to,payload,template_type
        self.to = str(kwargs.get('to', None))
        self.bot_id = str(kwargs.get('bot_id', None))
        self.message = kwargs.get('message', None)
        self.payload = kwargs.get('payload', None)
        self.template = kwargs.get('template', None)
        self.mess_id = kwargs.get('mess_id', None)
        self.interactive = kwargs.get('interactive', None)
        

    def basic_send_message(self):
        if not self.mess_id == None:
            baba = self.read()
        datas = {
                "messaging_product": "whatsapp",
                "to": self.to,
                "recipient_type": "individual",
                "type": "text",
                "text": { # the text object
                    "preview_url": False,
                    "body": self.message
                }
                }
        headers ={
            'Authorization' : AUTH,
            'Content-Type' : 'application/json'
        }
        response = requests.request('POST', 'https://graph.facebook.com/v14.0/'+ self.bot_id + '/messages',headers = headers,json=datas)
        return response.json()


    def interactive_message(self):
        if not self.mess_id == None:
            baba = self.read()
        datas = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": self.to,
        "type": "interactive",
        "interactive": {
            "type": self.message['type'],
            "header": {
            "type": "text",
            "text": self.message['header']
            },
            "body": {
            "text": self.message['body']
            },
            "footer": {
            "text": self.message['footer']
            },
            "action":self.interactive
        }
        }
        headers ={
            'Authorization' : AUTH,
            'Content-Type' : 'application/json'
        }
        response = requests.request('POST', 'https://graph.facebook.com/v14.0/'+ self.bot_id + '/messages',headers = headers,json=datas)
        return response.json()

    def template_message(self):
        datas = {
                "messaging_product": "whatsapp",
                "to": self.to,
                "recipient_type": "individual",
                "type": 'template',
                "template": { # the t object
                    "name": self.template,
                    "language": {
                        "code": "en"
                                }
                            }
                }
        headers ={
            'Authorization' : AUTH,
            'Content-Type' : 'application/json'
        }
        response = requests.request('POST', 'https://graph.facebook.com/v14.0/'+ self.bot_id + '/messages',headers = headers,json=datas)
        return response.json()


    def media_message(self):  #incomplete
        headers ={
            'Authorization' : AUTH,
            'Content-Type' : 'application/json'
        }

        file = {}
        resp = requests.request('get', 'https://graph.facebook.com/v14.0/'+ self.bot_id + '/messages',files= file)

        datas = {
                "messaging_product": "whatsapp",
                "to": self.to,
                "type": "image",
                "image": {
                    "id" : "MEDIA_OBJECT_ID"
                }
                }
        
        response = requests.request('POST', 'https://graph.facebook.com/v14.0/'+ self.bot_id + '/messages',headers = headers,json=datas)
        return response.json()

    def call_to_action(self): #incomplete
        return None

    def read(self):
        datas = {
                "messaging_product": "whatsapp",
                "status": "read",
                "message_id": self.mess_id
                }
        headers ={
            'Authorization' : AUTH,
            'Content-Type' : 'application/json'
        }
        response = requests.request('POST', 'https://graph.facebook.com/v14.0/'+ self.bot_id + '/messages',headers = headers,json=datas)
        return response.json()
        
        
        

        

class facebook:
    x='SELF'

class instagram:
    x='SELF'