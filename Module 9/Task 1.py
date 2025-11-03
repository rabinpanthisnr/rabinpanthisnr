class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

def main():
    # Create a new car
    car = Car("ABC-123", 142)

    print(f"Registration Number: {car.registration_number}")
    print(f"Maximum Speed: {car.max_speed} km/h")
    print(f"Current Speed: {car.current_speed} km/h")
    print(f"Travelled Distance: {car.travelled_distance} km")

if __name__ == "__main__":
    main()
