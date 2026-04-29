import time
print("\033[1;32m")
for i in range(1,11):
    time.sleep(2)
    for j in range(1,11):
        print("{:02}".format(i*j),end=" ")
    print()
