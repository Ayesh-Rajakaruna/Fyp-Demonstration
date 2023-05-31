import random

def generate_random_integer(start, end):
    return random.randint(start, end)

def decimal_to_binary(decimal, num_digits):
    binary = bin(decimal)[2:] 
    binary = str(binary.zfill(num_digits))
    return binary

def choose_random_integer_with_probabilities(probabilities):
    choices = [0, 1, 2, 3]
    return random.choices(choices, weights=probabilities)[0]

probabilities = [0.40, 0.10, 0.40, 0.10]

value = 0
count = 0
stage = 2
step = random.randint(1,51)
current_step = 0
with open('./Laptop/DataSets/received_data.txt', 'w') as file:
    while count < 1000000:
        current_step += 1
        if current_step == step:
            stage = choose_random_integer_with_probabilities(probabilities)
            step = generate_random_integer(1, 75)
            current_step = 0
        else:
            if stage == 0:
                value = max(value-1,0)
            elif stage == 2:
                value = min(value+1,220)
            else:
                value = value  

        binary_value = decimal_to_binary(value,10) + decimal_to_binary(stage,2)
        file.write(str(binary_value) + '\n')
        count += 1
    
