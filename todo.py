# This is a simple ToDo list app as you can insert the number of entries, able to update and also you can delete the inserted data.


from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root=root
        self.root.title('ToDo-List-App')                                  #title for the app
        self.root.geometry('650x410')                                     #set the geometry according to your need   
        self.label=Label(self.root, text='todo-list',                     #creating a label for the title of the app inside the app
            font='ariel, 25 bold', bd=5, bg='orange',width=10, fg='black')
        self.label.pack(side='top', fill='both')                          #another label for the indication to entry as Add Member
        self.label2=Label(self.root, text='Add Member',
            font='ariel, 18 bold', bd=5, bg='orange',width=10, fg='black')
        self.label2.place(x=40, y=55)                     
        self.label3=Label(self.root, text='Members',                      #another label for representing the entered data as Members
            font='ariel, 18 bold', bd=5, bg='orange',width=10, fg='black')
        self.label3.place(x=400, y=55)
        self.main_text=Listbox(self.root, bd=5, height=10, font='ariel, 20 italic bold',
                               width=25)                                  #creating the listbox where we can store our data
        self.main_text.place(x=350, y=100)
        self.text=Text(self.root, bd=5, height=1, font='ariel, 10 bold',
                               width=30)                                  #creating the entry section where we write the data to be insert
        self.text.place(x=20, y=120)
 
        #creating add function by which we can able to add the entered data in the entry section to the listbox
        def add():                                           
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)
        #creating the delete function for delete the available data from the listbox
        def delete():
            delete_=self.main_text.curselection()
            look =self.main_text.get(delete_)
            with open('data.txt', 'r+') as file:
                new_file=file.readlines()
                file.seek(0)
                for line in new_file:
                    item=str(look)
                    if item not in line:
                        file.write(line)
                file.truncate()
            self.main_text.delete(delete_)
        
        with open('data.txt', 'r') as file:
            read=file.readlines()
            for i in read:
                ready=i.split()
                self.main_text.insert(END, ready)
            file.close()
            
        #creating add button which call the add function 
        self.button = Button(self.root, text="Add", font='sarif, 20 italic bold', 
                    width=10, bd=5, bg='orange', fg='black', command=add)
        self.button.place(x=40, y=150)

        #creating the delete button to call the delete function 
        self.button2 = Button(self.root, text="Delete", font='sarif, 20 italic bold', 
                    width=10, bd=5, bg='orange', fg='black', command=delete)
        self.button2.place(x=40, y=200)

            
        

def main():
    root = Tk()           #creating root window
    ui=todo(root)
    root.mainloop()

if __name__=="__main__":
    main()                 #calling the main function
