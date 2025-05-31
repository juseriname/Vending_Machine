from tkinter import *

root = Tk()

root.title('Application')
root.geometry("480x640")

# #btn1 = Button(root, text = '버튼1')
# #btn2 = Button(root, text = '버튼2')

# #btn1.pack(side = 'left')
# #btn2.pack(side = 'left')

# #btn1.grid(row = 0, column = 0)
# #btn2.grid(row = 1, column = 1)

btn_f16 = Button(root, text = 'f16', padx = 10, pady = 10)
btn_f17 = Button(root, text = 'f17', padx = 10, pady = 10)
btn_f18 = Button(root, text = 'f18', padx = 10, pady = 10)
btn_f19 = Button(root, text = 'f19', padx = 10, pady = 10)
btn_f16.grid(row = 0, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn_f17.grid(row = 0, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_f18.grid(row = 0, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_f19.grid(row = 0, column = 3, sticky = N+E+W+S, padx = 3, pady = 3)

btn_1 = Button(root, text = '1', padx = 10, pady = 10)
btn_2 = Button(root, text = '2', padx = 10, pady = 10)
btn_3 = Button(root, text = '3', padx = 10, pady = 10)
btn_enter = Button(root, text = 'enter')

btn_1.grid(row = 1, column = 0, sticky = N+E+W+S, padx = 3, pady = 3)
btn_2.grid(row = 1, column = 1, sticky = N+E+W+S, padx = 3, pady = 3)
btn_3.grid(row = 1, column = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_enter.grid(row = 1, column = 3, rowspan = 2, sticky = N+E+W+S, padx = 3, pady = 3)

btn_0 = Button(root, text = '0', padx = 10, pady = 10)
btn_point = Button(root, text = '.', padx = 10, pady = 10)

btn_0.grid(row = 2, column = 0, columnspan = 2, sticky = N+E+W+S, padx = 3, pady = 3)
btn_point.grid(row = 2, column = 2,  sticky = N+E+W+S, padx = 3, pady = 3)

root.mainloop()