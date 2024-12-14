# Write your program here
# This program calculates the kinetic energy of a moving object whatever that means

mass = float(input("Enter the mass: "))
velocity = float(input("Enter the velocity: "))

momentum = mass * velocity
kinetic_energy = (1 / 2) * mass * (velocity ** 2)

print("The kinetic energy is", kinetic_energy)
print("The momentum is", momentum)