def main():
    #Ask user for mass in kilograms
    mass=int(input("What is a mass in kilograms? : "))

    #define function that calculates energy in joules
    def joules(n):
        return mass*90000000000000000
    #print the result
    print(joules(mass))
main()
