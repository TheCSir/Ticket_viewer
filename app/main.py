from flask import Flask, render_template
from tickets_factory import TicketObjectCreator
from flask_assets import Bundle, Environment

app = Flask(__name__)

@app.route('/index/<int:page_no>')
@app.route('/index/')
def index(page_no=1):
    """
	This will render ticket list.

	Args:
	    page_no: Integer, ID of the page.

	Returns:
	    data for Html template for displaying the ticket.
    """
    # generate ticket object
    oc = TicketObjectCreator()
    tickets = oc.genarate_ticket_list()

    # placeholder for next and previous button visibility
    is_next = True
    is_previous = True

    # value of number of results in a page 
    no_of_tickets = 25
    tickets_found = True

    # check if data received 
    if tickets[0].error_message:
        tickets_found = False
        is_next = False
        is_previous= False
	
    # set start and end index of ticketlist 
    start_ticket = 0 if page_no == 1 else no_of_tickets * (page_no - 1)
    end_ticket = start_ticket+no_of_tickets

	# if first page
    if start_ticket == 0:
        is_previous = False

    # if last page
    if end_ticket >= len(tickets):
        end_ticket = len(tickets)
        no_of_tickets = end_ticket - start_ticket
        is_next = False

    if not tickets_found:
        return render_template('ticketlist.html', tickets_found=tickets_found,ticket_list=tickets)
    else:

        return render_template('ticketlist.html', 
        ticket_list=tickets[start_ticket:end_ticket],tickets_found=tickets_found,
        current_page = page_no,is_next=is_next,is_previous=is_previous, ticket_count=len(tickets) ,
        no_of_tickets=no_of_tickets)

@app.route('/ticket/<int:ticket_id>')
def disply_selected_ticket(ticket_id):
	"""
	This will render a single.

	Args:
	    ticket_id: Integer, ID of the ticket to be displayed.

	Returns:
	    data for Html template for displaying the ticket.
    """

    # generate ticket object
	oc = TicketObjectCreator()
	ticket = oc.genarate_ticket(ticket_id)

    # check if data received 
	if(ticket.id):
		ticket_found = True
	else:
		ticket_found = False

	return render_template('ticket.html', ticket=ticket, ticket_found=ticket_found)



if __name__ == "__main__":
	app.run(debug=True)