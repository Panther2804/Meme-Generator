from PIL import Image, ImageDraw, ImageFont

drake = ("Memename","Templates/Drake-Comparison.jpg",{
    "Field_0":((5,362,586,565),(0,0,0),40),
    "Field_1":((602,3,600,590),(0,0,0),40),
    "Field_2":((599,601,1200,1199),(0,0,0),40), } ,"Fonts/sfont.otf")
memeinfo = drake
drake


def wrap(imagedraw, text, fontpath, fontsize, fontcolor, x1, y1, x2, y2):
    font = ImageFont.truetype(fontpath, fontsize)
    maxX = x2 - x1
    maxY = y2 - y1
    centerX = 0.5 * (x1 + x2)
    centerY = 0.5 * (y1 + y2)
    textXsize = 0
    textYsize = 0

    textcopy = text
    linetext = []
    currentline = ""

    while textcopy != "":

        width, height = imagedraw.textsize(currentline + textcopy[-1] + "-",
                                           font=font)

        if width > maxX:
            s = ""
            print("new end")
            print(currentline[:-5:-1] + "<end>")
            for i in currentline[:-5:-1]:
                print('sym:"' + i + '"')
                s += i
                if i == " ":
                    textcopy = s[::-1] + textcopy
                    print("S:" + s[::-1])
                    currentline = currentline[:-len(s)]

                    if textcopy[0] == " ":
                        textcopy = textcopy[1:]

                    s = ""

                    break
            print("Only appending " + currentline + ", leaving " + textcopy)

            if s == "":
                linetext.append(currentline)
            else:
                linetext.append(currentline + "-")

            currentline = ""
            textYsize += height

            if height > maxY:
                print("Well fuck")

        else:
            currentline += textcopy[0]
            textcopy = textcopy[1:]
            # print(textcopy)

    linetext.append(currentline)
    currentline = ""

    currentY = 0
    xstart = centerX - 0.5 * maxX
    ystart = centerY - 0.5 * textYsize

    print(str(linetext))

    for i in linetext:
        print("Drawing @ x: " + str(xstart) + " y: " + str(ystart))
        draw.text((xstart, ystart), i, font=font, fill=fontcolor)
        ystart += imagedraw.textsize(i, font=font)[1]
        print(imagedraw.textsize(i, font=font)[1])


im = Image.open("testtemplate.png")
im = im.convert("RGB")
draw = ImageDraw.Draw(im)
font = memeinfo[3]

message = "Das ist ein echter Testsatz, mit dem ich teste."
wrap(draw, message, font, 40, (0, 0, 0), 125, 125, 375, 375)
im.save("text.png")