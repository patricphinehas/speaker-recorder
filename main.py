#my work here is to ge the playlist and initiate the process
import webbrowser as wb
import sys

if __name__ == "__main__":
    if len(sys.argv)>1:
        data = ''.join(sys.argv[1:])
        wb.open(data)
    else:
        print("pass the playlist URL as argument")
        
