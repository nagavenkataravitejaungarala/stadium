import streamlit as st

class CricketStadium:
    def __init__(self, capacity):
        self.capacity = capacity
        self.booking_list = [0] * capacity

    def book_seat(self, seat_number):
        if self.booking_list[seat_number-1] == 0:
            self.booking_list[seat_number-1] = 1
            st.success(f"Seat {seat_number} booked successfully!")
        else:
            st.warning(f"Seat {seat_number} is already booked.")

    def cancel_seat(self, seat_number):
        if self.booking_list[seat_number-1] == 1:
            self.booking_list[seat_number-1] = 0
            st.success(f"Seat {seat_number} cancelled successfully!")
        else:
            st.warning(f"Seat {seat_number} is not booked.")

    def view_availability(self):
        st.write("Current seat availability:")
        for i, status in enumerate(self.booking_list):
            seat_number = i + 1
            if status == 0:
                st.write(f"Seat {seat_number}: Available")
            else:
                st.write(f"Seat {seat_number}: Booked")

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
