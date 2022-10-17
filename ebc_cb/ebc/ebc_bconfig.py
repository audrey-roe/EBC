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
                        'type':'list'
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
              "title": "📲 Quit",
              "description": "Exit the chatbot"
            },
          ]
        }
      ]
        }
        
        return 1, welcome_string, 'on-going', interactive

    def welcome_next(self):
        if (str(self.reply)).lower() =='1':
            return self.check_balance()
        elif (str(self.reply)).lower() =='2':
            return self.my_offers()
        elif (str(self.reply)).lower() =='3':
            return self.borrow_airtime_data()
        elif (str(self.reply)).lower() == '4':
            return self.social_plans()
        elif (str(self.reply)).lower() == '5':
            return self.data_plans()
        elif (str(self.reply)).lower() == '6':
            return self.faq()
        elif (str(self.reply)).lower() == '7':
            return self.chat_agent()
        elif (str(self.reply)).lower() == '8':
            return self.share_bot()
        else:
            return 1, 'I do not understand you.\nPlease kindly type in the corresponding number to the question or the option.', 'on-going', None
    
    def catalogue(self):
        pass

    def catalogueNext(self):
        pass

    def my_offers_next(self):
        pass