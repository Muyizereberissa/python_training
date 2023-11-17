"""for letter in range(ord("A"), ord("F")+1):
    if chr(letter) == "E":
        continue
    else:
        print(chr(letter), end="")"""

let = ord("A")
while let <= (ord('F')):
    if let == ord("E"):
        pass
    else:
        print(chr(let), end=" ")

    let += 1