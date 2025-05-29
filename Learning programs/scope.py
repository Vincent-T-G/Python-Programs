# The program is written in the learning and practice of working with variable scope in python

x = "global x"

def test():
    x = 'enclosing x'

    def inner():
        x = 'local x'
        print(x)

    inner()
    print(x)

test()
print(x)