print("Welcome to Kaun Banega Crorepati 🏆")
print("Each correct answer gives ₹1000\n")

questions = [
    "Who is the best programmer? a) Harry b) Striver c) Love Babbar d) All",
    "What does SQL stand for? a) Super Quick Language b) Software Query Logic c) Structured Query Logic d) Structured Query Language",
    "What does Boolean datatype represent? a) Numbers b) True/False c) Decimal d) Fraction",
    # "Which is not a core data type? a) Class b) List c) Dictionary d) Tuple",
    # "What is the data type of L = [1, 23, 1]? a) List b) Dictionary c) Tuple d) Array"
]

answers = ["d", "d", "b", "a", "a"]

reward = 0

for que, correct_ans in zip(questions, answers):
    print(que)
    user_ans = input("Enter your answer (a/b/c/d): ").lower()

    if user_ans == correct_ans:
        print("✅ Correct!\n")
        reward += 1000
    else:
        print("❌ Wrong answer")
        break

print("Your total reward is ₹", reward)


# factorial

def fact(n):
    if (n == 0 or n ==1 ):
        return 1
    else:
        return n * fact(n-1)

print(fact(7))
print(fact(6))
print(fact(3))


#Fibonacci
n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a,end=" ")
    a = b
    b = a + b
    count += 1
