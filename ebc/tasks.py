from celery import shared_task
from .bot import wabot

@shared_task
def send_mess(payload):
    log = wabot(reply = payload).clsc()
    return log

@shared_task
def ebc_notification(*args):
    if args.__len__() == 0:
        reply = {
                "name" :'' ,
                "phone" : 'recepients',
                "id" : '0',
                "message" : '',
                'bot_id' : '115809357801428'
                }
        log = wabot(reply = reply).business_initiate_log()
    else:
        reply = {
                "name" :'' ,
                "phone" : args[0],
                "id" : '0',
                "message" : '',
                'bot_id' : '115809357801428'
                }
        log = wabot(reply = reply).business_initiate_log()
    return log


@shared_task
def receive_message(payload):
    if payload['entry'][0]['changes'][0]['value']['metadata']['phone_number_id'] == '115809357801428':
        if payload['entry'][0]['changes'][0]['value'].get('statuses') == None:
            if payload['entry'][0]['changes'][0]['value']['messages'][0]['type'] == 'text':
                reply = {
                            "name" : payload['entry'][0]['changes'][0]['value']['contacts'][0]['profile']['name'] ,
                            "phone" : payload['entry'][0]['changes'][0]['value']['messages'][0]['from'],
                            "id" : payload['entry'][0]['id'],
                            "message" : payload['entry'][0]['changes'][0]['value']['messages'][0]['text']['body'],
                            'bot_id' : payload['entry'][0]['changes'][0]['value']['metadata']['phone_number_id'],
                            'message_id' : payload['entry'][0]['changes'][0]['value']['messages'][0]['id']
                            }

            elif payload['entry'][0]['changes'][0]['value']['messages'][0]['type'] == 'interactive':
                if payload['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['type'] == 'list_reply':
                    reply = {
                                "name" : payload['entry'][0]['changes'][0]['value']['contacts'][0]['profile']['name'] ,
                                "phone" : payload['entry'][0]['changes'][0]['value']['messages'][0]['from'],
                                "id" : payload['entry'][0]['id'],
                                "message" : payload['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['list_reply']['id'],
                                'bot_id' : payload['entry'][0]['changes'][0]['value']['metadata']['phone_number_id'],
                                'message_id' : payload['entry'][0]['changes'][0]['value']['messages'][0]['id']
                                }
                elif payload['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['type'] == 'button_reply':
                    reply = {
                                "name" : payload['entry'][0]['changes'][0]['value']['contacts'][0]['profile']['name'] ,
                                "phone" : payload['entry'][0]['changes'][0]['value']['messages'][0]['from'],
                                "id" : payload['entry'][0]['id'],
                                "message" : payload['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['button_reply']['id'],
                                'bot_id' : payload['entry'][0]['changes'][0]['value']['metadata']['phone_number_id'],
                                'message_id' : payload['entry'][0]['changes'][0]['value']['messages'][0]['id']
                                }
                elif payload['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['type'] == 'product_list':
                    reply = {
                                "phone" : payload['entry'][0]['changes'][0]['value']['statuses'][0]['recipient_id'],
                                "status" : payload['entry'][0]['changes'][0]['value']['statuses'][0]['status'],
                                'bot_id' : payload['entry'][0]['changes'][0]['value']['metadata']['phone_number_id'],
                                'message_id' : payload['entry'][0]['changes'][0]['value']['statuses'][0]['id']
                                }
        else:
            return None

        log = wabot(reply = reply).log_chat()#call bot
        return log
    else:
        return None


@shared_task
def delete():
   a = wabot().clear_chat()
   return a