import openpyxl #imports the openpyxl module to be able to use and work with excel sheets
path = 'PhoneFlippingGradingScale.xlsx' #this is the filename
wb = openpyxl.load_workbook(path) #loads the excel sheet to be able to read from it
usedIphoneSheet = wb.get_sheet_by_name('USED IPHONE') #links to the exact sheet

#A class for the main border which iwll be used 
class MenuBorder(): 
    def border(self):
        print(' ')
        for i in range(30):
            print(" *", end='')
        print('\n')

#A class with the grading scale specifics 
class GradingScale():
    def gradingRubric(self):
        print('\n\n')
        for i in range(53): #specific border menu for the Grading scale
            print(" *", end = "")
        print('\n\n\t\t\t\t    📝 Grading Scale 📝:')
        print('\n\tA Grade: Fully functional, perfect condition, no dents or scratches')
        print('\tB Grade: Fully functional, dents or scratches present. No Heavy/deep scratches')
        print('\tC Grade: Fully functional, heavy dents or scratches, lcd lines/spots, NO blackout LCD')
        print('\tD Grade: Fully functional, heavy dents/scratches or cracked, lcd lines./spots, no missing parts\n')
        for i in range(53): #specific border menu for the Grading Scale
            print(" *", end = "")

#This is a class that stores the average sale price of each phone
class AverageSalePrice():
    #iPhone 7 Average Sale Prices
    _iPhone7UL32GbAverage = usedIphoneSheet['C19'].value #Cell position for an average price of an 32gb unlocked iPhone 7
    _iPhone7UL128GbAverage = usedIphoneSheet['C20'].value #Cell position for an average price of an 128gb unlocked iPhone 7
    _iPhone7UL256GbAverage = usedIphoneSheet['C21'].value #Cell position for an average price of an 256gb unlocked iPhone 7
    _iPhone7L32GbAverage = usedIphoneSheet['C22'].value #Cell position for an average price of an 32gb locked iPhone 7
    _iPhone7L128GbAverage = usedIphoneSheet['C23'].value #Cell position for an average price of an 128gb locked iPhone 7
    _iPhone7L256GbAverage = usedIphoneSheet['C24'].value #Cell position for an average price of an 256gb locked iPhone 7
    #iPhone 7 Plus Average Sale Prices
    _iPhone7PlusUL32GbAverage = usedIphoneSheet['C28'].value #Cell position for an average price of an 32gb unlocked iPhone 7 Plus
    _iPhone7PlusUL128GbAverage = usedIphoneSheet['C29'].value #Cell position for an average price of an 128gb unlocked iPhone 7 Plus
    _iPhone7PlusUL256GbAverage = usedIphoneSheet['C30'].value #Cell position for an average price of an 256gb unlocked iPhone 7 Plus
    _iPhone7PlusL32GbAverage = usedIphoneSheet['C31'].value #Cell position for an average price of an 32gb locked iPhone 7 Plus
    _iPhone7PlusL128GbAverage = usedIphoneSheet['C32'].value #Cell position for an average price of an 128gb locked iPhone 7 Plus
    _iPhone7PlusL256GbAverage = usedIphoneSheet['C33'].value #Cell position for an average price of an 256gb locked iPhone 7 Plus

#This is a class that stores the cell positions for the phone prices 
class CellPositions():
    #Unlocked & Locked iPhone 7 Prices
   _iPhone7UL32GbAHigh = usedIphoneSheet['D19'].value #Cell position for A Grade High offer of an iPhone 7 unlocked 32Gb 
   _iPhone7UL32GbALow = usedIphoneSheet['E19'].value #Cell position for A Grade Low offer of an iPhone 7 unlocked 32GB 
   _iPhone7UL32GbBHigh = usedIphoneSheet['F9'].value #Cell position for B Grade High offer of an iPhone 7 unlocked 32GB 
   _iPhone7UL32GbBLow = usedIphoneSheet['G19'].value #Cell position for B Grade Low offer of an iPhone 7 unlocked 32GB 
   _iPhone7UL32GbCHigh = usedIphoneSheet['H19'].value #Cell position for C Grade High offer of an iPhone 7 unlocked 32GB
   _iPhone7UL32GbCLow = usedIphoneSheet['I19'].value #Cell position for C Grade Low offer of an iPhone 7 unlocked 32GB
   _iPhone7UL32GbDHigh = usedIphoneSheet['J19'].value #Cell position for D Grade High offer of an iPhone 7 unlocked 32GB 
   _iPhone7UL32GbDLow = usedIphoneSheet['K19'].value #Cell position for D Grade Low offer of an iPhone 7 unlocked 32GB
   _iPhone7UL128GbAHigh = usedIphoneSheet['D20'].value #Cell position for A Grade High offer of an iPhone 7 unlocked 128Gb
   _iPhone7UL128GbALow = usedIphoneSheet['E20'].value #Cell position for A Grade Low offer of an iPhone 7 unlocked 128Gb
   _iPhone7UL128GbBHigh = usedIphoneSheet['F20'].value #Cell position for B Grade High offer of an iPhone 7 unlocked 128Gb
   _iPhone7UL128GbBLow = usedIphoneSheet['G20'].value #Cell position for B Grade Low offer of an iPhone 7 unlocked 128Gb
   _iPhone7UL128GbCHigh = usedIphoneSheet['H20'].value #Cell position for C Grade High offer of an iPhone 7 unlocked 128Gb
   _iPhone7UL128GbCLow = usedIphoneSheet['I20'].value #Cell position for C Grade Low offer of an iPhone 7 unlocked 128Gb
   _iPhone7UL128GbDHigh = usedIphoneSheet['J20'].value #Cell position for D Grade High offer of an iPhone 7 unlocked 128Gb
   _iPhone7UL128GbDlow = usedIphoneSheet['K20'].value #Cell position for D Grade Low offer of an iPhone 7 unlocked 128Gb
   _iPhone7UL256GbAHigh = usedIphoneSheet['D21'].value #Cell position for A Grade High offer of an iPhone 7 unlocked 256Gb
   _iPhone7UL256GbALow = usedIphoneSheet['E21'].value #Cell position for A Grade Low offer of an iPhone 7 unlocked 256Gb
   _iPhone7UL256GbBHigh = usedIphoneSheet['F21'].value #Cell position for B Grade High offer of an iPhone 7 unlocked 256Gb
   _iPhone7UL256GbBLow = usedIphoneSheet['G21'].value #Cell position for B Grade Low offer of an iPhone 7 unlocked 256Gb
   _iPhone7UL256GbCHigh = usedIphoneSheet['H21'].value #Cell position for C Grade High offer of an iPhone 7 unlocked 256Gb
   _iPhone7UL256GbCLow= usedIphoneSheet['I21'].value #Cell position for C Grade Low offer of an iPhone 7 unlocked 256Gb
   _iPhone7UL256GbDHigh = usedIphoneSheet['J21'].value #Cell position for D Grade High offer of an iPhone 7 unlocked 256Gb
   _iPhone7UL256GbDLow = usedIphoneSheet['K21'].value #Cell position for D Grade Low offer of an iPhone 7 unlocked 256Gb
   _iPhone7L32GbAHigh = usedIphoneSheet['D22'].value #Cell position for A Grade High offer of an iPhone 7 locked 32Gb 
   _iPhone7L32GbALow = usedIphoneSheet['E22'].value #Cell position for A Grade Low offer of an iPhone 7 locked 32GB 
   _iPhone7L32GbBHigh = usedIphoneSheet['F22'].value #Cell position for B Grade High offer of an iPhone 7 locked 32GB 
   _iPhone7L32GbBLow = usedIphoneSheet['G22'].value #Cell position for B Grade Low offer of an iPhone 7 locked 32GB 
   _iPhone7L32GbCHigh = usedIphoneSheet['H22'].value #Cell position for C Grade High offer of an iPhone 7 locked 32GB
   _iPhone7L32GbCLow = usedIphoneSheet['I22'].value #Cell position for C Grade Low offer of an iPhone 7 locked 32GB
   _iPhone7L32GbDHigh = usedIphoneSheet['J22'].value #Cell position for D Grade High offer of an iPhone 7 locked 32GB 
   _iPhone7L32GbDLow = usedIphoneSheet['K22'].value #Cell position for D Grade Low offer of an iPhone 7 locked 32GB
   _iPhone7L128GbAHigh = usedIphoneSheet['D23'].value #Cell position for A Grade High offer of an iPhone 7 locked 128Gb
   _iPhone7L128GbALow = usedIphoneSheet['E23'].value #Cell position for A Grade Low offer of an iPhone 7 locked 128Gb
   _iPhone7L128GbBHigh = usedIphoneSheet['F23'].value #Cell position for B Grade High offer of an iPhone 7 locked 128Gb
   _iPhone7L128GbBLow = usedIphoneSheet['G23'].value #Cell position for B Grade Low offer of an iPhone 7 locked 128Gb
   _iPhone7L128GbCHigh = usedIphoneSheet['H23'].value #Cell position for C Grade High offer of an iPhone 7 locked 128Gb
   _iPhone7L128GbCLow = usedIphoneSheet['I23'].value #Cell position for C Grade Low offer of an iPhone 7 locked 128Gb
   _iPhone7L128GbDHigh = usedIphoneSheet['J23'].value #Cell position for D Grade High offer of an iPhone 7 locked 128Gb
   _iPhone7L128GbDlow = usedIphoneSheet['K23'].value #Cell position for D Grade Low offer of an iPhone 7 locked 128Gb
   _iPhone7L256GbAHigh = usedIphoneSheet['D24'].value #Cell position for A Grade High offer of an iPhone 7 locked 256Gb
   _iPhone7L256GbALow = usedIphoneSheet['E24'].value #Cell position for A Grade Low offer of an iPhone 7 locked 256Gb
   _iPhone7L256GbBHigh = usedIphoneSheet['F24'].value #Cell position for B Grade High offer of an iPhone 7 locked 256Gb
   _iPhone7L256GbBLow = usedIphoneSheet['G24'].value #Cell position for B Grade Low offer of an iPhone 7 locked 256Gb
   _iPhone7L256GbCHigh = usedIphoneSheet['H24'].value #Cell position for C Grade High offer of an iPhone 7 locked 256Gb
   _iPhone7L256GbCLow= usedIphoneSheet['I24'].value #Cell position for C Grade Low offer of an iPhone 7 locked 256Gb
   _iPhone7L256GbDHigh = usedIphoneSheet['J24'].value #Cell position for D Grade High offer of an iPhone 7 locked 256Gb
   _iPhone7L256GbDLow = usedIphoneSheet['K24'].value #Cell position for D Grade Low offer of an iPhone 7 locked 256Gb
   #Unlocked and Locked iPhone 7 Plus Prices
   _iPhone7PlusUL32GbAHigh = usedIphoneSheet['D28'].value #Cell position for A Grade High offer of an iPhone 7 Plus unlocked 32Gb 
   _iPhone7PlusUL32GbALow = usedIphoneSheet['E28'].value #Cell position for A Grade Low offer of an iPhone 7 Plus unlocked 32GB 
   _iPhone7PlusUL32GbBHigh = usedIphoneSheet['28'].value #Cell position for B Grade High offer of an iPhone 7 Plus unlocked 32GB 
   _iPhone7PlusUL32GbBLow = usedIphoneSheet['G28'].value #Cell position for B Grade Low offer of an iPhone 7 Plus unlocked 32GB 
   _iPhone7PlusUL32GbCHigh = usedIphoneSheet['H28'].value #Cell position for C Grade High offer of an iPhone 7 Plus unlocked 32GB
   _iPhone7PlusUL32GbCLow = usedIphoneSheet['I28'].value #Cell position for C Grade Low offer of an iPhone 7 Plus unlocked 32GB
   _iPhone7PlusUL32GbDHigh = usedIphoneSheet['J28'].value #Cell position for D Grade High offer of an iPhone 7 Plus unlocked 32GB 
   _iPhone7PlusUL32GbDLow = usedIphoneSheet['K28'].value #Cell position for D Grade Low offer of an iPhone 7 Plus unlocked 32GB
   _iPhone7PlusUL128GbAHigh = usedIphoneSheet['D29'].value #Cell position for A Grade High offer of an iPhone 7 Plus unlocked 128Gb
   _iPhone7PlusUL128GbALow = usedIphoneSheet['E29'].value #Cell position for A Grade Low offer of an iPhone 7 Plus unlocked 128Gb
   _iPhone7PlusUL128GbBHigh = usedIphoneSheet['F29'].value #Cell position for B Grade High offer of an iPhone 7 Plus unlocked 128Gb
   _iPhone7PlusUL128GbBLow = usedIphoneSheet['G29'].value #Cell position for B Grade Low offer of an iPhone 7 Plus unlocked 128Gb
   _iPhone7PlusUL128GbCHigh = usedIphoneSheet['H29'].value #Cell position for C Grade High offer of an iPhone 7 Plus unlocked 128Gb
   _iPhone7PlusUL128GbCLow = usedIphoneSheet['I29'].value #Cell position for C Grade Low offer of an iPhone 7 Plus unlocked 128Gb
   _iPhone7PlusUL128GbDHigh = usedIphoneSheet['J29'].value #Cell position for D Grade High offer of an iPhone 7 Plus unlocked 128Gb
   _iPhone7PlusUL128GbDlow = usedIphoneSheet['K29'].value #Cell position for D Grade Low offer of an iPhone 7 Plus unlocked 128Gb
   _iPhone7PlusUL256GbAHigh = usedIphoneSheet['D30'].value #Cell position for A Grade High offer of an iPhone 7 Plus unlocked 256Gb
   _iPhone7PlusUL256GbALow = usedIphoneSheet['E30'].value #Cell position for A Grade Low offer of an iPhone 7 Plus unlocked 256Gb
   _iPhone7PlusUL256GbBHigh = usedIphoneSheet['F30'].value #Cell position for B Grade High offer of an iPhone 7 Plus unlocked 256Gb
   _iPhone7PlusUL256GbBLow = usedIphoneSheet['G30'].value #Cell position for B Grade Low offer of an iPhone 7 Plus unlocked 256Gb
   _iPhone7PlusUL256GbCHigh = usedIphoneSheet['H30'].value #Cell position for C Grade High offer of an iPhone 7 Plus unlocked 256Gb
   _iPhone7PlusUL256GbCLow= usedIphoneSheet['I30'].value #Cell position for C Grade Low offer of an iPhone 7 Plus unlocked 256Gb
   _iPhone7PlusUL256GbDHigh = usedIphoneSheet['J30'].value #Cell position for D Grade High offer of an iPhone 7 Plus unlocked 256Gb
   _iPhone7PlusUL256GbDLow = usedIphoneSheet['K30'].value #Cell position for D Grade Low offer of an iPhone 7 Plus unlocked 256Gb
   _iPhone7PlusL32GbAHigh = usedIphoneSheet['D31'].value #Cell position for A Grade High offer of an iPhone 7 Plus locked 32Gb 
   _iPhone7PlusL32GbALow = usedIphoneSheet['E31'].value #Cell position for A Grade Low offer of an iPhone 7 Plus locked 32GB 
   _iPhone7PlusL32GbBHigh = usedIphoneSheet['F31'].value #Cell position for B Grade High offer of an iPhone 7 Plus locked 32GB 
   _iPhone7PlusL32GbBLow = usedIphoneSheet['G31'].value #Cell position for B Grade Low offer of an iPhone 7 Plus locked 32GB 
   _iPhone7PlusL32GbCHigh = usedIphoneSheet['H31'].value #Cell position for C Grade High offer of an iPhone 7 Plus locked 32GB
   _iPhone7PlusL32GbCLow = usedIphoneSheet['I31'].value #Cell position for C Grade Low offer of an iPhone 7 Plus locked 32GB
   _iPhone7PlusL32GbDHigh = usedIphoneSheet['J31'].value #Cell position for D Grade High offer of an iPhone 7 Plus locked 32GB 
   _iPhone7PlusL32GbDLow = usedIphoneSheet['K31'].value #Cell position for D Grade Low offer of an iPhone 7 Plus locked 32GB
   _iPhone7PlusL128GbAHigh = usedIphoneSheet['D32'].value #Cell position for A Grade High offer of an iPhone 7 Plus locked 128Gb
   _iPhone7PlusL128GbALow = usedIphoneSheet['E32'].value #Cell position for A Grade Low offer of an iPhone 7 Plus locked 128Gb
   _iPhone7PlusL128GbBHigh = usedIphoneSheet['F32'].value #Cell position for B Grade High offer of an iPhone 7 Plus locked 128Gb
   _iPhone7PlusL128GbBLow = usedIphoneSheet['G32'].value #Cell position for B Grade Low offer of an iPhone 7 Plus locked 128Gb
   _iPhone7PlusL128GbCHigh = usedIphoneSheet['H32'].value #Cell position for C Grade High offer of an iPhone 7 Plus locked 128Gb
   _iPhone7PlusL128GbCLow = usedIphoneSheet['I32'].value #Cell position for C Grade Low offer of an iPhone 7 Plus locked 128Gb
   _iPhone7PlusL128GbDHigh = usedIphoneSheet['J32'].value #Cell position for D Grade High offer of an iPhone 7 Plus locked 128Gb
   _iPhone7PlusL128GbDlow = usedIphoneSheet['K32'].value #Cell position for D Grade Low offer of an iPhone 7 Plus locked 128Gb
   _iPhone7PlusL256GbAHigh = usedIphoneSheet['D33'].value #Cell position for A Grade High offer of an iPhone 7 Plus locked 256Gb
   _iPhone7PlusL256GbALow = usedIphoneSheet['E33'].value #Cell position for A Grade Low offer of an iPhone 7 Plus locked 256Gb
   _iPhone7PlusL256GbBHigh = usedIphoneSheet['F33'].value #Cell position for B Grade High offer of an iPhone 7 Plus locked 256Gb
   _iPhone7PlusL256GbBLow = usedIphoneSheet['G33'].value #Cell position for B Grade Low offer of an iPhone 7 Plus locked 256Gb
   _iPhone7PlusL256GbCHigh = usedIphoneSheet['H33'].value #Cell position for C Grade High offer of an iPhone 7 Plus locked 256Gb
   _iPhone7PlusL256GbCLow= usedIphoneSheet['I33'].value #Cell position for C Grade Low offer of an iPhone 7 Plus locked 256Gb
   _iPhone7PlusL256GbDHigh = usedIphoneSheet['J33'].value #Cell position for D Grade High offer of an iPhone 7 Plus locked 256Gb
   _iPhone7PlusL256GbDLow = usedIphoneSheet['K33'].value #Cell position for D Grade Low offer of an iPhone 7 Plus locked 256Gb






#Main Source Code 
supportedPhones = {0: 'Grading Scale 📝', 1: 'iPhone 7 📱', 2: 'iPhone 7 Plus 📱', 3: 'iPhone 8 📱', 4: 'iPhone 8 Plus 📱', 5: 'iPhone X 📱', 6: 'iPhone XR 📱', 7: 'iPhone XS 📱', 8: 'iPhone XS Max 📱', 9: 'iPhone 11 📱', 10: 'iPhone 11 Pro 📱', 11: 'iPhone 11 Pro Max 📱'} #list of phones to choose from
phoneOption = False #creates a variable for the following loop
while phoneOption == False: #loop for the program to stay in so the user can continue or exit after checking on one phone
    MenuBorder.border('*') #anytime you see this it is calling the Menu Border class to create a menu border 
    print('\t\t     🗳  Menu Options 🗳 :\n')
    for key, value in supportedPhones.items(): #Prints each items key and value in the supportedPhones Dict
        print('\t\t   ', key, ':', value)
    MenuBorder.border('*')
    phoneOption = True
    yourOption = int(input('\n\nEnter the number of the phone you would like a price for: '))
    if yourOption == 0: #Option for the Grading Scale 
        GradingScale.gradingRubric(print)
        print('\n\n')
        #Confirmation message to either continue the program or quit it
        confirmationMesage = input('\nWould you like to check another phone? Enter Y for yes or an N for no: ').upper()
        if confirmationMesage == 'Y':
            phoneOption = False
        elif confirmationMesage == 'N':
            print('\nThank you for using this program')
            phoneOption = True
        else:
            print('you entered an invalid charachter')
            confirmationMesage = input('\nWould you like to check another phone? Enter Y for yes or an N for no: ').upper()
    elif yourOption == 1:
        print(usedIphoneSheet['D19'].value)



        