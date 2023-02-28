import pyperclip

while True:
    lines = []
    print("Bitte geben Sie mehrere Zeilen Text ein (leere Zeile zum Beenden):")
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    if not lines:
        break
    
    result = ""
    for line in lines:
        for symbol in [".", "-", "+", "<", ">", ":"]:
            line = line.replace(" "+symbol, symbol).replace(symbol+" ", symbol)
        stripped_line = line.lstrip('0123456789 ')
        line = line.replace("’", "'")
        result += stripped_line + "\n"
        
    pyperclip.copy(result.strip())
    print("Der bereinigte Text wurde in die Zwischenablage kopiert.")
    
print("Programm beendet.")

