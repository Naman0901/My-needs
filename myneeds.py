def calculatorprogram():
    
    def addition ():
        print("Addition")
        n = float(input("Enter the number: "))
        t = 0 #Total number enter
        ans = 0
        while n != 0:
            ans = ans + n
            t+=1
            n = float(input("Enter another number (0 to calculate): "))
        return [ans,t]
    def subtraction ():
        print("Subtraction");
        n = float(input("Enter the number: "))
        t = 0 #Total number enter
        ans = 0
        while n != 0:
            ans = ans - n
            t+=1
            n = float(input("Enter another number (0 to calculate): "))
        return [ans,t]
    def multiplication ():
        print("Multiplication")
        n = float(input("Enter the number: "))
        t = 0 #Total number enter
        ans = 1
        while n != 0:
            ans = ans * n
            t+=1
            n = float(input("Enter another number (0 to calculate): "))
        return [ans,t]
    def average():
        an = []
        an = addition()
        t = an[1]
        a = an[0]
        ans = a / t
        return [ans,t]
    # main...
    while True:
        list = []
        print(" \nSimple Calculator in python")
        print(" Enter 'a' for addition")
        print(" Enter 's' for substraction")
        print(" Enter 'm' for multiplication")
        print(" Enter 'v' for average")
        print(" Enter 'q' for quit")
        c = input(" ")
        if c != 'q':
            if c == 'a':
                list = addition()
                print("\nAns = ", list[0], " total inputs ",list[1])
            elif c == 's':
                list = subtraction()
                print("\nAns = ", list[0], " total inputs ",list[1])
            elif c == 'm':
                list = multiplication()
                print("\nAns = ", list[0], " total inputs ",list[1])
            elif c == 'v':
                list = average()
                print("\nAns = ", list[0], " total inputs ",list[1])
            else:
                print ("Sorry, invilid character")
        else:
            break


def youtubeprogram():
    from pytube import YouTube
    from pytube import Playlist

    def vedio(youtube_video_url,path):
        try:
            yt_obj = YouTube(youtube_video_url) 
            stream=yt_obj.streams.filter(progressive=True)
            for i in range(len(stream)):
                print(i ,stream[i])
            
            n=int(input("Enter The Corresponding Number You Want To Download(-1 To Exit):"))
            if n==-1:
                return
            elif n>len(stream)-1:
                print("invalid Choice.")
                return
            else:
                stream[n].download(output_path=path, filename=yt_obj.title)
                print('Video Downloaded Successfully')
        except Exception as e:
            print(e)


    def multyvedio(list_urls,path):
        for url in list_urls:
            try:
                yt_obj = YouTube(url) 
                stream=yt_obj.streams.filter(progressive=True)
                for i in range(len(stream)):
                    print("\n", i ,stream[i])
            
                n=int(input("Enter The Corresponding Number You Want To Download(-1 To Exit):"))
                if n==-1:
                    return
                elif n>len(stream)-1:
                    print("invalid Choice.")
                    return
                else:
                    stream[n].download(output_path=path, filename=yt_obj.title)
                
            except Exception as e:
                print(e)
                raise Exception('Some exception occurred.')
        print('All YouTube videos downloaded successfully.')
            
            
    def playlist(plist,path):
        try:
            playlist = Playlist(plist)
            re=(input('Enter Resolution 360 or 720:')) + "p"
            i=1;
            for vedio in playlist.videos:       
                stream=vedio.streams.filter(progressive=True, res=re)
                stream[0].download(output_path=path, filename=playlist.title+str(i))
                i+=1;
            print("Done")
        except Exception as e:
            print(e)






    print('Welcome To Youtube Downloader')
    download=True
    while(download==True):
        print('\nSelct Your Choice:')
        print('1. Download Single Video.')
        print('2. Download Multiple Video.')
        print('3. Download Single Playlist.')
        try:
            choice=int(input())
        except Exception as e:
            print(e)
        
        if choice==1:
            url=input('Please Paste Url:')
            path=input('Please Give Path Were To Save Video:')
            vedio(url,path)

        elif choice==2:
            n=int(input('Please Enter Number Of Vedio to Download:'))
            url=[]
            for i in range(0,n):
                url.append(input('Please Paste Url:'))
            path=input('Please Give Path Were To Save Videos:')
            multyvedio(url,path)

        
        elif choice==3:
            url=input('Please Paste Url:')
            path=input('Please Give Path Were To Save Playlist:')
            playlist(url,path)

        else:
            print('Invalid Choice.')
        again=input("Do you Wnat To Continue(y/n):")
        if again.lower() != 'y':
            download=False



def pdfprogram():
    from PIL import Image
    import tkinter as tk
    import img2pdf
    import os
    import glob
    from tkinter import filedialog
    from tkinter import messagebox

    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
    canvas1.pack()

    label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
    label1.config(font=('helvetica', 20))
    canvas1.create_window(150, 60, window=label1)

    def getFile ():
        global imgs    
        
        import_file_path = filedialog.askdirectory()
        imgs= import_file_path + "/*.jpg"


    browseButton = tk.Button(text="     Select File     ", command=getFile, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 130, window=browseButton)

    def convertToPdf ():
        global im1
        
        export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
        with open(export_file_path,"wb") as f:
            f.write(img2pdf.convert(glob.glob(imgs)))
        MsgBox = tk.messagebox.showinfo('File Created','File Create');

    saveAsButton = tk.Button(text='Convert to PDF', command=convertToPdf, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 180, window=saveAsButton)

    def exitApplication():
        MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
        if MsgBox == 'yes':
            root.destroy()
        
    exitButton = tk.Button (root, text='Exit Application',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 230, window=exitButton)

    root.mainloop()


app=True
while app==True:
    print('\nSelct Your Choice:')
    print('1. Download Youtube Video.')
    print('2. Create Pdf File From Images.')
    print('3. Simple Calculator.')
    try:
        choice=int(input())
    except Exception as e:
        print(e)
        
    if choice==1:
        youtubeprogram()
    elif choice==2:
        pdfprogram()
    elif choice==3:
        calculatorprogram()
    else:
        print('invslid Choice')
    again=input("Do You Want To Continue in MyNeeds(Y/N):")
    if again.lower()!="y":
        app=False
