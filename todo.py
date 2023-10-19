from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root=root
        self.root.title('ToDo-List-App')
        self.root.geometry('650x410+300+150')
        self.label=Label(self.root, text='todo-list',
            font='ariel, 25 bold', bd=5, bg='orange',width=10, fg='black')
        self.label.pack(side='top', fill='both')
        self.label2=Label(self.root, text='Add Member',
            font='ariel, 18 bold', bd=5, bg='orange',width=10, fg='black')
        self.label2.place(x=40, y=55)
        self.label3=Label(self.root, text='Members',
            font='ariel, 18 bold', bd=5, bg='orange',width=10, fg='black')
        self.label3.place(x=400, y=55)
        self.main_text=Listbox(self.root, bd=5, height=10, font='ariel, 20 italic bold',
                               width=25)
        self.main_text.place(x=350, y=100)
        self.text=Text(self.root, bd=5, height=1, font='ariel, 10 bold',
                               width=30)
        self.text.place(x=20, y=120)
 

        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

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
        
        self.button = Button(self.root, text="Add", font='sarif, 20 italic bold', 
                    width=10, bd=5, bg='orange', fg='black', command=add)
        self.button.place(x=40, y=150)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 italic bold', 
                    width=10, bd=5, bg='orange', fg='black', command=delete)
        self.button2.place(x=40, y=200)

            
        

def main():
    root = Tk()
    ui=todo(root)
    root.mainloop()

if __name__=="__main__":
    main()
