'''
The Bot Framework
'''

from .models import wamessage_log, rec_numbers, customer
from .ebc_bconfig import whatsappbot
from .connect import whatsapp as wasend
import re
class wabot:
    def __init__(self, **kwargs):
        self.reply = kwargs.get('reply', None)

    def log_chat(self):
        
        check = wamessage_log.objects.filter(customer = int(re.sub("[^0-9]", "", str(customer.objects.get_or_create(customer_no = self.reply['phone'])))), customer_mess = True )# Query database
        pid = customer.objects.get(customer_no  = self.reply['phone'])
        if not check.exists():
            id, response, status, interactive =  whatsappbot(id = 0, number = self.reply['phone']).message_call()
            log = wamessage_log.objects.create(customer = pid,
                                        bot_id =self.reply['bot_id'],
                                        message = self.reply['message'],
                                        customer_mess = True,
                                        reply_id = id,
                                        message_status = status)
            log.save()
            log1 = wamessage_log.objects.create(customer = pid,
                                        bot_id =self.reply['bot_id'],
                                        message = response,
                                        customer_mess = False,
                                        reply_id = id,
                                        message_status = status)
            log1.save()
            if interactive == None:
                ret = wasend(to = self.reply['phone'], message = response, bot_id =self.reply['bot_id'], mess_id = self.reply['message_id'] ).basic_send_message()
            else: 
                ret = wasend(to = self.reply['phone'], message = response, bot_id =self.reply['bot_id'], mess_id = self.reply['message_id'], interactive = interactive ).interactive_message()

            return ret
        else:
            self.checks = (list(check))[-1]
        
            if self.checks.message_status == 'complete':
                id, response, status, interactive =  whatsappbot(id = 0, number = self.reply['phone']).message_call()

                log = wamessage_log.objects.create(customer = pid,
                                            bot_id =self.reply['bot_id'],
                                            message = self.reply['message'],
                                            customer_mess = True,
                                            reply_id = id,
                                            message_status = status)
                log.save()
                log1 = wamessage_log.objects.create(customer = pid,
                                            bot_id =self.reply['bot_id'],
                                            message = response,
                                            customer_mess = False,
                                            reply_id = id,
                                            message_status = status)
                log1.save()
                if interactive == None:
                    ret = wasend(to = self.reply['phone'], message = response, bot_id =self.reply['bot_id'], mess_id = self.reply['message_id'] ).basic_send_message()              
                else: 
                    ret = wasend(to = self.reply['phone'], message = response, bot_id =self.reply['bot_id'], mess_id = self.reply['message_id'], interactive = interactive ).interactive_message()
                return ret
            
            elif self.checks.message_status == 'on-going':
                id, response, status, interactive = whatsappbot(id = int(self.checks.reply_id), reply = self.reply['message'], number = self.reply['phone']).message_call()
                log = wamessage_log.objects.create(customer = pid,
                                            bot_id =self.reply['bot_id'],
                                            message = self.reply['message'],
                                            customer_mess = True,
                                            reply_id = id,
                                            message_status = status)
                log.save()
                log1 = wamessage_log.objects.create(customer = pid,
                                            bot_id =self.reply['bot_id'],
                                            message = response,
                                            customer_mess = False,
                                            reply_id = id,
                                            message_status = status)
                log1.save()
                if response == 'detachedbot':
                    return None
                elif interactive == None:
                    ret = wasend(to = self.reply['phone'], message = response, bot_id =self.reply['bot_id'], mess_id = self.reply['message_id'] ).basic_send_message()
                else: 
                    ret = wasend(to = self.reply['phone'], message = response, bot_id =self.reply['bot_id'], mess_id = self.reply['message_id'], interactive = interactive ).interactive_message()
                return ret
        
            

    def business_initiate_log(self):
        if self.reply['phone'] == 'recepients':
            for number in rec_numbers.objects.all():
                ret = wasend(to = number.number, template = 'client_offer', bot_id = '115809357801428').template_message()
        else:
            ret = wasend(to = self.reply['phone'], template = 'client_offer', bot_id = '115809357801428').template_message()
        return ret

    def clear_chat(self):
        a = wamessage_log.objects.all().delete()
        return a

    def clsc(self):
        log = wamessage_log.objects.create(customer = customer.objects.get(customer_no  = self.reply['phone']),
                                            bot_id =self.reply['bot_id'],
                                            message = self.reply['message'],
                                            customer_mess = False,
                                            reply_id = 36,
                                            message_status = 'on-going')
        log.save()
        ret = wasend(to = self.reply['phone'], bot_id = '115809357801428', message = self.reply['message']).basic_send_message()
        return ret