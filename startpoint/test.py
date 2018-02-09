from startpoint import entrypoint

@entrypoint(__name__)
def main(args=[]):
    for i in args:
        print(i)
