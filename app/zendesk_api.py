import requests
from configurations import Configuration

class ApiCall:
    ''' This class define the API calls of given query ''' 

    def get_result(self, query):
        """
        Execute the Query using python requests library.

	    Args:
	        query: String, which is the api query to be executed.

	    Returns:
	        responce: ApiResult,
            which contains json output and output status variables.
        """

        # get credentials form file
        user = Configuration().getUserID()
        token = Configuration().getToken()
        result = requests.get(query, auth=(user,token))
        responce = ApiResult(result)

        return responce


class ApiResult:
    ''' This class define the result status of a query '''

    def __init__(self,response):
        """
        Setup status variables to a given API response.

	    Args:
	        response: Object, responce from requests library.

	    variables:
	        result: Object, responce from requests library.
            is_success: Boolean, did query result in success.
            error_message: string, error message from request.
        """

        self.result = response.json()
        self.is_success = False
        self.error_message = None

        if response:
            self.is_success = True

        else:
            self.error_message = self.result['error']


class ApiQuery:
    ''' This class define the types of queries '''

    def get_all(self):
        """
        Returns:
	        String: URL string to get all tickets.
            ( this is specified in zendesk API documentation )
        """

        return "/api/v2/tickets.json"

    def get_selected_ticket(self, id):
        """
        Returns:
	        String: URL string to get a specific ticket.
            ( this is specified in zendesk API documentation )
        """
        
        return "/api/v2/tickets/{ticket_id}.json".format(ticket_id = id)

    def get_full_query(self, url):
        """
        Returns:
	        String: full query string to feed into API call.
            ( this is specified in zendesk API documentation )
        """

        query = Configuration().getDomain() + url
        return query








