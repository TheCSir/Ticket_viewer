from zendesk_api import ApiCall , ApiQuery , ApiResult
from ticket import Ticket
import datetime

class TicketObjectCreator:
    ''' This class define methods of creating different
        types of ticket object(s) '''

    def genarate_ticket(self, id):
        """
        genarate a ticket object form a API results 
        by calling Object factory.

	    Args:
	        id: Integer, ID of the selected ticket.

	    Returns:
	        ticket: Ticket object, which contains ticket data
            if error:
                returns a default ticket with Error message assigned.
        """

        # get query genarated by zendesk_api.py methods
        url = ApiQuery().get_selected_ticket(id)
        query = ApiQuery().get_full_query(url)
        responce = ApiCall().get_result(query)

        if responce.is_success:
            result_data = responce.result
            ticket_data = result_data['ticket']
            factory = ObjectFactory()
            ticket = factory.create_ticket_object(ticket_data)
        else:
            ticket = Ticket()
            ticket.set_error_message(responce.error_message)

        return ticket

    def genarate_ticket_list(self):
        """
        genarate a ticket list form a API results 
        by calling Object factory.

	    Returns:
	        tickets: list of Ticket objects, which contains ticket data
            if error:
                returns a default ticket with Error message assigned.
        """

        # get query genarated by zendesk_api.py methods
        url = ApiQuery().get_all()
        query = ApiQuery().get_full_query(url)
        responce = ApiCall().get_result(query)
        tickets = []

        # loop while result do not have more pages
        # happens when json result have more than 100 tickets
        while True:
            if responce.is_success:

                result_data = responce.result
                ticket_data = result_data['tickets']

                for current_ticket in ticket_data:
                    factory = ObjectFactory()
                    ticket = factory.create_ticket_object(current_ticket)
                    tickets.append(ticket)
                if result_data['next_page']:
                    query = result_data['next_page']
                    responce = ApiCall().get_result(query)

                else:
                    break
                    
            else:
                tickets.clear()
                ticket = Ticket()
                ticket.set_error_message(responce.error_message)
                tickets.append(ticket)
                break
        

        return tickets



class ObjectFactory:
    ''' This class create required objects form given input '''

    def create_ticket_object(self, json_ticket):
        """
        Create a ticket object using json input.

	    Args:
	        json_ticket: json object, json ticket details.

	    Returns:
	        ticket: Ticket, a ticket object from Ticket class.
        """

        ticket = Ticket()
        ticket.set_id(json_ticket['id'])

        if json_ticket['type']:
            ticket.set_type(json_ticket['type'])

        if json_ticket['subject']:
            ticket.set_subject(json_ticket['subject'])

        if json_ticket['description']:
            ticket.set_description(json_ticket['description'])

        if json_ticket['priority']:
            ticket.set_priority(json_ticket['priority'])

        if json_ticket['status']:
            ticket.set_status(json_ticket['status'])

        if json_ticket['recipient']:
            ticket.set_recipient(json_ticket['recipient'])

        if json_ticket['requester_id']:
            ticket.set_requester_id(json_ticket['requester_id'])

        if json_ticket['assignee_id']:
            ticket.set_assignee_id(json_ticket['assignee_id'])

        if json_ticket['created_at']:
            ticket.set_created_at(self.get_date(json_ticket['created_at']))

        if json_ticket['updated_at']:
            ticket.set_updated_at(self.get_date(json_ticket['updated_at']))
            
        if json_ticket['due_at']:
            ticket.set_due_at(self.get_date(json_ticket['due_at']))

        return ticket
        

    def get_date(self, date):
        """ Helper function to change json date to readable date.
            this function convert 
            '2019-01-02T01:02:03Z' to  'Date: 02/01/2019 Time:01:02:03'

	    Args:
	        date: Json date

	    Returns:
            str_date: string, readable date time string
	    """

        # crete a dateobject by using library
        date_object = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')

        # farmat a string with above date object
        readable_date = "{D}/{M}/{Y} Time: {h}:{m}:{s}" \
        .format(D=date_object.day, M=date_object.month, Y=date_object.year,
        h=date_object.hour,m=date_object.minute,s=date_object.second)

        return readable_date

