# What's Your Name? in Python:

def print_full_name(a, b):
    print(("Hello %s %s! You just delved into python.")%(first_name,last_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#####################################################################################################################################

# Alternate Solution: (NOTE: Which works only for Python 3.7 or above)

def print_full_name(a, b):
    print(f"Hello {first_name} {last_name}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
