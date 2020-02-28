number_one, number_two, number_three, = int(input().strip()), int(input().strip()), int(input().strip())

if number_one > number_two and number_one > number_three:
    print("{} is the largest of the three numbers.".format(number_one))
elif number_two > number_one and number_two > number_three:
    print("{} is the largest of the three numbers.".format(number_two))
else:
    print("{} is the largest of the three numbers.".format(number_three))
