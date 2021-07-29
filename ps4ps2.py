print("Enter a startvalue")
startv = int(input())
print("Enter a stopv")
stopv = int(input())
print("Enter an incrv")
incrv = int(input())
for startv in range(startv, stopv + incrv, incrv):
    print("Loop literation" + str(startv))
