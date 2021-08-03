#from tkinter import *

#root = Tk()
#root.title('AIM - Avian (not so) Instant Messenger')
#main_canvas = Canvas(root, height=400, width=400)
#main_canvas.pack()

input = input('Message: ')
def encrypt_message(input):
    #input = T2.get("1.0",END) # This is the message string variable
    print(f'MESSAGE: {input}\nTYPE: {type(input)}\nMESSAGE LENGTH: {len(input)}') # Info for you good sir

    # ======= ADD ENCRYPTION OF SOME SORT AND OUTPUT TO A NEW VARIABLE. =========== 
    
    output = 'encrypted message test'

    try:
        if output:
            pass # If a message was written, filedialog will have you save the encrypted .txt to a flashdrive.
        else:
            pass # do nothing.
    except:
        pass

encrypt_message(input)
#T2 = Text(main_canvas, wrap=WORD, height=35, width=50)
#T2.place(relx=0, rely=0)

#send_button = Button(root, text=' SEND MESSAGE ')
#send_button.bind('<Button-1>', encrypt_message)
#send_button.pack()

#oot.mainloop()
