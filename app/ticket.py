class Ticket:
    """ 
    Ticket Class defines the ticket object.
    THis class contains initial parameters for a ticket
    and series of setters for the object.

    'id'        =	integer,Ticket id
    'type'      =	string, the type of this ticket.
    'subject'   =	string, The subject field for this ticket.
    'description'=  string, The first comment on the ticket.
    'priority'  =	string, The urgency of the ticket.
    'status'    =   string, The state of the ticket.
    'recipient'	=   string,	The recipient e-mail address.
    'requester_id'=	integer,The user who requested this ticket.
    'assignee_id'=	integer,The agent currently assigned to the ticket.
    'created_at'=   date,   When this record was created.
    'updated_at'=	date,   When this record last got updated.
    'due_at'    =	date,   When this ticket is due.
    'error_message'=string, Reason of object not creating.
    """

    def __init__(self):
        self.id = None
        self.type = 'Not Available'
        self.subject = 'Not Available'
        self.description = 'Not Available'
        self.priority = 'Not Available'
        self.status = 'Not Available'
        self.recipient = 'Not Available'
        self.requester_id = 'Not Available'
        self.assignee_id = 'Not Available'
        self.created_at = 'Not Available'
        self.updated_at = 'Not Available'
        self.due_at = 'Not Available'
        self.error_message = None
