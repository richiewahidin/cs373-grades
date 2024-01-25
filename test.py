import random

num_tests = random.randint(200,300)
print(num_tests)

def generate_random_sequence(length):
    sequence = [random.choice([0, 1, 2, 3]) if random.random() < 0.25 else random.randint(2, 3) for _ in range(length)]
    return sequence

for _ in range(0,num_tests):
    # Generate 5 random numbers with reduced frequency of 0
    proj = generate_random_sequence(5)
    exercise = generate_random_sequence(12)
    blog = generate_random_sequence(14)
    paper = generate_random_sequence(14)
    quizzes = generate_random_sequence(42)
    
    # Print the result
    print(" ".join(map(str, proj)))
    print(" ".join(map(str, exercise)))
    print(" ".join(map(str, blog)))
    print(" ".join(map(str, paper)))
    print(" ".join(map(str, quizzes)))
    print("")
