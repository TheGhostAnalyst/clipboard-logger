import shelve
import pyperclip
import sys
import time

DB_COPY = 'Clipboard.db'

def log_clipboard():
    last_copy =""
    with shelve.open(DB_COPY, writeback=True) as db:
        while True:
            try:
                current_copy = pyperclip.paste()
                if current_copy != last_copy and current_copy.strip():
                    timestamp = time.strftime("%Y-%m-%d %H-%M")
                    db[timestamp] = current_copy
                    last_copy = current_copy
                    print(f"New copy has been logged at {timestamp}:")
                    print(current_copy)
                    print('-' * 50)

                time.sleep(0.1)
            except KeyboardInterrupt:
                print('Exiting Clipboard logger....')
                break

def show_all():
    with shelve.open(DB_COPY) as db:
        for key in sorted(db):
            print('-' * 40)
            print(f'[{key}]')
            print(db[key])
            print('-' * 40)
            

# Menu loop
while True:
    try:
        choice = input('Check clipboard logs? (y/n/exit) Enter (n) to start clipboard logger: ').strip().lower()
        if choice == 'y':
            print('Getting clipboard logs from database...')
            time.sleep(1)
            show_all()
        elif choice == 'n':
            print('Starting clipboard logging...')
            log_clipboard()
        elif choice == 'exit':
            print('Exiting Clipboard logger.')
            sys.exit()
        else:
            print('Invalid input. Please type y, n, or exit.')
    except KeyboardInterrupt:
        print('\nExiting Clipboard logger.')
        sys.exit()
