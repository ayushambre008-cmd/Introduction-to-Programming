# ==========================================
#       BUS TICKET BOOKING SYSTEM
# ==========================================

print("==========================================")
print("        BUS TICKET BOOKING SYSTEM")
print("==========================================")

name = input("Enter Passenger Name: ")

print("\nAvailable Destinations:")
print("1.  Mumbai to Pune        - Rs. 1000")
print("2.  Mumbai to Nashik      - Rs. 900")
print("3.  Mumbai to Surat       - Rs. 1300")
print("4.  Mumbai to Goa         - Rs. 2200")
print("5.  Mumbai to Ahmedabad   - Rs. 1500")
print("6.  Mumbai to Nagpur      - Rs. 2000")
print("7.  Mumbai to Kolhapur    - Rs. 1400")
print("8.  Mumbai to Aurangabad  - Rs. 1200")
print("9.  Mumbai to Bengaluru   - Rs. 3000")
print("10. Mumbai to Hyderabad   - Rs. 2700")

total_fare = 0
bookings = []

while True:

    choice = int(input("\nEnter destination choice (1-10): "))

    if choice == 1:
        destination = "Mumbai to Pune"
        fare = 1000

    elif choice == 2:
        destination = "Mumbai to Nashik"
        fare = 900

    elif choice == 3:
        destination = "Mumbai to Surat"
        fare = 1300

    elif choice == 4:
        destination = "Mumbai to Goa"
        fare = 2200

    elif choice == 5:
        destination = "Mumbai to Ahmedabad"
        fare = 1500

    elif choice == 6:
        destination = "Mumbai to Nagpur"
        fare = 2000

    elif choice == 7:
        destination = "Mumbai to Kolhapur"
        fare = 1400

    elif choice == 8:
        destination = "Mumbai to Aurangabad"
        fare = 1200

    elif choice == 9:
        destination = "Mumbai to Bengaluru"
        fare = 3000

    elif choice == 10:
        destination = "Mumbai to Hyderabad"
        fare = 2700

    else:
        print("Invalid destination!")
        continue

    seats = int(input("Enter number of seats: "))

    if seats <= 0:
        print("Invalid number of seats!")
        continue

    amount = fare * seats
    total_fare = total_fare + amount

    bookings.append((destination, seats, amount))

    more = input("\nDo you want to add another destination? (yes/no): ")

    if more.lower() != "yes":
        break


# ==========================================
#              TICKET
# ==========================================

print("\n==========================================")
print("             BUS TICKET")
print("==========================================")

print("Passenger Name :", name)
print("------------------------------------------")

for booking in bookings:
    print("Destination    :", booking[0])
    print("Seats Booked   :", booking[1])
    print("Fare           : Rs.", booking[2])
    print("------------------------------------------")

print("TOTAL FARE     : Rs.", total_fare)

print("==========================================")
print("       BOOKING CONFIRMED!")
print("       Thank you for travelling!")
print("==========================================")
