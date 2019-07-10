from PIL import Image
import os

def pickImg():
    chosenFile = 0
    files = []
    for k in os.listdir('.'):
        kn = k.lower()
        if kn.endswith('.jpg') or kn.endswith('.png'):
            files.append(k)

    for f in range(len(files)):
        print(str(f+1) + ". " + str(files[f]))
        
    chosenFile = input("Choose your image number: ")
    return files[int(chosenFile) - 1]

def calcBrightness(r,g,b):  
    return (0.2126*r + 0.7152*g + 0.0722*b)

def printArt(minBrightness, img):
    im = Image.open(img)
    pix = im.load()
    for j in range(1, im.size[1]-1):
        line = "­"
        cont = False
        for i in range(1, im.size[0]-1):
            brightness = calcBrightness(pix[i,j][0],pix[i,j][1],pix[i,j][2])
            avgbright = 0
            for nx in range(-1,1):
                for ny in range(-1,1):
                    posx = i+nx
                    posy = j+ny
                    avgbright += calcBrightness(pix[posx,posy][0],pix[posx,posy][1],pix[posx,posy][2])
            avgbright = (avgbright / 9) - brightness
            if avgbright < -minBrightness:
                if cont == False:
                    line += "||     "
                else:
                    line += "     "
                cont = True
            else:
                if cont == True:
                    line += "||     "
                else:
                    line += "     "
                cont = False
        print(line)
    print("Printed '" + str(img) + "' with minimum brightness of " + str(minBrightness))
    choice = input("\n\n'M' to change the minimum brightness, 'I' to pick another image, 'R' to print the image again")
    if choice.lower() == "m":
        print("\n\nMost images should look fine with min brightness at 75\nIf you dont see your image at all with minimum brightness at 75 then try lowering it")
        minB = input("Min brightness (Currently its set to " + str(minBrightness)+ " | Default is 75): ")
        printArt(int(minB), img)
    elif choice.lower() == "i":
        print("\n\n")
        image = pickImg()
        printArt(minBrightness, image)
    elif choice.lower() == "r":
        printArt(minBrightness, img)

try:
    image = pickImg()
    printArt(75, image)
except:
    input("Your images need to be in the same folder as this python file.")
