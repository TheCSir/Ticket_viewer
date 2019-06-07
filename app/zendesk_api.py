import requests
from requests.models import Response
from configurations import Configuration


class ApiCall:
    """ This class define the API calls of given query """

    @staticmethod
    def get_result(query):
        """
        Execute the Query using python requests library.
        Args:
            query: String, which is the api query to be executed.

        Returns:
        response: ApiResult,
            which contains json output and output status variables.
        """

        # get credentials form file
        user = Configuration().get_user_id()
        token = Configuration().get_token()
        try:
            result = requests.get(query, auth=(user, token))
        except requests.exceptions.RequestException:
            # manually generate a response object
            the_response = Response()
            the_response.code = "expired"
            the_response.error_type = "expired"
            the_response.status_code = 400
            the_response._content = b'{ "error" : \
            " Can not connect to Zendesk API at the moment" }'
            result = the_response

        # get results stored in ApiResult object
        response = ApiResult(result)

        return response


class ApiResult:
    """ This class define the result status of a query """

    def __init__(self, response):
        """
        Setup status variables to a given API response.

        Args:
            response: Object, response from requests library.

        variables:
            result: Object, response from requests library.
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

    @staticmethod
    def get_all():
        """
        Returns:
            String: URL string to get all tickets.
            ( this is specified in zendesk API documentation )
        """

        return "/api/v2/tickets.json"

    @staticmethod
    def get_selected_ticket(id):
        """
        Returns:
            String: URL string to get a specific ticket.
            ( this is specified in zendesk API documentation )
        """

        return "/api/v2/tickets/{ticket_id}.json".format(ticket_id=id)

    @staticmethod
    def get_full_query(url):
        """
        Returns:
            String: full query string to feed into API call.
            ( this is specified in zendesk API documentation )
        """

        query = Configuration().get_domain() + url
        return query
