# with open("practice_question","w") as f:
#     f.write("My Name is Paravin \nI am from banglore \nI am Learning python programming \nI love python")
#
with open("txt files/practice_question", "r") as f:
    data = f.read()
    print(data)

new_data = data.replace("python","java")
print(new_data)

with open("txt files/practice_question", "w") as f:
    f.write(new_data)

def check_for_word():
    word = "java"
    with open("txt files/practice_question", "r") as f:
        data = f.read()
        if (data.find(word) != -1):
            print("found")
        else:
            print("not found")

print(check_for_word())
#
#
def check_for_line():
    word = "My"
    data = True
    line_no = 5
    with open("txt files/practice_question", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no += 1

    return -1


check_for_line()