class whatsappbot():    
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.reply = kwargs.get('reply', None)


    def message_call(self):
        if self.id == 0:
            id, response, status, interactive = self.welcome()
            return id, response, status, interactive
        elif self.id == 1:
            id, response, status, interactive = self.welcome_next()
            return id, response, status, interactive
        elif self.id == 2:
            id, response, status, interactive = self.my_offers_next()
            return id, response, status, interactive
        elif self.id == 3:
            id, response, status, interactive = self.offer_300daily_next()
            return id, response, status, interactive    
        elif self.id == 4:
            id, response, status, interactive = self.offer_300daily_renewal_next()
            return id, response, status, interactive
        elif self.id == 5:
            id, response, status, interactive = self.offer_500daily_next()
            return id, response, status, interactive
        elif self.id == 6:
            id, response, status, interactive = self.offer_500daily_renewal_next()
            return id, response, status, interactive
        elif self.id == 7:
            id, response, status, interactive = self.offer_1500weekly_next()
            return id, response, status, interactive
        elif self.id == 8:
            id, response, status, interactive = self.offer_1500weekly_renewal_next()
            return id, response, status, interactive
        elif self.id == 9:
            id, response, status, interactive = self.offer_500bimonthly_next()
            return id, response, status, interactive
        elif self.id == 10:
            id, response, status, interactive = self.offer_500bimonthly_renewal_next()
            return id, response, status, interactive
        elif self.id == 11:
            id, response, status, interactive = self.offer_1000monthly_next()
            return id, response, status, interactive
        elif self.id == 12:
            id, response, status, interactive = self.offer_1000monthly_renewal_next()
            return id, response, status, interactive    
        elif self.id == 13:
            id, response, status, interactive = self.offer_1200monthly_next()
            return id, response, status, interactive
        elif self.id == 14:
            id, response, status, interactive = self.offer_1200monthly_renewal_next()
            return id, response, status, interactive
        elif self.id == 15:
            id, response, status, interactive = self.offer_1500monthly_next()
            return id, response, status, interactive
        elif self.id == 16:
            id, response, status, interactive = self.offer_1500monthly_renewal_next()
            return id, response, status, interactive
        elif self.id == 17:
            id, response, status, interactive = self.borrow_airtime_data_next()
            return id, response, status, interactive
        elif self.id == 18:
            id, response, status, interactive = self.social_plans_next()
            return id, response, status, interactive
        elif self.id == 19:
            id, response, status, interactive = self.social_bundle_next()
            return id, response, status, interactive
        elif self.id == 20:
            id, response, status, interactive = self.plus_bundles_next()
            return id, response, status, interactive
        elif self.id == 21:
            id, response, status, interactive = self.opera_bundles_next()
            return id, response, status, interactive
        elif self.id == 22:
            id, response, status, interactive = self.instagram_bundles_next()
            return id, response, status, interactive
        elif self.id == 23:
            id, response, status, interactive = self.streaming_bundle_next()
            return id, response, status, interactive
        elif self.id == 24:
            id, response, status, interactive = self.data_plans_next()
            return id, response, status, interactive
        elif self.id == 25:
            id, response, status, interactive = self.daily_bund_next()
            return id, response, status, interactive
        elif self.id == 26:
            id, response, status, interactive = self.ending_next()
            return id, response, status, interactive
        elif self.id == 27:
            id, response, status, interactive = self.weekly_bund_next()
            return id, response, status, interactive
        elif self.id == 28:
            id, response, status, interactive = self.monthly_bund_next()
            return id, response, status, interactive
        elif self.id == 29:
            id, response, status, interactive = self.data_pp_next()
            return id, response, status, interactive
        elif self.id == 30:
            id, response, status, interactive = self.mega_bund_next()
            return id, response, status, interactive
        elif self.id == 31:
            id, response, status, interactive = self.binge_plans_next()
            return id, response, status, interactive
        elif self.id == 32:
            id, response, status, interactive = self.big_data_next()
            return id, response, status, interactive
        elif self.id == 33:
            id, response, status, interactive = self.always_on_next()
            return id, response, status, interactive
        elif self.id == 34:
            id, response, status, interactive = self.faq_next()
            return id, response, status, interactive
        elif self.id == 35:
            id, response, status, interactive = self.recharge_next()
            return id, response, status, interactive
        elif self.id == 36:
            id, response, status, interactive = self.chat_agent_next()
            return id, response, status, interactive


    def welcome(self):#welcome
        welcome_string ={
                        'header' :"Welcome to Everything But Coffee!",
                        'body':"Hey 👋🏾 there, what can i help you with today?",
                        'type':'interactive'
                        }

        interactive = {
            "button": "SELECT ITEM",
            "sections": [
        {
          "title": "OPTIONS",
          "rows": [
            {
              "id": "1",
              "title": "🛒 Catalogue",
              "description": "Browse our inventory"
            },
            {
              "id": "2",
              "title": "🏷 Sales/ Offers/ Promotions",
              "description": "Check out our products on sale"
            },
            {
              "id": "3",
              "title": "🧾 Purchase/ Payments",
              "description": "Check out your transaction history"
            },
            {
              "id": "4",
              "title": "🧑🏾‍💻 Support - Chat with Customer",
              "description": "Chat with an agent to get some help with a customer care representative"
            },
            {
              "id": "5",
              "title": "🤖 Share Chatbot",
              "description": "Share the chatbot with others"
            },
            {
              "id": "6",
              "title": "📲 Quit",
              "description": "Exit the chatbot"
            },
          ]
        }
      ]
        }
        
        return 1, welcome_string, 'on-going', interactive

    def welcome_next(self):
        if (str(self.reply)).lower() == 'catalogue' or(str(self.reply)).lower() =='1':
            return self.catalogue()
        elif (str(self.reply)).lower() == 'sales' or (str(self.reply)).lower() == 'Sales/ Offers/ Promotions' or(str(self.reply)).lower() == 'offers' or(str(self.reply)).lower() == 'promotions' or (str(self.reply)).lower() =='2':
            return self.sale()
        elif (str(self.reply)).lower() == 'purchase' or (str(self.reply)).lower() =='3':
            return self.purchase()
        elif (str(self.reply)).lower() == 'support' or (str(self.reply)).lower() == '4':
            return self.pre_chat_agent()
        elif (str(self.reply)).lower() == 'share chatbot' or (str(self.reply)).lower() == 'share' or (str(self.reply)).lower() == '5':
            return self.share_bot()
        elif (str(self.reply)).lower() == 'q' or (str(self.reply)).lower() == 'quit' or(str(self.reply)).lower() == '6':
            return self.ending()
        else:
            return 1, 'I do not understand you.\nPlease kindly type in the corresponding number to the question or the option.', 'on-going', None

    def reminder(self):
        #i'm guessing we have to put a celery worker to 
        # trigger this function every 5 mins of no activity
        return 'Hey, Coffee lover still waiting on your response'

    def catalogue(self):
        data = {
            "type": "product_list",
            "header": {
                "type": "interactive",
                "text": "Catalogue"
            }}
        interactive = {
                    "body":{
                        "text": "Explore our fine range of coffee accessories"
                    },
                    "footer":{
                        "text": "Everything But Coffee"
                    },
                    "action":
                           { "catalog_id":"1239386806600403",
                            "sections": 
                            [
                                {
                                "title": "Stainless Steel Coffee Storage Containers",             
                                "product_items": [
                                    { "product_retailer_id": "kpqyd0o9hu" },
                                    # { "product_retailer_id": "product-SKU-in-catalog" },
                                ]},
                                {
                                "title": "Another Section",
                                "product_items": [
                                    { "product_retailer_id": "product-SKU-in-catalog" }
                                ]},
                        ]
                        },
                        }, 
        return 2, data, 'on-going', interactive
                              

    def catalogueNext(self):
        pass


    def sale(self):
        data = {
            "type": "product_list",
            "header": {
                "type": "interactive",
                "text": "Catalogue"
            }}
        interactive = {
                    "body":{
                        "text": "Explore our fine range of coffee accessories"
                    },
                    "footer":{
                        "text": "Everything But Coffee On Sale!"
                    },
                    "action":
                           { "catalog_id":"1239386806600403",
                            "sections": 
                            [
                                {
                                "title": "Machinery on Sale -  20%` discounts on all coffee machines offer lasts till the end of the month!",             
                                "product_items": [
                                    { "product_retailer_id": "kpqyd0o9hu" },
                                    # { "product_retailer_id": "product-SKU-in-catalog" },
                                ]},
                                {
                                "title": "Coffee Filters on Sale!",
                                "product_items": [
                                    { "product_retailer_id": "kpqyd0o9hu" }
                                ]},
                                {
                                "title": "Coffee Mugs on Sale!",
                                "product_items": [
                                    { "product_retailer_id": "kpqyd0o9hu" }
                                ]},
                                {
                                "title": "Coffee Mugs on Sale!",
                                "product_items": [
                                    { "product_retailer_id": "kpqyd0o9hu" }
                                ]},
                                {
                                "title": "Coffee Mugs on Sale!",
                                "product_items": [
                                    { "product_retailer_id": "kpqyd0o9hu" }
                                ]},
                        ]
                        },
                        }, 
        return 2, data, 'on-going', interactive
                              

    def purchase(self):
        pass
    
    def post_purchase(self):

        pass



    def pre_chat_agent(self):
        data ={
                        'header' :"",
                        'body':"Hey 👋🏾 there, chat with our agents?",
                        'type':'interactive'
                        }

        interactive = {
            "button": "SELECT ITEM",
            "sections": [
        {
          "title": "OPTIONS",
          "rows": [
            {
              "id": "1",
              "title": "🔍 Can`t find a product",
              "description": "Browse our inventory"
            },
            {
              "id": "2",
              "title": "📍 Track Order",
              "description": "Check out our products on sale"
            },
            {
              "id": "3",
              "title": "🧾 Payment Issues",
              "description": "Check out your transaction history"
            },
            {
              "id": "4",
              "title": "🧐 Other Issues",
              "description": "Chat with an agent to get some help with a customer care representative"
            },
            {
              "id": "5",
              "title": "📲 Menu",
              "description": "Go to the main menu"
            },
            {
              "id": "6",
              "title": "😮‍💨 Quit",
              "description": "Exit the chatbot"
            },
          ]
        }
      ]
        }
        return 31, data, 'on-going', interactive

    def pre_chat_agent_next(self):
        
        if (str(self.reply)).lower() == 'Can`t find a Product' or (str(self.reply)).lower() =='1':
            return self.chat_agent_q()
        elif (str(self.reply)).lower() == 'Track Order' or (str(self.reply)).lower() =='2':
            return self.chat_agent_q()
        elif (str(self.reply)).lower() == 'Payment Issues' or (str(self.reply)).lower() =='3':
            return self.chat_agent_q()
        elif (str(self.reply)).lower() == 'Other Issues' or (str(self.reply)).lower() == '4':
            return self.chat_agent_q()
        elif (str(self.reply)).lower() == 'Menu' or (str(self.reply)).lower() == 'main menu' or (str(self.reply)).lower() == '5':
            return self.welcome()
        elif (str(self.reply)).lower() == 'q' or (str(self.reply)).lower() == 'quit' or(str(self.reply)).lower() == '6':
            return self.ending()
        else:
            return 32,'I do not understand you.\nPlease kindly type in the corresponding number to aid us in connecting you to right agent', 'on-going', None
    
    def chat_agent_q(self):
        data = {
                'header' :"Deep Sigh",
                'body':"All our agents are currently busy, would you like to wait on the queue?",
                'type':'button'
                }
        interactive = {"buttons": [{
                                "type": "reply",
                                "reply": {
                                    "id": "1",
                                    "title": "Sure why not! 🥹"
                                        }
                                        },
                                {
                                "type": "reply",
                                "reply": {
                                    "id": "0",
                                    "title": "Nope. 😒"
                                }
                                }
                                ]}
        return 26, data, 'on-going', interactive
    
    def chat_agent_q_next(self):
        if (str(self.reply)).lower() =='1':
            return self.chat_agent()
        elif (str(self.reply)).lower() == '0':
            return 26, 'Thank you for contacting us', 'complete', None
        else:
            return 26, "Didn't quite get you there, please try again", 'on-going', self.chat_agent_q()
    
    def chat_agent(self):
        data = """Hold-on as we connect you to an agent"""
        return 36, data, 'on-going', None

    def chat_agent_next(self):
        return 36, 'detachedbot','on-going', None

    def share_bot(self):
        data = "Share me in 3 Easy steps ⏩ \n\nYou can share me with your friends and family, and I will be more than happy to assist them. \n\nStep 1: Click on the link below 👇 \nStep 2: Choose contacts to send to\nStep 3: Send the message \nOr tell them to send a text to 234********** "
        return 15, data, 'on-going', None

    def ending(self):
        data = {
                'header' :"Almost Done",
                'body':"Any other thing I can assist you with",
                'type':'button'
                }
        interactive = {"buttons": [{
                                "type": "reply",
                                "reply": {
                                    "id": "1",
                                    "title": "Yes!"
                                        }
                                        },
                                {
                                "type": "reply",
                                "reply": {
                                    "id": "0",
                                    "title": "No"
                                }
                                }
                                ]}

        return 26, data, 'on-going', interactive
    def ending_next(self):
        if (str(self.reply)).lower() =='1':
            return self.welcome()
        elif (str(self.reply)).lower() == '0':
            return 26, 'Thank you for shopping with us', 'complete', None
        else:
            return 26, "Didn't quite get you there.", 'on-going', self.ending()