# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class ElectricCar:                                  # Create a class name ElectricCar
    def __init__(self,v,e,c):                       # Initialize input variables using Constructor
        self.V = v
        self.E = e
        self.C = c

    def min_stops(self):                            # Function for calculating to minimized the no.of stops
        cities = []
        for i in range(len(self.E)):
            if self.E[i]==0:
                return "Distance Cannot be Zero"
            elif self.C<250 or self.C>350:
                return "Capacity Should be Considered in between 250 to 300."
            elif self.E[i]>self.C:
                return "Car will break down while going from {} to {}".format(self.V[i],self.V[i+1])
            elif self.E[i]<10 or self.E[i]>self.c//2:
                return "Distance should be between 10 to C/2."
        cities.append(self.V[0])
        dist = self.E[0]
        i = 1
        while i<len(self.E):
            if self.E[i]<300:                              # Testing Corner Cases after each refill
                if (dist+2*self.E[i])<=self.C:
                    dist += self.E[i]
                    i+=1
                else:
                    cities.append(self.V[i])
                    dist = 0
                    self.C = c
            else:
                print("Car will break down while going from {} to {}".format(self.V[i],self.V[i+1]))
        cities.append(self.V[i])
        return cities


    def display(self):                              # Function to display vertices and edges
        print(self.V)
        print(self.E)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())                            # Take total number of test cases
    while n:
        v = list(map(str,input().split()))      # Take vertices from user
        e = list(map(int,input().split()))      # Take edges from user
        c = int(input())                        # Take Capacity from user
        ec = ElectricCar(v,e,c)                 # Object Created and passed three arguments
        ec.display()                            # Displayed the vertices and edges
        sol = ec.min_stops()                    # Call the calculating function
        print(sol)                              # print solution
        n-=1                                    # Decrement the n

