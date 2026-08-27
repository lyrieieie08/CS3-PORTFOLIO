year = int(input("Enter your birth year: "))

if year >= 1900:
    if (year-1900)%12==0:
        a='Rat (鼠 / Shǔ)'
        print(f"Your Chinese Zodiac is : {a}" )

    elif (year-1900)%12==1:
        b='Ox (牛 / Niú)'
        print(f"Your Chinese Zodiac is : {b}" )
            
    elif (year-1900)%12==2:
        c='Tiger (虎 / Hǔ)'
        print(f"Your Chinese Zodiac is : {c}" )
            
    elif (year-1900)%12==3:
        d=' Rabbit (兔 / Tù)'
        print(f"Your Chinese Zodiac is : {d}" )
            
    elif (year-1900)%12==4:
        e ='Dragon (龙 / Lóng)'
        rint(f"Your Chinese Zodiac is : {e}" )
            
    elif (year-1900)%12==5:
        f ='Snake (蛇 / Shé)'
        print(f"Your Chinese Zodiac is : {f}" )
            
    elif (year-1900)%12==6:
        g='Horse (马 / Mǎ)'
        print(f"Your Chinese Zodiac is : {g}" )

    elif (year-1900)%12==7:
        h='Goat (羊 / Yáng'
        print(f"Your Chinese Zodiac is : {h}" )
            
    elif (year-1900)%12==8:
        i ='Monkey (猴 / Hóu)'
        print(f"Your Chinese Zodiac is : {i}" )
            
    elif (year-1900)%12==9:
        j='Rooster (鸡 / Jī)'
        print(f"Your Chinese Zodiac is : {j}" )
            
    elif (year-1900)%12== 10:
        k='Dog (狗 / Gǒu)'
        print(f"Your Chinese Zodiac is : {k}" )
            
    elif (year-1900)%12==11:
        l='Pig (猪 / Zhū)'
        print(f"Your Chinese Zodiac is : {l}" )
    
else:
    print('Invalid year, it should not be earlier than 1900.')
