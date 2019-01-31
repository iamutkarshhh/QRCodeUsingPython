import pyqrcode
#TO import the pip file in cmd --> pip install pyqrcode
#After Succesfully downloading the file you need to update it using command --> python -m pip install --upgrade pip
#It will automatically get updated and will run Sucessfully
def qrcode():
    #We need to create a Variable first where we will store the link of our Qr Code
    s = "www.google.com"
    #Create another Variable where we will actually create the qrcode passing our
    #variable as a parameter
    url = pyqrcode.create(s)
    #pass the second variable as a .svg having 2 parameters firsst will be the name
    #of our QR code the second wil be our sixe of the QR code
    url.svg("myqr.svg",scale=6)
    print("QR Code Generated")

if __name__=='__main__':
    qrcode()
