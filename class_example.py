class Distance():
    def get_distance(self):
        self.distance=int(input("Enter the distance:"))

    def print_distance(self):
        print("The distance is :",self.distance)

d1=Distance()
d1.get_distance()
d1.print_distance()