#!/usr/bin/env python3
import unittest
import json
from zendesk_api import ApiCall , ApiQuery , ApiResult
from requests.models import Response
from configurations import Configuration
from tickets_factory import *
from ticket import Ticket


class UnitTests(unittest.TestCase):
    '''Unit Tests class '''

    """  Tests for Api calls and url genaration """

    def test_single_ticket_url(self):
        self.assertEqual(ApiQuery().get_selected_ticket(1),"/api/v2/tickets/1.json")

    def test_list_ticket_url(self):
        self.assertEqual(ApiQuery().get_all(),"/api/v2/tickets.json")

    def test_full_query_single(self):
        self.assertEqual(ApiQuery().get_full_query("/api/v2/tickets/1.json")
        ,Configuration().getDomain()+"/api/v2/tickets/1.json")

    def test_full_query_all(self):
        self.assertEqual(ApiQuery().get_full_query("/api/v2/tickets.json")
        ,Configuration().getDomain()+"/api/v2/tickets.json")

    
    """  Test for responce fails  """

    def test_result_fail(self):

        # generate intended responce object
        expected_response = Response()
        expected_response.code = "expired"
        expected_response.error_type = "expired"
        expected_response.status_code = 400
        expected_response._content = b'{ "error" : "Can not connect to API" }'

        objectified_responce = ApiResult(expected_response)

        # check values of objects are equal
        self.assertEqual(ApiCall().get_result("")
        .error_message,objectified_responce.error_message)
        self.assertEqual(ApiCall().get_result("")
        .result,objectified_responce.result)
        self.assertEqual(ApiCall().get_result("")
        .is_success,objectified_responce.is_success)

    def test_single_ticket_factory_fail(self):

        # genarate intended failed request output ticket
        expected_ticket = Ticket()
        expected_ticket.set_error_message("InvalidEndpoint")

        # check if error messages match
        self.assertEqual(TicketObjectCreator().genarate_ticket("")
        .error_message,expected_ticket.error_message)


    """  Tests for Api Factory methods  """
    
    def test_ticket_factory(self):

        # create a dummy json ticket
        dummy_ticket = '{ "id":1, "type":2, "subject":3, "description":4,\
        "priority":5, "status":6,"recipient":7,"requester_id":8, "assignee_id":9,\
        "created_at":"1111-11-11T11:11:11Z", "updated_at":"2222-11-11T11:11:11Z","due_at":"3333-11-11T11:11:11Z" }'

        # make the dummy a json object
        dummy_json_data = json.loads(dummy_ticket)

        # load dummy data into ticket object
        return_ticket = ObjectFactory().create_ticket_object(dummy_json_data)

        # check expected value form ticket object is equal to dummy data
        self.assertEqual(return_ticket.id,1)
        self.assertEqual(return_ticket.type,2)
        self.assertEqual(return_ticket.subject,3)
        self.assertEqual(return_ticket.description,4)
        self.assertEqual(return_ticket.priority,5)
        self.assertEqual(return_ticket.status,6)
        self.assertEqual(return_ticket.recipient,7)
        self.assertEqual(return_ticket.requester_id,8)
        self.assertEqual(return_ticket.assignee_id,9)
        # these test will work as tests for date simplification methods as well
        self.assertEqual(return_ticket.created_at,"11/11/1111 Time: 11:11:11")
        self.assertEqual(return_ticket.updated_at,"11/11/2222 Time: 11:11:11")
        self.assertEqual(return_ticket.due_at,"11/11/3333 Time: 11:11:11")
        self.assertEqual(return_ticket.error_message,None)

# run tests
if __name__ == '__main__':
	unittest.main()