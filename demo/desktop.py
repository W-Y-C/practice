from tkinter import *
from tkinter import messagebox
from selector import select_images
class desktop(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
        self.mainloop()

    def createWidgets(self):
        master=self.master
        # 组件添加
        self.lblTitle=Label(self,text='网络图片搜查')
        self.star=Label(self,text='目标:')
        self.label2=Label(self,text='范围:')
        self.entrytarget=Entry(self)
        self.entrylabel2=Entry(self)
        self.btnOK=Button(self,text='确定',command=lambda :select_images(int(self.entrylabel2.get()),self.get_messsage()).run())
        self.btnCancel=Button(self,text='取消',command=master.destroy)




        # 组件部署
        self.lblTitle.grid(row=0,column=0,columnspan=4)
        self.star.grid(row=1,column=0)
        self.entrytarget.grid(row=1,column=1,columnspan=3)
        self.label2.grid(row=2, column=0)
        self.entrylabel2.grid(row=2, column=1, columnspan=3)
        self.btnOK.grid(row=3,column=1,sticky=E)
        self.btnCancel.grid(row=3,column=3,sticky=W)

    def get_messsage(self):
        return self.entrytarget.get().split(',')
