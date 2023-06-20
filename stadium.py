# Import streamlit
import streamlit as st

# Define a list of stadiums
stadiums = ["Wankhede Stadium", "Eden Gardens", "M. Chinnaswamy Stadium", "Feroz Shah Kotla Ground", "M. A. Chidambaram Stadium"]

# Define a dictionary of tickets available for each stadium
tickets = {"Wankhede Stadium": 1000, "Eden Gardens": 1500, "M. Chinnaswamy Stadium": 1200, "Feroz Shah Kotla Ground": 800, "M. A. Chidambaram Stadium": 900}

# Define a dictionary of seats available for each stadium
seats = {"Wankhede Stadium": ["A1", "A2", "A3", ...], # Add more seats as needed
         "Eden Gardens": ["B1", "B2", "B3", ...],
         "M. Chinnaswamy Stadium": ["C1", "C2", "C3", ...],
         "Feroz Shah Kotla Ground": ["D1", "D2", "D3", ...],
         "M. A. Chidambaram Stadium": ["E1", "E2", "E3", ...]}

# Define a dictionary of booked tickets for each user
booked_tickets = {}

# Define a function to display the stadium list and the tickets available
def display_stadiums():
    st.title("Welcome to online cricket ticket booking!")
    st.subheader("Here are the stadiums and the tickets available:")
    for stadium in stadiums:
        st.write(stadium + ": " + str(tickets[stadium]) + " tickets")

# Define a function to book tickets for a given stadium and number of tickets
def book_tickets(stadium, num_tickets):
    # Check if the stadium is valid
    if stadium not in stadiums:
        st.error("Invalid stadium name. Please try again.")
        return
    # Check if the number of tickets is valid
    if num_tickets <= 0:
        st.error("Invalid number of tickets. Please try again.")
        return
    # Check if there are enough tickets available
    if num_tickets > tickets[stadium]:
        st.error("Sorry, there are not enough tickets available for " + stadium + ". Please try again.")
        return
    # Book the tickets and update the dictionary
    tickets[stadium] -= num_tickets
    st.success("You have successfully booked " + str(num_tickets) + " tickets for " + stadium + ".")
    # Ask the user to choose the seats
    chosen_seats = []
    for i in range(num_tickets):
        seat = st.selectbox("Choose a seat for ticket #" + str(i+1) + ": ", seats[stadium])
        # Check if the seat is valid and available
        if seat not in seats[stadium]:
            st.error("Invalid seat name. Please try again.")
            return
        if seat in chosen_seats:
            st.error("Seat already chosen. Please try again.")
            return
        # Add the seat to the chosen seats list
        chosen_seats.append(seat)
    # Update the seats dictionary and remove the chosen seats
    for seat in chosen_seats:
        seats[stadium].remove(seat)
    # Update the booked tickets dictionary and add the chosen seats
    booked_tickets[stadium] = chosen_seats
    st.success("You have successfully chosen the seats: " + ", ".join(chosen_seats) + ". Enjoy the match!")

# Define a function to cancel tickets for a given stadium and number of tickets
def cancel_tickets(stadium, num_tickets):
    # Check if the stadium is valid
    if stadium not in stadiums:
        st.error("Invalid stadium name. Please try again.")
        return
    # Check if the number of tickets is valid
    if num_tickets <= 0:
        st.error("Invalid number of tickets. Please try again.")
        return
    # Check if the user has booked any tickets for that stadium
    if stadium not in booked_tickets:
        st.error("You have not booked any tickets for " + stadium + ". Please try again.")
        return
    # Check if the user has enough tickets to cancel
    if num_tickets > len(booked_tickets[stadium]):
        st.error("You have only booked " + str(len(booked_tickets[stadium])) + " tickets for " + stadium + ". Please try again.")
        return
    # Cancel the tickets and update the dictionary
    tickets[stadium] += num_tickets
    st.success("You have successfully cancelled " + str(num_tickets) + " tickets for " + stadium + ".")
    # Ask the user to choose the seats to cancel
    cancelled_seats = []
    for i in range(num_tickets):
        seat = st.selectbox("Choose a seat to cancel for ticket #" + str(i+1) + ": ", booked_tickets[stadium])
        # Check if the seat is valid and booked
        if seat not in booked_tickets[stadium]:
            st.error("Invalid seat name. Please try again.")
            return
        if seat in cancelled_seats:
            st.error("Seat already cancelled. Please try again.")
            return
        # Add the seat to the cancelled seats list
        cancelled_seats.append(seat)
    # Update the seats dictionary and add the cancelled seats
    for seat in cancelled_seats:
        seats[stadium].append(seat)
    # Update the booked tickets dictionary and remove the cancelled seats
    for seat in cancelled_seats:
        booked_tickets[stadium].remove(seat)
    st.success("You have successfully cancelled the seats: " + ", ".join(cancelled_seats) + ". We hope to see you again!")

# Display the stadium list and the tickets available
display_stadiums()

# Ask the user to enter their choice of action: book, cancel or exit
choice = st.sidebar.radio("Enter your choice of action: ", ["book", "cancel", "exit"])

# Perform the action based on the user's choice
if choice == "book":
    # Ask the user to enter the stadium name and the number of tickets they want to book
    stadium = st.sidebar.selectbox("Enter the stadium name: ", stadiums)
    num_tickets = st.sidebar.number_input("Enter the number of tickets: ", min_value=1, max_value=tickets[stadium])
    # Book the tickets for the user
    book_tickets(stadium, num_tickets)
elif choice == "cancel":
    # Ask the user to enter the stadium name and the number of tickets they want to cancel
    stadium = st.sidebar.selectbox("Enter the stadium name: ", stadiums)
    num_tickets = st.sidebar.number_input("Enter the number of tickets: ", min_value=1, max_value=len(booked_tickets.get(stadium, [])))
    # Cancel the tickets for the user
    cancel_tickets(stadium, num_tickets)
elif choice == "exit":
    # Exit the program
    st.write("Thank you for using online cricket ticket booking. Have a nice day!")
