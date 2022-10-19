import requests
from .models import payment, product, cart, customer

class whatsappbot():    
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.reply = kwargs.get('reply', None)

    def message_call(self):
        if self.id == 0:
            id, response, status, interactive = self.welcome()#self.cart()
            return id, response, status, interactive
        elif self.id == 1:
            id, response, status, interactive = self.welcome_next()
            return id, response, status, interactive
        elif self.id == 2:
            id, response, status, interactive = self.catalogueNext()
            return id, response, status, interactive
        elif self.id == 3:
            id, response, status, interactive = self.discounts_next()
            return id, response, status, interactive    
        elif self.id == 4:
            id, response, status, interactive = self.place_order_next()
            return id, response, status, interactive
        elif self.id == 5:
            id, response, status, interactive = self.news_letter_next()
            return id, response, status, interactive
        elif self.id == 6:
            id, response, status, interactive = self.ending_next()
            return id, response, status, interactive
        elif self.id == 7:
            id, response, status, interactive = self.confirm_email_next()
            return id, response, status, interactive
        elif self.id == 8:
            id, response, status, interactive = self.add_to_cart_next()
            return id, response, status, interactive
        elif self.id == 9:
            id, response, status, interactive = self.add_to_cart_next_next_next()
            return id, response, status, interactive
        elif self.id == 10:
            id, response, status, interactive = self.details_next()
            return id, response, status, interactive
        elif self.id == 11:
            id, response, status, interactive = self.add_customer_initiate()
            return id, response, status, interactive
        elif self.id == 12:
            id, response, status, interactive = self.add_customer_next_email()
            return id, response, status, interactive
        elif self.id == 13:
            id, response, status, interactive = self.add_customer_next_address()
            return id, response, status, interactive
        elif self.id == 14:
            id, response, status, interactive = self.confirm_details()
            return id, response, status, interactive
        elif self.id == 15:
            id, response, status, interactive = self.confirm_details_next()
            return id, response, status, interactive

    def cart(self):
        for products in product.objects.all():
            if products.id == self.reply:
                return self.add_to_cart()
        return self.welcome()

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
           
            "header": {
                "type": "interactive",
                "text": "Catalogue"
            },
            "type": "product_list",

            "body":{
                "text": "Explore our fine range of coffee accessories"
            },
            "footer":{
                "text": "Everything But Coffee"
            },
            }
        interactive = {
                    
                     "catalog_id":"1239386806600403",
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
                        
        return 2, data, 'on-going', interactive
                              

    def catalogueNext(self):
        pass

    def discounts(self):
        data = {
            "header": {
                "type": "interactive",
                "text": "Catalogue"
            },
            "type": "product_list",
            "body": {
                "text": "Explore our fine range of coffee accessories",
            },  
            "footer":{
                "text": "Everything But Coffee On Sale!"
            },
            
        }
        interactive = {
                   "catalog_id" : "1239386806600403",
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
                        
        return 2, data, 'on-going', interactive                          

    def purchase(self):
        pass
    
    def post_purchase(self):

        pass

    def add_to_cart(self):
        if not customer.objects.get(customer_no = self.number).customer_email == 'none':
            cart.objects.create(customer = customer.objects.get(customer_no = self.number), product = product.objects.get(id = self.reply)).save()
            data = {
                    'header' :"ADD ITEM TO CART",
                    'body': f"Do you want to add the item with product ID: {str(product.objects.get(id = self.reply))} to your cart.",
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
            return 8, data, 'on-going', interactive
        else:
            cart.objects.create(customer = customer.objects.get(customer_no = self.number), product = product.objects.get(id = self.reply)).save()
            data = {
                    'header' :"Add item to cart",
                    'body': f"To add the item: {str(product.objects.get(id = self.reply))} to your cart you need to Sign Up.",
                    'type':'button'
                    }
            interactive = {"buttons": [{
                                    "type": "reply",
                                    "reply": {
                                        "id": "1",
                                        "title": "Sign Up"
                                            }
                                            },
                                    {
                                    "type": "reply",
                                    "reply": {
                                        "id": "0",
                                        "title": "Delete Cart"
                                    }
                                    }
                                    ]}
            return 11, data, 'on-going', interactive

    def add_customer_initiate(self):
        if (str(self.reply)).lower() =='1':
            return self.add_customer()
        elif (str(self.reply)).lower() == '0':
            cart.objects.filter(customer = customer.objects.get(customer_no = self.number)).last().delete            
            return self.welcome()

    def add_customer(self):
        data = f'Please provide all the information and your details will be linked to this number {self.number}.\n Can I get your full name?'
        return 12, data, 'on-going', None

    def add_customer_next_email(self):
        data = f"Your email?"
        change = customer.objects.get(customer_no = self.number)
        change.customer_name = self.reply
        change.save()
        return 13, data,  'on-going', None
    
    def add_customer_next_address(self):
        data = f"One last thing, can I get your address too?"
        change = customer.objects.get(customer_no = self.number)
        change.customer_email = self.reply
        change.save()
        return 14, data,  'on-going', None

    def confirm_details(self):
        change = customer.objects.get(customer_no = self.number)
        change.customer_address = self.reply
        change.save()
        data = {
            'header':'Confirm details',
            'body':f'Wonderful! Please can you confirm the details listed below are correct.\n name: {change.customer_name}.\n email: {change.customer_email}.\n number: {change.customer_no}.\n address: {change.customer_address}',
            'type':'button'
            }
        interactive = {"buttons": [{
                                "type": "reply",
                                "reply": {
                                    "id": "1",
                                    "title": "Confirm"
                                        }
                                        },
                                {
                                "type": "reply",
                                "reply": {
                                    "id": "0",
                                    "title": "Change"
                                }
                                }
                                ]}
        return 15, data,  'on-going', interactive

    def confirm_details_next(self):
        if (str(self.reply)).lower() =='1':
            return self.add_to_cart_next_next()
        elif (str(self.reply)).lower() == '0':
            cart.objects.filter(customer = customer.objects.get(customer_no = self.number)).last().delete            
            return self.add_customer()

    def add_to_cart_next(self):
        if (str(self.reply)).lower() =='1':
            return self.add_to_cart_next_next()
        elif (str(self.reply)).lower() == '0':
            cart.objects.filter(customer = customer.objects.get(customer_no = self.number)).last().delete            
            return self.welcome()

    def add_to_cart_next_next(self):
        data = {
                'header' :"Order now",
                'body': "Complete your order or continue shopping.",
                'type':'button'
                }
        interactive = {"buttons": [{
                                "type": "reply",
                                "reply": {
                                    "id": "1",
                                    "title": "Complete order"
                                        }
                                        },
                                {
                                "type": "reply",
                                "reply": {
                                    "id": "0",
                                    "title": "Continue spending"
                                }
                                }
                                ]}
        return 9, data, 'on-going', interactive
    
    def add_to_cart_next_next_next(self):
        payment.objects.create(customer = customer.objects.get(customer_no = self.number))
        if (str(self.reply)).lower() =='1':
            auth_pay = "sk_live_c8b29dedc59450ce1837b29c5ffe687b62c275ea"
            cust = payment.objects.filter(customer = customer.objects.get(customer_no = self.number)).last()
            datum = requests.request('post', 'https://api.paystack.co/transaction/initialize', headers = {"Authorization": f"Bearer {auth_pay}","Content-Type" : "application/json"}, json={"email": cust.customer.customer_email, "amount": cust.total_amount})
            link = datum.json()['data']['authorization_url']
            data = f"You're buying items:{cust.items} at the price of ₦{str(int(cust.total_price)/100)} .\npayment link: {link}.\n Please type done when you have completed the transaction "
            return 10, data, "on-going", None

        elif (str(self.reply)).lower() == '0':
            return self.browse_catalogue()
    
    def details_next(self):
        data = {
                'header' :"Almost Done",
                'body':"Hooray you have completed the transaction.\n We will update you here on the progress of your purchase.\n Is there any other thing I can assist you with?",
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
        return 6, data, 'on-going', interactive

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