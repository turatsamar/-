
#画像認識に挑戦

#矢印の書かれた画像をみて、　矢印の判別してみる
#矢印の方向　判定　PIL(Python　Image　Library)
#カラー画像の読み込み　拡張子は　jpg
from PIL import Image
while True:
    data=input("\画像のファイル名　(.jgp　は　省略)　＝　")
    if data =="":break
    img=Image.open("C:/Users/Turatbek/Desktop/gazou/" +data+ ".jpg")
    Px=img.width
    Py=img.height
    print("\n  チェックする画像ファイル名＝C:\Turatbek\Desktop\gazou\ " +data+".jpg")
    print("元の画像サイズ=",img.width,"x",img.height)
    fx, fy = 600/img.width, 400/img.height
    size= (round(img.width*fx), round(img.height*fy))
    img=img.resize(size)
    print("変更後の画像サイズ=",img.width,"x",img.height)
    Px=img.width
    Py=img.height
    img = img.convert("L")
    img.save(data+'.jpg', 'bmp')
    print("カラー画像をグレースケールのビットマップに変更して処理します")
    print("   Analysis by PIL(Puthon Image Library)")
    val1=img.getpixel((int(Px/2),50))
    ch=0
    min=255
    max=0
    for x in range(51,Px-10):
        for y in range(51,Py-10):
            val2=img.getpixel((x,y))
            if val2<val1-10 or val2>val1+10:
                if val2<val1-10 and val2<min:min=val2
                if val2>val1+10 and val2>max:max=val2
    if 255-min > max-0:val2=min
    if 255-min < max-0:val2=max
    if val1>val2:
        type=1
        print("矢印は背景より暗い色です。")
        if val1<val2:type=-1
        print("矢印は背景より暗い色です。")

    erea_start=[0,0]
    erea_end=[0,0]
    ch=0
    for x in range(10,Px-10):
        for y in range(10,Py-4):
            if type==1:
                if val2-80<0:val2=80
                val=img.getpixel((x,y))
                if ch==0 and val<val1-80:
                    erea_start[0]=x
                    erea_start[1]=y
                    ch=1
                    break
                if ch==1 and val<val1-80:
                    if erea_start[1]>y:erea_start[1]=y
                    if erea_end[1]<y: erea_end[1]=y
                    erea_end[0]=x
            if type==-1:
                if val1+70>255:val1=255-70
                val=img.getpixel((x,y))
                if ch==0 and val1>=val1+70:
                    erea_start[0]=x
                    erea_start[1]=y
                    break
                if ch==1 and val>=val1+70:
                    if erea_start[1]>y:erea_start[1]=y
                    if erea_end[1]<y:erea_end[1]=y
                    erea_and[0]=xml

    print("矢印の表示エリア")
    print("  スタート",erea_start)
    print("　　エンド　　", erea_end)
    cropped=img.crop((erea_start[0],erea_start[1],erea_end[0],erea_end[1]))
    fx, fy = 600/cropped.width, 400/cropped.height
    size=(round(cropped.width*fx),round(cropped.height*fy))
    img=cropped.resize(size)
    img.show()
    Px=img.width
    Py=img.height

    val1=img.getpixel((10,10))
    for x in range(10,Px):
        ch=0
        for y in range(10,Py):
            val2=img.getpixel((x,y))
            if val<val1-50 or val2>val1+50:
                ch=1
                break
        if ch==1:break
    print("val1(背景)＝", val,"  val2(矢印)＝",val2)

    discrimination=[]
    y=int(Py/8)
    for x in range(Px):
        if type==1:
            val=img.getpixel((x,y))
            if val<val1-70:
                for j in range(y+1):
                    val=img.getpixel((x,j))
                    if val<val1-70:
                        discrimination.append(j)
                        break
        if type==-1:
            val=img.getpixel((x,y))
            if val>val+50:
                for j in range(y+1):
                    val=img.getpixel((x,j))
                    if val<val1+50:
                        discrimination.append(j)
                        break
    print("\n 最終判断用データ\n",discrimination)
    n=len(discrimination)
    if n==0:
        print("\n 判定出来ません")
    elif discrimination [2]>discrimination[int(n/2)] and discrimination[n-2]>discrimination[int(n/2)]:
        print("\n 直進方向です。")
    elif discrimination[2]>discrimination[n-2]:print("\n 左方向です。")
    elif discrimination[2]<discrimination[n-2]:print("\n 右方向です。")



