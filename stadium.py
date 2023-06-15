import streamlit as st

class CricketStadium:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stadium_list = [{'seat_number': i+1, 'status': 'Available'} for i in range(capacity)]
        self.order_data = []

    def book_seat(self, seat_number):
        seat = self.stadium_list[seat_number-1]
        if seat['status'] == 'Available':
            seat['status'] = 'Booked'
            self.order_data.append(seat)
            st.success(f"Seat {seat_number} booked successfully!")
        else:
            st.warning(f"Seat {seat_number} is already booked.")

    def cancel_seat(self, seat_number):
        seat = self.stadium_list[seat_number-1]
        if seat['status'] == 'Booked':
            seat['status'] = 'Available'
            self.order_data = [order for order in self.order_data if order['seat_number'] != seat_number]
            st.success(f"Seat {seat_number} cancelled successfully!")
        else:
            st.warning(f"Seat {seat_number} is not booked.")

    def view_availability(self):
        available_seats = []
        booked_seats = []

        for seat in self.stadium_list:
            if seat['status'] == 'Available':
                available_seats.append(seat['seat_number'])
            elif seat['status'] == 'Booked':
                booked_seats.append(seat['seat_number'])

        st.write("Current seat availability:")
        st.write(f"Available seats: {available_seats}")
        st.write(f"Booked seats: {booked_seats}")

        st.write("\nOrder data:")
        if self.order_data:
            for order in self.order_data:
                st.write(f"Seat {order['seat_number']} is booked.")
        else:
            st.write("No seat has been booked yet.")

# Creating an instance of the CricketStadium
stadium = CricketStadium(capacity=50)

# Streamlit app
def main():
    st.title("Online Cricket Stadium Booking")

    menu = ["Book Seat", "Cancel Seat", "View Availability"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Book Seat":
        seat_number = st.number_input("Enter seat number", min_value=1, max_value=stadium.capacity, step=1)
        if st.button("Book"):
            stadium.book_seat(seat_number)

    elif choice == "Cancel Seat":
        seat_number = st.number_input("Enter seat number", min_value=1, max_value=stadium.capacity, step=1)
        if st.button("Cancel"):
            stadium.cancel_seat(seat_number)

    elif choice == "View Availability":
        stadium.view_availability()

if __name__ == '__main__':
    main()
