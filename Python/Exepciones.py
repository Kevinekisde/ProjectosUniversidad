import sys
def linux_intercation():
    assert('linux' in sys.platform),("funcion puede correr solo en linux")
    print('doing something')
try:
    linux_intercation()
except:
    print("no")

