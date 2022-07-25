import sys

from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) != 1:
    if len(sys.argv) != 3:

        sys.exit("Invalid usage")


    elif sys.argv[1] != "-f" and "--font":
        print(sys.argv[1])
        sys.exit("Invalid usage")

if (len(sys.argv)) == 3:
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    text = input("Input: ")
    font = sys.argv[2]
    figlet.setFont(font=font)
    print(figlet.renderText(text))

if (len(sys.argv)) == 1:
    text = input("Input: ")
    font = '3-d'
    figlet.setFont(font=font)
    print(figlet.renderText(text))
