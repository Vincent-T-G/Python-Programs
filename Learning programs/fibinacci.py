# Problem statement: Write a program that prints the fibinacci sequence of any size on the screen

sequence = [0,1]

length = int(input("How many numbers of the fibonacci sequence do you want to output: "))


def printing():
    for i in range(len(sequence)):
        if i < len(sequence) - 1:
            print(sequence[i], end=", ")
        else:
            print(sequence[i])

if length <= 0:
    print("The number has to be greater than 0!")
elif length == 1:
    print(sequence[0])
elif length == 2:
    printing()
else:
    for i in range(2,length):
        next = sequence[i-1] + sequence[i-2]
        sequence.append(next)
    printing()

