### Create a Random Password Generator that generate 15 digit random password.
import random
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

random_password=random.shuffle(numbers)
random_password=numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]+numbers[5]+numbers[6]+numbers[7]+numbers[8]+numbers[9]+numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]
print(f"Random password is  {random_password}")