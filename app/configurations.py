class Configuration:
    # TODO: extract tokens form python module and make it a json file.
    """
    Configuration Class for Api Configuration details.
    You need replace these variables if you want to 
    run form a different account.

    'DOMAIN' = URL of your company
    'USER' = email of your zendesk account
    'TOKEN' = Your active zendesk api token  
    """

    DOMAIN = 'https://interntest.zendesk.com'
    USER = ''
    TOKEN = ''

    def get_user_id(self):
        return self.USER

    def get_token(self):
        return self.TOKEN

    def get_domain(self):
        return self.DOMAIN
