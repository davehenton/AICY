import sys

def f_help(f,s,t):
    #print()
    #print()
    #print(f)
    #print(s)
    #print(t)

    if not f:
        print('This is the standart help')
    else:
        print('No help')

if __name__ == '__main__':
    f = str(sys.argv[1])
    s = str(sys.argv[2])
    t = str(sys.argv[3])
    f_help(f,s,t)
