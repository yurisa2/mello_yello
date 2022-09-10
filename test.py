import time
import logging

def main():
    while True:
        print('El Time: ', time.time())
        logging.info(time.time())
        time.sleep(1)

if __name__ == '__main__':
    main()
