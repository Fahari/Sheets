from pyfiglet import Figlet
import pyfiglet
import os
import sys
import signal
import xlsxwriter


if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


def signal_handler(signal, frame):
    print("\nTerminated Successfully!!")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

print(r"""

                                  __,__
                         .--.  .-"     "-.  .--.
                        / .. \/  .-. .-.  \/ .. \
                       | |  '|  /   Y   \  |'  | |
                       | \   \  \ 0 | 0 /  /   / |
                        \ '- ,\.-"`` ``"-./, -' /
                         `'-' /_   ^ ^   _\ '-'`
                             |  \._   _./  |
                             \   \ `~` /   /
                              '._ '-=-' _.'
                                 '~---~'
 

                """)


custom_fig = Figlet(font='doom')
print(custom_fig.renderText('           For the Noobs'))
# ascii_banner = pyfiglet.figlet_format("for the noobs")
# print(ascii_banner)
fileName = input("NAME YOUR EXCEL FILE: ")


text = input("COLUMN TITLES: ")
txt = text.split()
txt2 = [x.upper() for x in txt]

arr = list()
count = 1
while (count < 1000000):
    count = count + 1

    print("-" * 50)
    print("*" + str(count))
    inside = list()
    for n in range(len(txt)):

        inside.append(input(str(txt[n]).upper() + ": "))

    arr.append(inside)

    workbook = xlsxwriter.Workbook(
        os.path.expanduser("~/Desktop/%s.xlsx" % fileName))
    worksheet = workbook.add_worksheet()

    worksheet.write_row(0, 0, txt2)

    for row_num, row_data in enumerate(arr):
        for col_num, col_data in enumerate(row_data):
            worksheet.write(row_num + 1, col_num, col_data)

    workbook.close()
