from tkinter import Tk
from tkinter import Button
from tkinter import Menu
from tkinter import Text
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Entry
from tkinter import Label
from tkinter import StringVar
from ttkthemes import themed_tk as tk
from tkinter import ttk
import numpy as np
import string
import re
import os
import sys
import PyPDF2
import time


class Admin(object):

    global file
    FLAG = 0
    dataCon = []
    pdfname = ''
    contentList = []
    contentListSec = []

    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")

    def __init__(self):
        self.file = None
        self.key = None

    """LOAD PDF >>create coded text with tri values"""

    def loadPdf(self,pgNo, valPos):
        cdir = os.getcwd()
        try:
            if len(self.key) == False:
                print(self.key)
                messagebox.showinfo("Key", "No Inputed Key")
        except NameError:
            print("enter Key -> loadPdf",self.key)
            sys.exit(1)
        try:
            self.file = open(self.key, 'rb')
        except FileNotFoundError:
            print('no file found')
        except NameError:
            print('Enter Key')
        file2 = open(cdir + 'code.txt', 'a')

        pdfreader = PyPDF2.PdfFileReader(self.file)
        pdfpageno = pdfreader.numPages
        pdfpage = pdfreader.getPage(3 + pgNo)
        text = list(pdfpage.extractText())
        # print(text)
        try:
            if text[valPos] == None:
                print('if state')
            self.contentList.extend('')
            self.contentList.extend(text[valPos])
        except IndexError:
            print('Error Reading PDF...Enter readable PDF')
            time.sleep(2)
            sys.exit(1)

        # print(contentList)
        content_second_mem = str(pgNo) + ''.join(self.contentList) + str(valPos)
        file2.write(content_second_mem)
        self.contentListSec.append(content_second_mem)
        # print(contentListSec)
        self.contentList.clear()

    """DECIPHER CHILD"""

    def decipherChild(self,pdfFile, codeData):
        filePdf = open(pdfFile, 'rb')
        # file1=open('code.txt','r')
        # xx=open('xx.txt','w')
        codeDataList = []
        codeDataListAux = []
        convertedCode = []

        pdfreader = PyPDF2.PdfFileReader(filePdf)
        pdfpageno = pdfreader.numPages
        codeDataList = codeData
        #print(codeDataList)
        # for line in file1:
        # codeDataList.extend(list(line))

        for i in np.arange(0, len(codeDataList), 3):
            auxData = codeDataList[i], codeDataList[i + 1], codeDataList[i + 2]
            auxData2 = list(auxData)
            codeDataListAux.append(auxData2)

        tempList = []
        for it in range(0, len(codeDataListAux)):
            aux = codeDataListAux[it]
            tempList.extend(''.join(aux[0]))
            tempList.extend(''.join(aux[2]))

        # xx.write(''.join(tempList))
        #print('Fin delocating the tri into bi')
        return tempList

    """TAKE THE ENCODED FILE LIST"""

    def decipher(self,fileContent):
        cdir = os.getcwd()
        #encFilePath = 'replica.txt'
        DecriptedFile = cdir + "original.txt"
        # encodedFileObj=open(encFilePath,'r')
        decriptedFile = open(DecriptedFile, 'w')

        auxencFileList = []
        dic = auxDic = {'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15', '9': '16', ')': '17',
                        'f': '21', 'g': '22', 'h': '23', 'i': '24', 'j': '25', '8': '26', '(': '27',
                        'k': '31', 'l': '32', 'm': '33', 'n': '34', 'o': '35', '7': '36', '*': '37',
                        'p': '41', 'r': '42', 's': '43', 't': '44', 'u': '45', '6': '46', '&': '47',
                        'v': '51', 'w': '52', 'x': '53', 'y': '54', 'z': '55', '5': '56', '^': '57',
                        '0': '61', '1': '62', '2': '63', '3': '64', '4': '65', ',': '66', '.': '67',
                        '!': '71', '@': '72', '#': '73', '$': '74', '%': '75', '-': '76', '+': '77',
                        '>': '81', '<': '82', '_': '83', '\n': '84', '=': '85', '?': '86', '/': '87',
                        ':': '91', '"\"': '92', '~': '93', '`': '94', '\t': '95', ' ': '96', 'q': '97',
                        '{': '00', '}': '01', '[': '02', ']': '03'
                        }

        encFileList = []
        try:
            encFileList = self.decipherChild(self.key, fileContent)
        except NameError:
            print('enter key')
            time.sleep(2)
            sys.exit(1)

        x = []
        # for line in encodedFileObj:
        #    encFileList.extend(list(line))

        """need to combine 2digits for value to key \
        we do this by combining two digits into 1 """
        auxencFileList = ''.join(encFileList)  # this is a string from the encfilelist we take away spaces
        listHoldingFinalFile = []
        """check the no of char of the encripted if higher than 150k stop"""
        if len(auxencFileList) > 150000:
            print(len(auxencFileList))
            exit()

        print('auxencFileList De>>', len(auxencFileList))
        """this loop gets the dic value and key to write into final file"""
        for i in np.arange(0, len(auxencFileList), 2):
            x1 = auxencFileList[i], auxencFileList[i + 1]
            x2 = list(x1)
            x.append(''.join(x2))  # this is critical for ['ab','dr'....'nn']

        for i in range(0, len(x)):

            dicValue = x[i]
            # dicValue1=''.join(dicValue)
            try:
                dicKey = list(dic.keys())[list(dic.values()).index(dicValue)]

            except ValueError:
                dicKey = ' '

            # keyAux=''.join(dicKey)
            listHoldingFinalFile.extend(dicKey)

        decriptedFile.write(''.join(listHoldingFinalFile))
        print('Finished Deciphering')
    """READ A FILE """

    def encipher(self,fileList):

        auxDic = {'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15', '9': '16', ')': '17',
                  'f': '21', 'g': '22', 'h': '23', 'i': '24', 'j': '25', '8': '26', '(': '27',
                  'k': '31', 'l': '32', 'm': '33', 'n': '34', 'o': '35', '7': '36', '*': '37',
                  'p': '41', 'r': '42', 's': '43', 't': '44', 'u': '45', '6': '46', '&': '47',
                  'v': '51', 'w': '52', 'x': '53', 'y': '54', 'z': '55', '5': '56', '^': '57',
                  '0': '61', '1': '62', '2': '63', '3': '64', '4': '65', ',': '66', '.': '67',
                  '!': '71', '@': '72', '#': '73', '$': '74', '%': '75', '-': '76', '+': '77',
                  '>': '81', '<': '82', '_': '83', '\n': '84', '=': '85', '?': '86', '/': '87',
                  ':': '91', ']': '92', '~': '93', '`': '94', '\t': '95', ' ': '96', 'q': '97',
                  '{': '00', '}': '01', '[': '02'
                  }

        """reading the file into a List"""

        storyList = []
        storyList = fileList

        """ciphering """

        for i in range(0, len(storyList)):
            for j in auxDic:
                if j == storyList[i]:
                    storyList.pop(i)
                    storyList.insert(i, auxDic.get(j))
                    break
                else:
                    continue

        cipherText = ''.join(storyList)
        """removing punctuation from the """
        punctuation = string.punctuation
        for punc in punctuation:
            if punc in cipherText:
                cipherText = cipherText.replace(punc, "")

        """we remove all whitespaces"""
        saifa = re.sub(r'\s+', '', cipherText)

        """writing the cipher text into external replica file"""
        # file2.write(cipherText)

        """"CHECK WHETHER THE CIPHERTXT IS EVEN"""
        if len(cipherText) % 2 == False:
            print('CipherText Even')
            for q in np.arange(0, len(cipherText), 2):
                try:
                    pgNO = int(cipherText[q])
                    pgCont = int(cipherText[q + 1])
                    self.loadPdf(pgNO, pgCont)
                except ValueError:
                    print('check the Cipher Text')

        else:
            print("ciphertext !=even")
            sys.exit(1)

        print('FINISHED ENCODING !!cipherTxt Length >>{}'.format(len(cipherText)))

    def decode(self,txtBoxValue):
        self.checkKey()
        cdir = os.getcwd()
        print('from adminDecode>> TextBoxValue=>',txtBoxValue)
        fileBuffer = txtBoxValue
        if fileBuffer == 0:
            self.dataCon.extend(fileBuffer)
        self.dataCon.clear()
        if len(self.dataCon) == 0:
            """read from replica/encoded txt"""
            encFilePath = cdir + 'code.txt'
            try:
                encodedFileObj = open(encFilePath, 'r')
                #print('rad coded')
                for line in encodedFileObj:
                    self.dataCon.extend(list(line))
            except FileNotFoundError:
                print('coded file not found')



            """finished reading from the replica"""

        if len(fileBuffer) or len(''.join(self.dataCon)) == 1:
            if len(''.join(self.dataCon)) != 0:
                print('Decoding content from Cache')
                print(len(self.dataCon))
                self.decipher(self.dataCon)
            else:
                messagebox.showinfo("Empty Textbox", "Tbox and file cache occupied")
        elif len(''.join(self.dataCon)) or len(fileBuffer) == 1:
            print('Decoding file directory first')
            self.decipher(self.dataCon)
        else:
            messagebox.showinfo("Empty Textbox", "Enter Text For Decoding")

    def encode(self,txtBoxValue):
        self.fileBuffer = txtBoxValue
        self.checkKey()
        if len(self.dataCon) == 0:
            print('dataCon empty extending fileBufer')
            self.dataCon.extend(self.fileBuffer)
        # else:
        # clearCache()

        # dataconLen=len(dataCon)
        if len(self.fileBuffer) or len(''.join(self.dataCon)) == 1:
            if len(''.join(self.dataCon)) != 0:
                print('content from Cache')
                self.encipher(self.dataCon)
                # print(dataCon)
            else:
                # messagebox.showinfo("Empty Textbox","Tbox and file cache occupied")
                print(self.dataCon)
        elif len(''.join(self.dataCon)) or len(self.fileBuffer) == 1:
            print('file directory first')
            self.encipher(self.dataCon)
        else:
            messagebox.showinfo("Empty Textbox", "Enter Text For Encoding")

    def checkKey(self):
        try:
            if len(Admin.key) == 0:
                print('Enter key')
                sys.exit(1)
        except AttributeError:
            print('Restart the App....Enter KIFUNGUO nxt time')
            time.sleep(2)
            sys.exit(2)

    def clearCache(self):
        self.dataCon.clear()
        messagebox.showinfo("Cache ", "Done erasing cache")


class AllUser(object):

    def matrix(self,key):
        matrix = []
        for e in key.upper():
            if e not in matrix:
                matrix.append(e)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        for e in alphabet:
            if e not in matrix:
                matrix.append(e)

        # initialize a new list. Is there any elegant way to do that?
        matrix_group = []
        for e in range(5):
            matrix_group.append('')

        # Break it into 5*5
        matrix_group[0] = matrix[0:5]
        matrix_group[1] = matrix[5:10]
        matrix_group[2] = matrix[10:15]
        matrix_group[3] = matrix[15:20]
        matrix_group[4] = matrix[20:25]
        return matrix_group

    def message_to_digraphs(self,message_original):
        # Change it to Array. Because I want used insert() method
        message = []
        for e in message_original:
            message.append(e)

        # Delet space
        for unused in range(len(message)):
            if " " in message:
                message.remove(" ")

        # If both letters are the same, add an "X" after the first letter.
        i = 0
        msgLen = int(len(message) / 2)
        for e in range(msgLen):
            if message[i] == message[i + 1]:
                message.insert(i + 1, 'X')
            i = i + 2

        # If it is odd digit, add an "X" at the end
        if len(message) % 2 == 1:
            message.append("X")
        # Grouping
        i = 0
        new = []
        for x in range(1, int(len(message) / 2 + 1)):
            new.append(message[i:i + 2])
            i = i + 2
        return new

    def find_position(self,key_matrix, letter):
        x = y = 0
        for i in range(5):
            for j in range(5):
                if key_matrix[i][j] == letter:
                    x = i
                    y = j

        return x, y

    def cipher_to_digraphs(self,cipher):
        i = 0
        new = []
        for x in range(int(len(cipher) / 2)):
            new.append(cipher[i:i + 2])
            i = i + 2
        return new

    def decode(self, key, txtBoxValue):
        cdir = os.getcwd()
        decodedFile = cdir + 'Decripted.txt'
        decFile = open(decodedFile,'w')
        #print('from alluser decode', txtBoxValue)
        cipher1 = self.cipher_to_digraphs(txtBoxValue)
        key_matrix = self.matrix(key)
        plaintext = []
        for e in cipher1:
            p1, q1 = self.find_position(key_matrix, e[0])
            p2, q2 = self.find_position(key_matrix, e[1])
            if p1 == p2:
                if q1 == 4:
                    q1 = -1
                if q2 == 4:
                    q2 = -1
                plaintext.append(key_matrix[p1][q1 - 1])
                plaintext.append(key_matrix[p1][q2 - 1])
            elif q1 == q2:
                if p1 == 4:
                    p1 = -1
                if p2 == 4:
                    p2 = -1
                plaintext.append(key_matrix[p1 - 1][q1])
                plaintext.append(key_matrix[p2 - 1][q2])
            else:
                plaintext.append(key_matrix[p1][q2])
                plaintext.append(key_matrix[p2][q1])

        for unused in range(len(plaintext)):
            if "X" in plaintext:
                plaintext.remove("X")

        output = ""
        for e in plaintext:
            output += e
        #decFile.write(output.lower())
        print('PlainText =',output.lower())


    def encode(self,key,txtBxValue):
        cdir = os.getcwd()
        encodedFile = cdir+'code.txt'
        encFile = open(encodedFile,'w')

        #print('from alluser encode', txtBxValue,key)
        msg = self.message_to_digraphs(txtBxValue)
        message1 = msg
        key_matrix = self.matrix(key)
        cipher = []
        for e in message1:
            p1, q1 = self.find_position(key_matrix, e[0])
            p2, q2 = self.find_position(key_matrix, e[1])
            if p1 == p2:  # SAME rows (Y)
                if q1 == 4:
                    q1 = 0
                else:
                    q1 += 1
                if q2 == 4:
                    q2 = 0
                else:
                    q2 += 1
                cipher.append(key_matrix[p1][q1])
                cipher.append(key_matrix[p2][q2])
            elif q1 == q2:
                if p1 == 4:
                    p1 = -1
                if p2 == 4:
                    p2 = -1
                cipher.append(key_matrix[p1 + 1][q1])
                cipher.append(key_matrix[p2 + 1][q2])
            else:
                cipher.append(key_matrix[p1][q2])
                cipher.append(key_matrix[p2][q1])
        encFile.write(''.join(cipher))
        print('Encoded Text',''.join(cipher))


class Selector(Admin, AllUser):
    FLAG = 0

    def __init__(self,FLAG,PathWay,Single,textBox):
        self.FLAG = FLAG
        self.PathWay = PathWay
        self.Single = Single
        self.textBox = textBox

    def frmAll(self):
        self.FLAG = 2
        self.divider(self.FLAG)

    def frmAdm(self):
        Admin.key= self.getKeyLocation()
        # passcode = input("enter Admin code>>")
        # if passcode != 'marvin':
        #     sys.exit(1)
        self.FLAG = 1
        self.divider(self.FLAG)

    def dec(self,txtBoxValue, path):
            Admin.decode(self,txtBoxValue)

    def decU(self,txtBoxValue,key, path):
        cdir = os.getcwd()
        decode = AllUser.decode(self,key,txtBoxValue.upper())
        print(decode)

    def encU(self,txtBoxValue,key, path):
        cdir = os.getcwd()

        encoded = AllUser.encode(self, key, txtBoxValue.upper())
        print(encoded)

    def enc(self,txtBoxValue):
        Admin.encode(self,txtBoxValue)

    def divider(self,FLAG):
        if FLAG % 2 != 0:
            "WE use the Admin class"
            self.Single = self.PathWay[0]
            print('For admin>>',self.Single)

        else:

            """AllUser class"""
            self.Single = self.PathWay[1]
            print('for alluser>>',self.Single)

    def AccessUser(self,txtBoxValue,key):
        print('From AccessUser Decoder>>')

        if key == None:
            self.dec(txtBoxValue,path=self.Single)
        else:
            self.decU(txtBoxValue, key, path=self.Single)

    def AccessUser1(self,txtBoxValue,key):
        print('From AccessUser encoder>>')
        if key == None:
            self.enc(txtBoxValue)
        else:
            self.encU(txtBoxValue,key,path=self.Single)



    def getKeyLocation(self):
        print("To Use This Feature You Need Admin Previledges\n")
        self.adminCode=input("Enter admin code:")
        if self.adminCode != 'mavrano96':
            sys.exit(1)

        keyCont=filedialog.askopenfile('rb')
        try:
            self.key=keyCont.name
            print(self.key)
        except AttributeError:
            print('No KEY registered ')
            sys.exit(1)
        return self.key



class Gui(Selector):

    def __init__(self, name,FLAG,PathWay,Single):
        self.FLAG = FLAG
        self.PathWay = PathWay
        self.Single = Single
        self.textBox = []
        self.KeyValue = None

        # self.dataCon = []
        # self.pdfname = ''
        # self.contentList = []
        # self.contentListSec = []
        self.window = tk.ThemedTk()
        self.window.get_themes()
        self.window.set_theme("plastik")

        self.window.title(name)
        self.window.geometry('1000x550+300+30')
        self.window.resizable(False, False)
        self.window.iconbitmap('soa.ico')
        cdir = os.getcwd()
        """Menu section"""
        menubar = Menu()
        menubarcntent = Menu()
        menukeydir = Menu()
        menuHelp = Menu()

        menubar.add_cascade(label='File', menu=menubarcntent)
        menubarcntent.add_command(label='Open File', command=self.openFile)
        menubarcntent.add_command(label='clear memory', command=self.clearCaheMem)
        menubarcntent.add_command(label='Delete Previous file', command=self.deleteCode)

        menubar.add_cascade(label="Kifunguo", menu=menukeydir)
        menukeydir.add_command(label="Normal Key", command=self.normalKey)
        menukeydir.add_command(label="Admin Key", command=self.komplexKey)

        menubar.add_cascade(label="help", menu=menuHelp)
        menuHelp.add_command(label="Hola the Developer(L)")
        self.window.config(menu=menubar)

        # self.textBox = ttk.Text(self.window, height=30, bg='gray', bd=20)
        self.textBox = Text(self.window, height=30, bg='gray', bd=20)
        self.textBox.place(x=0, y=0)

        # encodeButton = Button(self.window, text='< ENCODE >', width=20, height=8, bg='lime', activebackground='red', bd=10,
        #                       font='helvitica', command=self.encodingKey)
        encodeButton = ttk.Button(self.window, text='< ENCODE >', width=20, command=self.encodingKey)
        encodeButton.place(x=750, y=1)
        # decodeButton = Button(self.window, text='< DECODE >', width=20, height=8, bg='brown', activebackground='red', bd=10,
        #                       font='helvitica', command=self.decodingKey)
        decodeButton = ttk.Button(self.window, text='< DECODE >', width=20, command=self.decodingKey)
        decodeButton.place(x=750, y=210)
        self.window.mainloop()



    def getTextBox(self):
        self.fileData = self.textBox.get("1.0", "end-1c")
        return self.fileData

    def normalKey(self):
        Selector.frmAll(self)
        self.allUserKey()

    def komplexKey(self):
        Selector.frmAdm(self)

    def decodingKey(self):
        Selector.AccessUser(self, self.getTextBox(),self.getKey())

    def encodingKey(self):
        Selector.AccessUser1(self, self.getTextBox(), self.getKey())

    def allUserKey(self):
        a = StringVar()
        lab = Label(text='Enter Key(TXT)', font='elephant', fg='red')
        lab.place(x=750, y=405)
        keyEntry = Entry(self.window, textvariable=a, width=23, bd=5, bg='pink', font='helvetica')
        keyEntry.place(x=750, y=430)
        #enterBut = Button(text='Enter', width=30, height=2, bg='gray', bd=2, command=lambda: self.getEntry(a))
        enterBut = Button(text='Enter', width=30, bg='gray', bd=2, command=lambda: self.getEntry(a))
        enterBut.place(x=750, y=467)

    def getEntry(self,a):
        # a = StringVar()
        print('KEY ENTERED')
        txtCont = a.get().upper()
        self.KeyValue = txtCont
    def getKey(self):
        return self.KeyValue

    def clearCaheMem(self):
        Admin.clearCache(self)

    def deleteCode(self):
        cdir = os.getcwd()
        if os.path.exists('replica.txt') or os.path.exists(cdir + 'code.txt') or os.path.exists(cdir + 'original.txt'):
            try:
                os.remove('replica.txt')
            except FileNotFoundError:
                print('deamon file cleared')
            finally:
                try:
                    os.remove(cdir + 'code.txt')
                except FileNotFoundError:
                    print('Coded file already cleared')
                finally:
                    try:
                        os.remove(cdir + 'original.txt')
                    except FileNotFoundError:
                        print('Original file already cleared')
        else:
            print('Files do not exist')

    def openFile(self):
        file = filedialog.askopenfile()
        try:
            filebuffer = file.read().lower()
            if len(Admin.dataCon) == 0:
                try:
                    Admin.dataCon.extend(filebuffer)
                except UnboundLocalError:
                    print('No Detectable Entry')

            else:
                print('clear cache')
                Admin.clearCache(self)
                Gui.openFile(self)
        except AttributeError:
            messagebox.showinfo('Error', 'no file text was selected')

        print('fileContent char size ', len(''.join(Admin.dataCon)))


def main():
    PathWay = ['Admin', 'AllUser']
    Single = []  #this will get the single pathway
    Gui('CB~enigma', 0, PathWay, Single)
    #selecta=Selector(0,PathWay,Single)


if __name__ == '__main__':
    main()

