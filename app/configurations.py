class Configuration:
	""" 
    Configuration Class for Api Configuration details.
    You need replace these variables if you want to 
    run form a different account.

    'DOMAIN' = URL of your company
    'USER' = email of your zendesk account
    'TOKEN' = Your active zendesk api token  
    """

	DOMAIN = 'https://interntest.zendesk.com'
	USER = 'shehanchathura@gmail.com/token'
	TOKEN = '2B4O0mN5Ya3zkHLNHfw4gIQcc4w8tdqWm9PUJSGh'

	def getUserID(self):
		return self.USER

	def getToken(self):
		return self.TOKEN

	def getDomain(self):
		return self.DOMAIN