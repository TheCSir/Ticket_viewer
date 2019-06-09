class Configuration:
    # TODO: extract tokens form python module to a json file.
    """
    Configuration Class for Api Configuration details.
    You need replace these variables if you want to 
    run form a different account.

    'DOMAIN' = URL of your company
    'USER' = email of your zendesk account
    'TOKEN' = Your active zendesk api token

    You need to change API result url if Zendesk API change in future
    current implementation is from 10/06/2019

    'ALL_TICKET_JSON' = URL for all ticket result
    'SELECTED_TICKET_JSON' = URL for single ticket json
    """

    DOMAIN = 'https://interntest.zendesk.com'
    USER = '{Your email here}/token'
    TOKEN = '{Your token here}'

    ALL_TICKET_JSON = '/api/v2/tickets.json'
    SELECTED_TICKET_JSON = '/api/v2/tickets/'  # add {id}.json to the end

    def get_user_id(self):
        return self.USER

    def get_token(self):
        return self.TOKEN

    def get_domain(self):
        return self.DOMAIN

    def get_all_ticket_url(self):
        return self.ALL_TICKET_JSON

    def get_single_ticket_url(self):
        return self.SELECTED_TICKET_JSON
