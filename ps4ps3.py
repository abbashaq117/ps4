totalex1 = 0
counter = 0
print("Do you want to compute your average score(Yes or No)")
response = input()
while response == "Yes":
    counter = counter + 1
    print("Enter student lastname")
    lastname = input()
    print("Enter exam score 1")
    score1 = float(input())
    print("Enter exam score 2")
    score2 = float(input())
    avg = (score1 + score2) / 2
    totalex1 = totalex1 + score1
    print("Student " + lastname + " has average of " + str(avg))
    response = input()
print("Total Number of Students" + str(counter))
avgex1 = totalex1 / counter
print("Average Exam score 1 is " + str(avgex1))
