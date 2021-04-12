DB Tables
--------
vehicle_master
	id , type ,max_persons
vehicles
	id , type (FK vehicle_master.id) , name , 
	
customers
	id , name , ssn , address(can be a diff table if multiple addresses are stored)
	
Bookings
	id , customer(FK customer.id) , vehicle_id(FK vehicles.id) , date_of_hire , date_of_return , invoice_id(FK invoice.id) , letter_sent , date_of_booking
	
Invoices
	id , customer(FK cuetomer.id), amount , payment_method , invoice_date
 
