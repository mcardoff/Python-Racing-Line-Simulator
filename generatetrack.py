import pyautogui
import time

def main():
    # insert code here
    # print('Hello World!')
    # first generate racing line
    trackxy = []
    try: 
        while True:  
            trackxy.append(pyautogui.position())
            print(trackxy[-1])
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

    file = open('track.txt', 'w')
    for tup in trackxy:
        file.write(str(tup)+"\n")

    file.close()

if __name__ == "__main__":
    main()
