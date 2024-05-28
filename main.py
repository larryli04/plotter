import sys

# handle arguments
n = len(sys.argv)
if(n == 3 and sys.argv[1] == "-f"):
    filename = sys.argv[2]
elif(n==2 and sys.argv[1] == "-c"):
    filename = None
    # initialize controller stuff (maybe use pygame)
    print("Controller not currently supported") 
    exit(1)

def penDown():
    pass

def penUp():
    pass

def goto(x: int, y:int, speed: float):
    pass

def main():
    # zero plotter

    # run with controller

    # run with predefined file
if __name__ == "__main__":
    main()

