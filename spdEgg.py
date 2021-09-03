# -*- coding: utf-8 -*-
"""
Created on Web Sep 1 21:00:00 2021

@author: Chin-Yeh Chen
"""
import os

def calculate(fname):
    pathO = os.getcwd()

    #
    lon = []
    lat = []
    lname = []
    with open(fname) as f:
        for line in f.readlines():
            s = line.split('\t')
            lon.append(str(s[0]))
            lat.append(str(s[1]))
            lname.append(str(s[2]).strip()) # strip() for removing \n

    #
    # print(lon)
    # print(lat)
    # print(lname)
    #

    # grap lineName and distinct
    unique = []
    for lineName in lname:
        if lineName not in unique:
            unique.append(lineName)

    # get Data
    for lnmae in unique:
        path = pathO + '/spd_Egg/lines/' + lnmae + '.txt' #path important!
        f = open(path, 'w') #寫檔案

        for i in range(0, len(lon), 1):
            if lnmae == lname[i]:
                f.write(lon[i] + '\t' + lat[i] + '\t' + lname[i] + '\n') # the row
    f.close()



# main #
fname = '/Users/yago/Documents/py_test/demo/imgTest/spd_Egg/SPK_location_latlot.txt'
calculate(fname)






''' “假如想要手選要被切開的檔案”
def select_file():
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))

    # select file
    filename = fd.askopenfilename(
        title='Open a file', initialdir='/', filetypes=filetypes)

    # showinfo(title='Selected File', message=filename)
    # read csv file and calculate
    calculate(readCsv(filename))

### create the window window###
window = tk.Tk()
window.title('window itself')
window.resizable(False, False)
window.geometry('450x300')

# open button
open_button = ttk.Button(window, text='OPEN A FILE', command=select_file)
open_button2 = ttk.Button(window, text='CLOSE', command=window.destroy)

open_button.pack(expand=True)
open_button2.pack(expand=True)

# run the application
window.mainloop()
'''