from tkinter import *
import speedtest


interDownload = '0'
interUpload = '0'
interPing = '0'


def runSpeedTest():
    downloadLable.config(text='loading... please wait :)')

    test = speedtest.Speedtest()

    global interDownload, interPing, interUpload
    download_result = test.download()
    download_result = download_result / 1024 / 1024
    upload_result = test.upload()
    upload_result = upload_result/1024/1024
    ping_result = test.results.ping

    interDownload = "{0:.2f}".format(download_result)
    interUpload = "{0:.2f}".format(upload_result)
    interPing = ping_result

    print(f' download {interDownload}')
    print(f' ulpoad {interUpload}')
    print(f' ping {interPing}')

    downloadLable.config(text=f'download speed:{interDownload} Mb/s')
    uploadLable.config(text=f'upload speed:{interUpload} Mb/s')
    pingLable.config(text=f'ping:{interPing} ms')

    if float(interDownload) > 0:
        btnRun.config(text='rerun test')
    print(u'done \N{check mark}')
    return interDownload, interPing, interUpload


window = Tk()
window.title('internet test by shaaban\'s industries')
window.geometry("600x300")
window.resizable(False, False)
#######################################################
w = Label(window, text='Test Your Internet Speed',
          fg="black", font=("Arial", 25))
w.pack()


downloadLable = Label(
    window, text='', font=("Arial", 15))

uploadLable = Label(
    window, text='', font=("Arial", 15))

pingLable = Label(
    window, text='', font=("Arial", 15))

downloadLable.pack()
uploadLable.pack()
pingLable.pack()
#######################################################
btnExit = Button(window, text='Exit', bd='5',
                 command=window.destroy)
btnExit.place(x=475, y=250)

btnRun = Button(window, text='run test', bd='5',
                command=runSpeedTest)
btnRun.place(x=525, y=250)


window.mainloop()
