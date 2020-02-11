# number_one = int(input("Enter the first number: ").strip())
# number_two = int(input("Enter the second number: ").strip())

number_one, number_two = map(int, input("Enter the two numbers: ").split())

print("The sum of the two number {} and {} is {}".format(number_one, number_two, number_one + number_two))
print("The difference of the two number {} and {} is {}".format(number_one, number_two, number_one - number_two))
print("The product of the two number {} and {} is {}".format(number_one, number_two, number_one * number_two))
print("The division of the two number {} and {} is {}".format(number_one, number_two, number_one / number_two))
