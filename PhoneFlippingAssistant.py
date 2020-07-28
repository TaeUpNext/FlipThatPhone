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
    _iPhone7UL32GbAverage = usedIphoneSheet['C19'].value #Cell position for an average price of a 32gb unlocked iPhone 7
    _iPhone7UL128GbAverage = usedIphoneSheet['C20'].value #Cell position for an average price of a 128gb unlocked iPhone 7
    _iPhone7UL256GbAverage = usedIphoneSheet['C21'].value #Cell position for an average price of a 256gb unlocked iPhone 7
    _iPhone7L32GbAverage = usedIphoneSheet['C22'].value #Cell position for an average price of a 32gb locked iPhone 7
    _iPhone7L128GbAverage = usedIphoneSheet['C23'].value #Cell position for an average price of a 128gb locked iPhone 7
    _iPhone7L256GbAverage = usedIphoneSheet['C24'].value #Cell position for an average price of a 256gb locked iPhone 7
    #iPhone 7 Plus Average Sale Prices
    _iPhone7PlusUL32GbAverage = usedIphoneSheet['C28'].value #Cell position for an average price of a 32gb unlocked iPhone 7 Plus
    _iPhone7PlusUL128GbAverage = usedIphoneSheet['C29'].value #Cell position for an average price of a 128gb unlocked iPhone 7 Plus
    _iPhone7PlusUL256GbAverage = usedIphoneSheet['C30'].value #Cell position for an average price of a 256gb unlocked iPhone 7 Plus
    _iPhone7PlusL32GbAverage = usedIphoneSheet['C31'].value #Cell position for an average price of a 32gb locked iPhone 7 Plus
    _iPhone7PlusL128GbAverage = usedIphoneSheet['C32'].value #Cell position for an average price of a 128gb locked iPhone 7 Plus
    _iPhone7PlusL256GbAverage = usedIphoneSheet['C33'].value #Cell position for an average price of a 256gb locked iPhone 7 Plus
    #iPhone 8 Average Sale Prices
    _iPhone8UL64GbAverage = usedIphoneSheet['C37'].value #Cell Position for an average price of a 64Gb unlocked iPhone 8
    _iPhone8UL256GbAverage = usedIphoneSheet['C38'].value #Cell Position for an average price of a 256Gb unlocked iPhone 8
    _iPhone8L64GbAverage = usedIphoneSheet['C39'].value #Cell Position for an average price of a 64Gb locked iPhone 8
    _iPhone8L256GbAverage = usedIphoneSheet['C40'].value #Cell Position for an average price of a 256Gb locked iPhone 8
    #iPhone 8 Plus
    _iPhone8PlusUL64GbAverage = usedIphoneSheet['C44'].value #Cell Position for an average price of a 64Gb unlocked iPhone 8 Plus
    _iPhone8PlusUL256GbAverage = usedIphoneSheet['C45'].value #Cell Position for an average price of a 256Gb unlocked iPhone 8 Plus
    _iPhone8PlusL64GbAverage = usedIphoneSheet['C46'].value #Cell Position for an average price of a 64Gb locked iPhone 8 Plus
    _iPhone8PlusL256GbAverage = usedIphoneSheet['C47'].value #Cell Position for an average price of a 256Gb locked iPhone 8 Plus
   #iPhone X Average Sale Prices 
    _iPhoneXUL64GbAverage = usedIphoneSheet['C51'].value #Cell Position for an average price of a 64Gb unlocked iPhone X
    _iPhoneXUL256GbAverage = usedIphoneSheet['C52'].value #Cell Position for an average price of a 256Gb unlocked iPhone X
    _iPhoneXL64GbAverage = usedIphoneSheet['C53'].value #Cell Position for an average price of a 64Gb locked iPhone X
    _iPhoneXL256GbAverage = usedIphoneSheet['C54'].value #Cell Position for an average price of a 256Gb locked iPhone X
    #iPhone XR Average Sales Price 
    _iPhoneXRUL64GbAverage = usedIphoneSheet['C58'].value #Cell position for an average price of a 64Gb unlocked iPhone X
    _iPhoneXRUL128GbAverage = usedIphoneSheet['C59'].value #Cell position for an average price of a 128Gb unlocked iPhone X
    _iPhoneXRUL256GbAverage = usedIphoneSheet['C60'].value #Cell position for an average price of a 256Gb unlocked iPhone X
    _iPhoneXRL64GbAverage = usedIphoneSheet['C61'].value #Cell position for an average price of a 64Gb unlocked iPhone X
    _iPhoneXRL128GbAverage = usedIphoneSheet['C62'].value #Cell position for an average price of a 128Gb unlocked iPhone X
    _iPhoneXRL256GbAverage = usedIphoneSheet['C63'].value #Cell position for an average price of a 256Gb unlocked iPhone X
    #iPhone XS Average Sales Price
    _iPhoneXSUL64GbAverage = usedIphoneSheet['C67'].value #Cell position for an average price of a 64Gb unlocked iPhone XS
    _iPhoneXSUL256GbAverage = usedIphoneSheet['C68'].value #Cell position for an average price of a 256Gb unlocked iPhone XS
    _iPhoneXSUL512GbAverage = usedIphoneSheet['C69'].value #Cell position for an average price of a 512Gb unlocked iPhone XS
    _iPhoneXSL64GbAverage = usedIphoneSheet['C70'].value #Cell position for an average price of a 64Gb unlocked iPhone XS
    _iPhoneXSL256GbAverage = usedIphoneSheet['C71'].value #Cell position for an average price of a 256Gb unlocked iPhone XS
    _iPhoneXSL512GbAverage = usedIphoneSheet['C72'].value #Cell position for an average price of a 512Gb unlocked iPhone XS
    #iPhone XS Max Average Sales Price
    _iPhoneXSMaxUL64GbAverage = usedIphoneSheet['C76'].value #Cell position for an average price of a 64Gb unlocked iPhone XS Max
    _iPhoneXSMaxUL256GbAverage = usedIphoneSheet['C77'].value #Cell position for an average price of a 256Gb unlocked iPhone XS Max
    _iPhoneXSMaxUL512GbAverage = usedIphoneSheet['C78'].value #Cell position for an average price of a 512Gb unlocked iPhone XS Max
    _iPhoneXSMaxL64GbAverage = usedIphoneSheet['C79'].value #Cell position for an average price of a 64Gb unlocked iPhone XS Max
    _iPhoneXSMaxL256GbAverage = usedIphoneSheet['C80'].value #Cell position for an average price of a 256Gb unlocked iPhone XS Max 
    _iPhoneXSMaxL512GbAverage = usedIphoneSheet['C81'].value #Cell position for an average price of a 512Gb unlocked iPhone XS Max 
    #iPhone 11 Average Sales Price 
    _iPhone11UL64GbAverage = usedIphoneSheet['C86'].value #Cell position for an average price of a 64Gb unlocked iPhone 11
    _iPhone11UL128GbAverage = usedIphoneSheet['C87'].value #Cell position for an average price of a 128Gb unlocked iPhone 11
    _iPhone11UL256GbAverage = usedIphoneSheet['C88'].value #Cell position for an average price of a 256Gb unlocked iPhone 11
    _iPhone11L64GbAverage = usedIphoneSheet['C89'].value #Cell position for an average price of a 64Gb unlocked iPhone 11
    _iPhone11L128GbAverage = usedIphoneSheet['C90'].value #Cell position for an average price of a 128Gb unlocked iPhone 11
    _iPhone11L256GbAverage = usedIphoneSheet['C91'].value #Cell position for an average price of a 256Gb unlocked iPhone 11
    #iPhone 11 Pro Average Sales Price
    _iPhone11ProUL64GbAverage = usedIphoneSheet['C95'].value #Cell position for an average price of a 64Gb unlocked iPhone 11 Pro
    _iPhone11ProUL256GbAverage = usedIphoneSheet['C96'].value #Cell position for an average price of a 256Gb unlocked iPhone 11 Pro
    _iPhone11ProUL512GbAverage = usedIphoneSheet['C97'].value #Cell position for an average price of a 512Gb unlocked iPhone 11 Pro
    _iPhone11ProL64GbAverage = usedIphoneSheet['C98'].value #Cell position for an average price of a 64Gb unlocked iPhone 11 Pro
    _iPhone11ProL256GbAverage = usedIphoneSheet['C99'].value #Cell position for an average price of a 256Gb unlocked iPhone 11 Pro
    _iPhone11ProL512GbAverage = usedIphoneSheet['C100'].value #Cell position for an average price of a 512Gb unlocked iPhone 11 pro 
     #iPhone 11 Pro Max Average Sales Price
    _iPhone11ProMaxUL64GbAverage = usedIphoneSheet['C104'].value #Cell position for an average price of a 64Gb unlocked iPhone 11 Pro Max
    _iPhone11PromaxUL256GbAverage = usedIphoneSheet['C105'].value #Cell position for an average price of a 256Gb unlocked iPhone 11 Pro Max
    _iPhone11ProMaxUL512GbAverage = usedIphoneSheet['C106'].value #Cell position for an average price of a 512Gb unlocked iPhone 11 Pro Max
    _iPhone11ProMaxL64GbAverage = usedIphoneSheet['C107'].value #Cell position for an average price of a 64Gb unlocked iPhone 11 Pro Max 
    _iPhone11PromaxUL256GbAverage = usedIphoneSheet['C108'].value #Cell position for an average price of a 256Gb unlocked iPhone 11 Pro Max
    _iPhone11ProL512GbAverage = usedIphoneSheet['C109'].value #Cell position for an average price of a 512Gb unlocked iPhone 11 pro Max 










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
   #
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
   #unlocked & Locked iPhone 8 Prices
   #
   _iPhone8UL64GbAHigh = usedIphoneSheet['D37'].value #Cell position for A Grade High of a iPhone 8 Unlocked 64Gb
   _iPhone8UL64GbALow = usedIphoneSheet['E37'].value #Cell position for A Grade Low of a iPhone 8 Unlocked 64Gb
   _iPhone8UL64GbBHigh = usedIphoneSheet['F37'].value #Cell position for B Grade High of a iPhone 8 Unlocked 64Gb
   _iPhone8UL64GbBLow= usedIphoneSheet['G37'].value #Cell position for B Grade Low of a iPhone 8 Unlocked 64Gb
   _iPhone8UL64GbCHigh = usedIphoneSheet['H37'].value #Cell position for C Grade High of an iPhone 8 Unlocked 64Gb
   _iPhone8UL64GbCLow= usedIphoneSheet['I37'].value #Cell position for C Grade Low of an iPhone 8 Unlocked 64Gb
   _iPhone8UL64GbDHigh = usedIphoneSheet['J37'].value #Cell position for D Grade High of an iPhone 8 Unlocked 64Gb
   _iPhone8UL64GbDLow = usedIphoneSheet['K37'].value #Cell position for D Grade Low of an iPhone 8 Unlocked 64Gb
   _iPhone8UL256GbAHigh = usedIphoneSheet['D38'].value #Cell position for A Grade High of a iPhone 8 Unlocked 256Gb
   _iPhone8UL256GbALow = usedIphoneSheet['E38'].value #Cell position for A Grade Low of a iPhone 8 Unlocked 256Gb
   _iPhone8UL256GbBHigh = usedIphoneSheet['F38'].value #Cell position for B Grade High of a iPhone 8 Unlocked 256Gb
   _iPhone8UL256GbBLow= usedIphoneSheet['G38'].value #Cell position for B Grade Low of a iPhone 8 Unlocked 256Gb
   _iPhone8UL256GbCHigh = usedIphoneSheet['H38'].value #Cell position for C Grade High of an iPhone 8 Unlocked 256Gb
   _iPhone8UL256GbCLow= usedIphoneSheet['I38'].value #Cell position for C Grade Low of an iPhone 8 Unlocked 256Gb
   _iPhone8UL256GbDHigh = usedIphoneSheet['J38'].value #Cell position for D Grade High of an iPhone 8 Unlocked 256Gb
   _iPhone8UL256GbDLow = usedIphoneSheet['K38'].value #Cell position for D Grade Low of an iPhone 8 Unlocked 256Gb
   _iPhone8L64GbAHigh = usedIphoneSheet['D39'].value #Cell position for A Grade High of a iPhone 8 locked 64Gb
   _iPhone8L64GbALow = usedIphoneSheet['E39'].value #Cell position for A Grade Low of a iPhone 8 locked 64Gb
   _iPhone8L64GbBHigh = usedIphoneSheet['F39'].value #Cell position for B Grade High of a iPhone 8 locked 64Gb
   _iPhone8L64GbBLow= usedIphoneSheet['G39'].value #Cell position for B Grade Low of a iPhone 8 locked 64Gb
   _iPhone8L64GbCHigh = usedIphoneSheet['H39'].value #Cell position for C Grade High of an iPhone 8 locked 64Gb
   _iPhone8L64GbCLow= usedIphoneSheet['I39'].value #Cell position for C Grade Low of an iPhone 8 locked 64Gb
   _iPhone8L64GbDHigh = usedIphoneSheet['J39'].value #Cell position for D Grade High of an iPhone 8 locked 64Gb
   _iPhone8L64GbDLow = usedIphoneSheet['K39'].value #Cell position for D Grade Low of an iPhone 8 locked 64Gb
   _iPhone8L256GbAHigh = usedIphoneSheet['D40'].value #Cell position for A Grade High of a iPhone 8 locked 256Gb
   _iPhone8L256GbALow = usedIphoneSheet['E40'].value #Cell position for A Grade Low of a iPhone 8 locked 256Gb
   _iPhone8L256GbBHigh = usedIphoneSheet['F40'].value #Cell position for B Grade High of a iPhone 8 locked 256Gb
   _iPhone8L256GbBLow= usedIphoneSheet['G40'].value #Cell position for B Grade Low of a iPhone 8 locked 256Gb
   _iPhone8L256GbCHigh = usedIphoneSheet['H40'].value #Cell position for C Grade High of an iPhone 8 locked 256Gb
   _iPhone8L256GbCLow= usedIphoneSheet['I40'].value #Cell position for C Grade Low of an iPhone 8 locked 256Gb
   _iPhone8L256GbDHigh = usedIphoneSheet['J40'].value #Cell position for D Grade High of an iPhone 8 locked 256Gb
   _iPhone8L256GbDLow = usedIphoneSheet['K40'].value #Cell position for D Grade Low of an iPhone 8 locked 256Gb
    #unlocked & locked iPhone 8 Plus Prices
    #
   _iPhone8PlusUL64GbAHigh = usedIphoneSheet['D44'].value #Cell position for A Grade High of a iPhone 8 Plus Unlocked 64Gb
   _iPhone8PlusUL64GbALow = usedIphoneSheet['E44'].value #Cell position for A Grade Low of a iPhone 8 Plus Unlocked 64Gb
   _iPhone8PlusUL64GbBHigh = usedIphoneSheet['F44'].value #Cell position for B Grade High of a iPhone 8 Plus Unlocked 64Gb
   _iPhone8PlusUL64GbBLow= usedIphoneSheet['G44'].value #Cell position for B Grade Low of a iPhone 8 Plus Unlocked 64Gb
   _iPhone8PlusUL64GbCHigh = usedIphoneSheet['H44'].value #Cell position for C Grade High of an iPhone 8 Plus Unlocked 64Gb
   _iPhone8PlusUL64GbCLow= usedIphoneSheet['I44'].value #Cell position for C Grade Low of an iPhone 8 Plus Unlocked 64Gb
   _iPhone8PlusUL64GbDHigh = usedIphoneSheet['J44'].value #Cell position for D Grade High of an iPhone 8 Plus Unlocked 64Gb
   _iPhone8PlusUL64GbDLow = usedIphoneSheet['K44'].value #Cell position for D Grade Low of an iPhone 8 Plus Unlocked 64Gb
   _iPhone8PlusUL256GbAHigh = usedIphoneSheet['D45'].value #Cell position for A Grade High of a iPhone 8 Plus Unlocked 256Gb
   _iPhone8PlusUL256GbALow = usedIphoneSheet['E45'].value #Cell position for A Grade Low of a iPhone 8 Plus Unlocked 256Gb
   _iPhone8PlusUL256GbBHigh = usedIphoneSheet['F45'].value #Cell position for B Grade High of a iPhone 8 Plus Unlocked 256Gb
   _iPhone8PlusUL256GbBLow= usedIphoneSheet['G45'].value #Cell position for B Grade Low of a iPhone 8 Plus Unlocked 256Gb
   _iPhone8PlusUL256GbCHigh = usedIphoneSheet['H45'].value #Cell position for C Grade High of an iPhone 8 Plus Unlocked 256Gb
   _iPhone8PlusUL256GbCLow= usedIphoneSheet['I45'].value #Cell position for C Grade Low of an iPhone 8 Plus Unlocked 256Gb
   _iPhone8PlusUL256GbDHigh = usedIphoneSheet['J45'].value #Cell position for D Grade High of an iPhone 8 Plus Unlocked 256Gb
   _iPhone8PlusUL256GbDLow = usedIphoneSheet['K45'].value #Cell position for D Grade Low of an iPhone 8 Plus Unlocked 256Gb
   _iPhone8PlusL64GbAHigh = usedIphoneSheet['D46'].value #Cell position for A Grade High of a iPhone 8 Plus locked 64Gb
   _iPhone8PlusL64GbALow = usedIphoneSheet['E46'].value #Cell position for A Grade Low of a iPhone 8 Plus locked 64Gb
   _iPhone8PlusL64GbBHigh = usedIphoneSheet['F46'].value #Cell position for B Grade High of a iPhone 8 Plus locked 64Gb
   _iPhone8PlusL64GbBLow= usedIphoneSheet['G46'].value #Cell position for B Grade Low of a iPhone 8 Plus locked 64Gb
   _iPhone8PlusL64GbCHigh = usedIphoneSheet['H46'].value #Cell position for C Grade High of an iPhone 8 Plus locked 64Gb
   _iPhone8PlusL64GbCLow= usedIphoneSheet['I46'].value #Cell position for C Grade Low of an iPhone 8 Plus locked 64Gb
   _iPhone8PlusL64GbDHigh = usedIphoneSheet['J46'].value #Cell position for D Grade High of an iPhone 8 Plus locked 64Gb
   _iPhone8PlusL64GbDLow = usedIphoneSheet['K46'].value #Cell position for D Grade Low of an iPhone 8 Plus locked 64Gb
   _iPhone8PlusL256GbAHigh = usedIphoneSheet['D47'].value #Cell position for A Grade High of a iPhone 8 Plus locked 256Gb
   _iPhone8PlusL256GbALow = usedIphoneSheet['E47'].value #Cell position for A Grade Low of a iPhone 8 Plus locked 256Gb
   _iPhone8L256GbBHigh = usedIphoneSheet['F47'].value #Cell position for B Grade High of a iPhone 8 Plus locked 256Gb
   _iPhone8PlusL256GbBLow= usedIphoneSheet['G47'].value #Cell position for B Grade Low of a iPhone 8 Plus locked 256Gb
   _iPhone8PlusL256GbCHigh = usedIphoneSheet['H47'].value #Cell position for C Grade High of an iPhone 8 Plus locked 256Gb
   _iPhone8PlusL256GbCLow= usedIphoneSheet['I47'].value #Cell position for C Grade Low of an iPhone 8 Plus locked 256Gb
   _iPhone8PlusL256GbDHigh = usedIphoneSheet['J47'].value #Cell position for D Grade High of an iPhone 8 Plus locked 256Gb
   _iPhone8PlusL256GbDLow = usedIphoneSheet['K47'].value #Cell position for D Grade Low of an iPhone 8 Plus locked 256Gb
   #Unlocked & Locked iPhone X Prices
   #
   _iPhoneXUL64GbAHigh = usedIphoneSheet['D51'].value #Cell position for A Grade High of a iPhone X Unlocked 64Gb
   _iPhoneXUL64GbALow = usedIphoneSheet['E51'].value #Cell position for A Grade Low of a iPhone X Unlocked 64Gb
   _iPhoneXUL64GbBHigh = usedIphoneSheet['F51'].value #Cell position for B Grade High of a iPhone X Unlocked 64Gb
   _iPhoneXUL64GbBLow= usedIphoneSheet['G51'].value #Cell position for B Grade Low of a iPhone X Unlocked 64Gb
   _iPhoneXUL64GbCHigh = usedIphoneSheet['H51'].value #Cell position for C Grade High of an iPhone X Unlocked 64Gb
   _iPhoneXUL64GbCLow = usedIphoneSheet['I51'].value #Cell position for C Grade Low of an iPhone X Unlocked 64Gb
   _iPhoneXUL64GbDHigh = usedIphoneSheet['J51'].value #Cell position for D Grade High of an iPhone X Unlocked 64Gb
   _iPhoneXUL64GbDLow = usedIphoneSheet['K51'].value #Cell position for D Grade Low of an iPhone X Unlocked 64Gb
   _iPhoneXUL256GbAHigh = usedIphoneSheet['D52'].value #Cell position for A Grade High of a iPhone X Unlocked 256Gb
   _iPhoneXUL256GbALow = usedIphoneSheet['E52'].value #Cell position for A Grade Low of a iPhone X Unlocked 256Gb
   _iPhoneXUL256GbBHigh = usedIphoneSheet['F52'].value #Cell position for B Grade High of a iPhone X Unlocked 256Gb
   _iPhoneXUL256GbBLow= usedIphoneSheet['G52'].value #Cell position for B Grade Low of a iPhone X Unlocked 256Gb
   _iPhoneXUL256GbCHigh = usedIphoneSheet['H52'].value #Cell position for C Grade High of an iPhone X Unlocked 256Gb
   _iPhoneXUL256GbCLow= usedIphoneSheet['I52'].value #Cell position for C Grade Low of an iPhone X Unlocked 256Gb
   _iPhoneXUL256GbDHigh = usedIphoneSheet['J52'].value #Cell position for D Grade High of an iPhone X Unlocked 256Gb
   _iPhoneXUL256GbDLow = usedIphoneSheet['K52'].value #Cell position for D Grade Low of an iPhone X Unlocked 256Gb
   _iPhoneXL64GbAHigh = usedIphoneSheet['D53'].value #Cell position for A Grade High of a iPhone X locked 64Gb
   _iPhoneXL64GbALow = usedIphoneSheet['E53'].value #Cell position for A Grade Low of a iPhone X locked 64Gb
   _iPhoneXL64GbBHigh = usedIphoneSheet['F53'].value #Cell position for B Grade High of a iPhone X locked 64Gb
   _iPhoneXL64GbBLow= usedIphoneSheet['G53'].value #Cell position for B Grade Low of a iPhone X locked 64Gb
   _iPhoneXL64GbCHigh = usedIphoneSheet['H53'].value #Cell position for C Grade High of an iPhone X locked 64Gb
   _iPhoneXL64GbCLow= usedIphoneSheet['I53'].value #Cell position for C Grade Low of an iPhone X locked 64Gb
   _iPhoneXL64GbDHigh = usedIphoneSheet['J53'].value #Cell position for D Grade High of an iPhone X locked 64Gb
   _iPhoneXL64GbDLow = usedIphoneSheet['K53'].value #Cell position for D Grade Low of an iPhone X locked 64Gb
   _iPhoneXL256GbAHigh = usedIphoneSheet['D54'].value #Cell position for A Grade High of a iPhone X locked 256Gb
   _iPhoneXL256GbALow = usedIphoneSheet['E54'].value #Cell position for A Grade Low of a iPhone X locked 256Gb
   _iPhoneXL256GbBHigh = usedIphoneSheet['F54'].value #Cell position for B Grade High of a iPhone X locked 256Gb
   _iPhoneXL256GbBLow= usedIphoneSheet['G54'].value #Cell position for B Grade Low of a iPhone X locked 256Gb
   _iPhoneXL256GbCHigh = usedIphoneSheet['H54'].value #Cell position for C Grade High of an iPhone X locked 256Gb
   _iPhoneXL256GbCLow= usedIphoneSheet['I54'].value #Cell position for C Grade Low of an iPhone X locked 256Gb
   _iPhoneXL256GbDHigh = usedIphoneSheet['J54'].value #Cell position for D Grade High of an iPhone X locked 256Gb
   _iPhoneXL256GbDLow = usedIphoneSheet['K54'].value #Cell position for D Grade Low of an iPhone X locked 256Gb
   #Unlocked and Locked iPhone XR Prices
   #
   _iPhoneXRUL64GbAHigh = usedIphoneSheet['D58'].value #Cell position for A Grade High of a unlocked iPhone XR 64Gb
   _iPhoneXRUL64GbALow = usedIphoneSheet['E58'].value #Cell position for A Grade Low of a unlocked iPhone XR 64Gb
   _iPhoneXRUL64GbBHigh = usedIphoneSheet['F58'].value #Cell position for B Grade High of a unlocked iPhone XR 64Gb
   _iPhoneXRUL64GbBLow = usedIphoneSheet['G58'].value #Cell position for B Grade Low of a unlocked iPhone XR 64Gb
   _iPhoneXRUL64GbCHigh = usedIphoneSheet['H58'].value #Cell position for C Grade High of a unlocked iPhone XR 64Gb
   _iPhoneXRUL64GbCLow = usedIphoneSheet['I58'].value #Cell position for C Grade Low of a unlocked iPhone XR 64Gb
   _iPhoneXRUL64GbDHigh = usedIphoneSheet['J58'].value #Cell position for D Grade High of a unlocked iPhone XR 64Gb
   _iPhoneXRUL64GbDLow = usedIphoneSheet['K58'].value #Cell position for D Grade Low of a unlocked iPhone XR 64Gb
   _iPhoneXRUL128GbAHigh = usedIphoneSheet['D59'].value #Cell position for A Grade High of a unlocked iPhone XR 128Gb
   _iPhoneXRUL128GbALow = usedIphoneSheet['E59'].value #Cell position for A Grade Low of a unlocked iPhone XR 128Gb
   _iPhoneXRUL128GbBHigh = usedIphoneSheet['F59'].value #Cell position for B Grade High of a unlocked iPhone XR 128Gb
   _iPhoneXRUL128GbBLow = usedIphoneSheet['G59'].value #Cell position for B Grade Low of a unlocked iPhone XR 128Gb
   _iPhoneXRUL128GbCHigh = usedIphoneSheet['H59'].value #Cell position for C Grade High of a unlocked iPhone XR 128Gb
   _iPhoneXRUL128GbCLow = usedIphoneSheet['I59'].value #Cell position for C Grade Low of a unlocked iPhone XR 128Gb
   _iPhoneXRUL128GbDHigh = usedIphoneSheet['J59'].value #Cell position for D Grade High of a unlocked iPhone XR 128Gb
   _iPhoneXRUL128GbDLow = usedIphoneSheet['K59'].value #Cell position for D Grade Low of a unlocked iPhone XR 128Gb
   _iPhoneXRUL256GbAHigh = usedIphoneSheet['D60'].value #Cell position for A Grade High of a unlocked iPhone XR 256Gb
   _iPhoneXRUL256GbALow = usedIphoneSheet['E60'].value #Cell position for A Grade Low of a unlocked iPhone XR 256Gb
   _iPhoneXRUL256GbBHigh = usedIphoneSheet['F60'].value #Cell position for B Grade High of a unlocked iPhone XR 256Gb
   _iPhoneXRUL256GbBLow = usedIphoneSheet['G60'].value #Cell position for B Grade Low of a unlocked iPhone XR 256Gb
   _iPhoneXRUL256GbCHigh = usedIphoneSheet['H60'].value #Cell position for C Grade High of a unlocked iPhone XR 256Gb
   _iPhoneXRUL256GbCLow = usedIphoneSheet['I60'].value #Cell position for C Grade Low of a unlocked iPhone XR 256Gb
   _iPhoneXRUL256GbDHigh = usedIphoneSheet['J60'].value #Cell position for D Grade High of a unlocked iPhone XR 256Gb
   _iPhoneXRUL256GbDLow = usedIphoneSheet['K60'].value #Cell position for D Grade Low of a unlocked iPhone XR 256Gb
   _iPhoneXRL64GbAHigh = usedIphoneSheet['D61'].value #Cell position for A Grade High of a unlocked iPhone XR 64Gb
   _iPhoneXRL64GbALow = usedIphoneSheet['E61'].value #Cell position for A Grade Low of a unlocked iPhone XR 64Gb
   _iPhoneXRL64GbBHigh = usedIphoneSheet['F61'].value #Cell position for B Grade High of a unlocked iPhone XR 64Gb
   _iPhoneXRL64GbBLow = usedIphoneSheet['G61'].value #Cell position for B Grade Low of a unlocked iPhone XR 64Gb
   _iPhoneXRL64GbCHigh = usedIphoneSheet['H61'].value #Cell position for C Grade High of a unlocked iPhone XR 64Gb
   _iPhoneXRL64GbCLow = usedIphoneSheet['I61'].value #Cell position for C Grade Low of a unlocked iPhone XR 64Gb
   _iPhoneXRL64GbDHigh = usedIphoneSheet['J61'].value #Cell position for D Grade High of a unlocked iPhone XR 64Gb
   _iPhoneXRL64GbDLow = usedIphoneSheet['K61'].value #Cell position for D Grade Low of a unlocked iPhone XR 64Gb
   _iPhoneXRL128GbAHigh = usedIphoneSheet['D62'].value #Cell position for A Grade High of a unlocked iPhone XR 128Gb
   _iPhoneXRL128GbALow = usedIphoneSheet['E62'].value #Cell position for A Grade Low of a unlocked iPhone XR 128Gb
   _iPhoneXRL128GbBHigh = usedIphoneSheet['F62'].value #Cell position for B Grade High of a unlocked iPhone XR 128Gb
   _iPhoneXRL128GbBLow = usedIphoneSheet['G62'].value #Cell position for B Grade Low of a unlocked iPhone XR 128Gb
   _iPhoneXRL128GbCHigh = usedIphoneSheet['H62'].value #Cell position for C Grade High of a unlocked iPhone XR 128Gb
   _iPhoneXRL128GbCLow = usedIphoneSheet['I62'].value #Cell position for C Grade Low of a unlocked iPhone XR 128Gb
   _iPhoneXRL128GbDHigh = usedIphoneSheet['J62'].value #Cell position for D Grade High of a unlocked iPhone XR 128Gb
   _iPhoneXRL128GbDLow = usedIphoneSheet['K62'].value #Cell position for D Grade Low of a unlocked iPhone XR 128Gb
   _iPhoneXRL256GbAHigh = usedIphoneSheet['D63'].value #Cell position for A Grade High of a unlocked iPhone XR 256Gb
   _iPhoneXRL256GbALow = usedIphoneSheet['E63'].value #Cell position for A Grade Low of a unlocked iPhone XR 256Gb
   _iPhoneXRL256GbBHigh = usedIphoneSheet['F63'].value #Cell position for B Grade High of a unlocked iPhone XR 256Gb
   _iPhoneXRL256GbBLow = usedIphoneSheet['G63'].value #Cell position for B Grade Low of a unlocked iPhone XR 256Gb
   _iPhoneXRL256GbCHigh = usedIphoneSheet['H63'].value #Cell position for C Grade High of a unlocked iPhone XR 256Gb
   _iPhoneXRL256GbCLow = usedIphoneSheet['I63'].value #Cell position for C Grade Low of a unlocked iPhone XR 256Gb
   _iPhoneXRL256GbDHigh = usedIphoneSheet['J63'].value #Cell position for D Grade High of a unlocked iPhone XR 256Gb
   _iPhoneXRL256GbDLow = usedIphoneSheet['K63'].value #Cell position for D Grade Low of a unlocked iPhone XR 256Gb
   #Unlocked and Locked iPhone XS Prices
   #
   _iPhoneXSUL64GbAHigh = usedIphoneSheet['D67'].value #Cell position for A Grade High of a unlocked iPhone XS 64Gb
   _iPhoneXSUL64GbALow= usedIphoneSheet['E67'].value #Cell position for A Grade Low of a unlocked iPhone XS 64Gb
   _iPhoneXSUL64GbBHigh = usedIphoneSheet['F67'].value #Cell position for B Grade High of a unlocked iPhone XS 64Gb
   _iPhoneXSUL64GbBLow = usedIphoneSheet['G67'].value #Cell position for B Grade Low of a unlocked iPhone XS 64Gb
   _iPhoneXSUL64GbCHigh = usedIphoneSheet['H67'].value #Cell position for C Grade High of a unlocked iPhone XS 64Gb
   _iPhoneXSUL64GbCLow = usedIphoneSheet['I67'].value #Cell position for C Grade Low of a unlocked iPhone XS 64Gb
   _iPhoneXSUL64GbDHigh = usedIphoneSheet['J67'].value #Cell position for D Grade High of a unlocked iPhone XS 64Gb
   _iPhoneXSUL64GbDLow = usedIphoneSheet['K67'].value #Cell position for D Grade Low of a unlocked iPhone XS 64Gb
   _iPhoneXSUL256GbAHigh = usedIphoneSheet['D68'].value #Cell position for A Grade High of a unlocked iPhone XS 256Gb
   _iPhoneXSUL256GbALow = usedIphoneSheet['E68'].value #Cell position for A Grade Low of a unlocked iPhone XS 256Gb
   _iPhoneXSUL256GbBHigh = usedIphoneSheet['F68'].value #Cell position for B Grade High of a unlocked iPhone XS 256Gb
   _iPhoneXSUL256GbBLow = usedIphoneSheet['G68'].value #Cell position for B Grade Low of a unlocked iPhone XS 256Gb
   _iPhoneXSUL256GbCHigh = usedIphoneSheet['H68'].value #Cell position for C Grade High of a unlocked iPhone XS 256Gb
   _iPhoneXSUL256GbCLow = usedIphoneSheet['I68'].value #Cell position for C Grade Low of a unlocked iPhone XS 256Gb
   _iPhoneXSUL256GbDHigh = usedIphoneSheet['J68'].value #Cell position for D Grade High of a unlocked iPhone XS 256Gb
   _iPhoneXSUL256GbDLow = usedIphoneSheet['K68'].value #Cell position for D Grade Low of a unlocked iPhone XS 256Gb
   _iPhoneXSUL512GbAHigh = usedIphoneSheet['D69'].value #Cell position for A Grade High of a unlocked iPhone XS 512Gb
   _iPhoneXSUL512GbALow = usedIphoneSheet['E69'].value #Cell position for A Grade Low of a unlocked iPhone XS 512Gb
   _iPhoneXSUL512GbBHigh = usedIphoneSheet['F69'].value #Cell position for B Grade High of a unlocked iPhone XS 512Gb
   _iPhoneXSUL512GbBLow = usedIphoneSheet['G69'].value #Cell position for B Grade Low of a unlocked iPhone XS 512Gb
   _iPhoneXSUL512GbCHigh = usedIphoneSheet['H69'].value #Cell position for C Grade High of a unlocked iPhone XS 512Gb
   _iPhoneXSUL512GbCLow = usedIphoneSheet['I69'].value #Cell position for C Grade Low of a unlocked iPhone XS 512Gb
   _iPhoneXSUL512GbDHigh = usedIphoneSheet['J69'].value #Cell position for D Grade High of a unlocked iPhone XS 512Gb
   _iPhoneXSUL512GbDLow = usedIphoneSheet['K69'].value #Cell position for D Grade Low of a unlocked iPhone XS 512Gb
   _iPhoneXSL64GbAHigh = usedIphoneSheet['D70'].value #Cell position for A Grade High of a locked iPhone XS 64Gb
   _iPhoneXSL64GbALow = usedIphoneSheet['E70'].value #Cell position for A Grade Low of a locked iPhone XS 64Gb
   _iPhoneXSL64GbBHigh = usedIphoneSheet['F70'].value #Cell position for B Grade High of a locked iPhone XS 64Gb
   _iPhoneXSL64GbBLow = usedIphoneSheet['G70'].value #Cell position for B Grade Low of a locked iPhone XS 64Gb
   _iPhoneXSL64GbCHigh = usedIphoneSheet['H70'].value #Cell position for C Grade High of a locked iPhone XS 64Gb
   _iPhoneXSL64GbCLow = usedIphoneSheet['I70'].value #Cell position for C Grade Low of a locked iPhone XS 64Gb
   _iPhoneXSL64GbDHigh = usedIphoneSheet['J70'].value #Cell position for D Grade High of a locked iPhone XS 64Gb
   _iPhoneXSL64GbDLow = usedIphoneSheet['K70'].value #Cell position for D Grade Low of a locked iPhone XS 64Gb
   _iPhoneXSL256GbAHigh = usedIphoneSheet['D71'].value #Cell position for A Grade High of a locked iPhone XS 256Gb
   _iPhoneXSL256GbALow = usedIphoneSheet['E71'].value #Cell position for A Grade Low of a locked iPhone XS 256Gb
   _iPhoneXSL256GbBHigh = usedIphoneSheet['F71'].value #Cell position for B Grade High of a locked iPhone XS 256Gb
   _iPhoneXSL256GbBLow = usedIphoneSheet['G71'].value #Cell position for B Grade Low of a locked iPhone XS 256Gb
   _iPhoneXSL256GbCHigh = usedIphoneSheet['H71'].value #Cell position for C Grade High of a locked iPhone XS 256Gb
   _iPhoneXSL256GbCLow = usedIphoneSheet['I71'].value #Cell position for C Grade Low of a locked iPhone XS 256Gb
   _iPhoneXSL256GbDHigh = usedIphoneSheet['J71'].value #Cell position for D Grade High of a locked iPhone XS 256Gb
   _iPhoneXSL256GbDLow = usedIphoneSheet['K71'].value #Cell position for D Grade Low of a locked iPhone XS 256Gb
   _iPhoneXSL512GbAHigh = usedIphoneSheet['D72'].value #Cell position for A Grade High of a locked iPhone XS 512Gb
   _iPhoneXSL512GbALow = usedIphoneSheet['E72'].value #Cell position for A Grade Low of a locked iPhone XS 512Gb
   _iPhoneXSL512GbBHigh = usedIphoneSheet['F72'].value #Cell position for B Grade High of a locked iPhone XS 512Gb
   _iPhoneXSL512GbBLow = usedIphoneSheet['G72'].value #Cell position for B Grade Low of a ocked iPhone XS 512Gb
   _iPhoneXSL512GbCHigh = usedIphoneSheet['H72'].value #Cell position for C Grade High of a locked iPhone XS 512Gb
   _iPhoneXSL512GbCLow = usedIphoneSheet['I72'].value #Cell position for C Grade Low of a locked iPhone XS 512Gb
   _iPhoneXSL512GbDHigh = usedIphoneSheet['J72'].value #Cell position for D Grade High of a locked iPhone XS 512Gb
   _iPhoneXSL512GbDLow = usedIphoneSheet['K72'].value #Cell position for D Grade Low of a locked iPhone XS 512Gb
   #unlocked & Locked iPhone XS Max Prices
   #
   _iPhoneXSMaxUL64GbAHigh = usedIphoneSheet['D76'].value #Cell position for A Grade High of a unlocked iPhone XS Max 64Gb
   _iPhoneXSMaxUL64GbALow = usedIphoneSheet['E76'].value #Cell position for A Grade Low of a unlocked iPhone XS Max 64Gb
   _iPhoneXSMaxUL64GbBHigh = usedIphoneSheet['F76'].value #Cell position for B Grade High of a unlocked iPhone XS Max 64Gb
   _iPhoneXSMaxUL64GbBLow = usedIphoneSheet['G76'].value #Cell position for B Grade Low of a unlocked iPhone XS Max 64Gb
   _iPhoneXSMaxUL64GbCHigh = usedIphoneSheet['H76'].value #Cell position for C Grade High of a unlocked iPhone XS Max 64Gb
   _iPhoneXSMaxUL64GbCLow = usedIphoneSheet['I76'].value #Cell position for C Grade Low of a unlocked iPhone XS Max 64Gb
   _iPhoneXSMaxUL64GbDHigh = usedIphoneSheet['J76'].value #Cell position for D Grade High of a unlocked iPhone XS Max 64Gb
   _iPhoneXSMaxUL64GbDLow = usedIphoneSheet['K76'].value #Cell position for D Grade Low of a unlocked iPhone XS Max 64Gb
   _iPhoneXSMaxUL256GbAHigh = usedIphoneSheet['D77'].value #Cell position for A Grade High of a unlocked iPhone XS Max  256Gb
   _iPhoneXSMaxUL256GbALow = usedIphoneSheet['E77'].value #Cell position for A Grade Low of a unlocked iPhone XS Max 256Gb
   _iPhoneXSMaxUL256GbBHigh = usedIphoneSheet['F77'].value #Cell position for B Grade High of a unlocked iPhone XS Max 256Gb
   _iPhoneXSMaxUL256GbBLow = usedIphoneSheet['G77'].value #Cell position for B Grade Low of a unlocked iPhone XS Max 256Gb
   _iPhoneXSMaxUL256GbCHigh = usedIphoneSheet['H77'].value #Cell position for C Grade High of a unlocked iPhone XS Max 256Gb
   _iPhoneXSMaxUL256GbCLow = usedIphoneSheet['I77'].value #Cell position for C Grade Low of a unlocked iPhone XS Max 256Gb
   _iPhoneXSMaxUL256GbDHigh = usedIphoneSheet['J77'].value #Cell position for D Grade High of a unlocked iPhone XS Max 256Gb
   _iPhoneXSMaxUL256GbDLow = usedIphoneSheet['K77'].value #Cell position for D Grade Low of a unlocked iPhone XS Max 256Gb
   _iPhoneXSMaxUL512GbAHigh = usedIphoneSheet['D78'].value #Cell position for A Grade High of a unlocked iPhone XS Max 512Gb
   _iPhoneXSMaxUL512GbALow = usedIphoneSheet['E78'].value #Cell position for A Grade Low of a unlocked iPhone XS Max 512Gb
   _iPhoneXSMaxUL512GbBHigh = usedIphoneSheet['F78'].value #Cell position for B Grade High of a unlocked iPhone XS Max 512Gb
   _iPhoneXSMaxUL512GbBLow = usedIphoneSheet['G78'].value #Cell position for B Grade Low of a unlocked iPhone XS Max 512Gb
   _iPhoneXSMaxUL512GbCHigh = usedIphoneSheet['H78'].value #Cell position for C Grade High of a unlocked iPhone XS Max 512Gb
   _iPhoneXSMaxUL512GbCLow = usedIphoneSheet['I78'].value #Cell position for C Grade Low of a unlocked iPhone XS Max 512Gb
   _iPhoneXSMaxUL512GbDHigh = usedIphoneSheet['J78'].value #Cell position for D Grade High of a unlocked iPhone XS Max 512Gb
   _iPhoneXSMaxL64GbAHigh = usedIphoneSheet['D79'].value #Cell position for A Grade High of a locked iPhone XS Max 64Gb
   _iPhoneXSMaxL64GbAHigh = usedIphoneSheet['E79'].value #Cell position for A Grade Low of a locked iPhone XS Max 64Gb
   _iPhoneXSMaxL64GbBHigh = usedIphoneSheet['F79'].value #Cell position for B Grade High of a locked iPhone XS Max 64Gb
   _iPhoneXSMaxL64GbBLow = usedIphoneSheet['G79'].value #Cell position for B Grade Low of a locked iPhone XS Max 64Gb
   _iPhoneXSMaxL64GbCHigh = usedIphoneSheet['H79'].value #Cell position for C Grade High of a locked iPhone XS Max 64Gb
   _iPhoneXSMaxL64GbCLow = usedIphoneSheet['I79'].value #Cell position for C Grade Low of a locked iPhone XS Max 64Gb
   _iPhoneXSMaxL64GbDHigh = usedIphoneSheet['J79'].value #Cell position for D Grade High of a locked iPhone XS Max 64Gb
   _iPhoneXSMaxL64GbDLow = usedIphoneSheet['K79'].value #Cell position for D Grade Low of a locked iPhone XS Max 64Gb
   _iPhoneXSMaxL256GbAHigh = usedIphoneSheet['D80'].value #Cell position for A Grade High of a locked iPhone XS Max  256Gb
   _iPhoneXSMaxL256GbALow = usedIphoneSheet['E80'].value #Cell position for A Grade Low of a locked iPhone XS Max 256Gb
   _iPhoneXSMaxL256GbBHigh = usedIphoneSheet['F80'].value #Cell position for B Grade High of a locked iPhone XS Max 256Gb
   _iPhoneXSMaxL256GbBLow = usedIphoneSheet['G80'].value #Cell position for B Grade Low of a locked iPhone XS Max 256Gb
   _iPhoneXSMaxL256GbCHigh = usedIphoneSheet['H80'].value #Cell position for C Grade High of a locked iPhone XS Max 256Gb
   _iPhoneXSMaxL256GbCLow = usedIphoneSheet['I80'].value #Cell position for C Grade Low of a locked iPhone XS Max 256Gb
   _iPhoneXSMaxL256GbDHigh = usedIphoneSheet['J80'].value #Cell position for D Grade High of a locked iPhone XS Max 256Gb
   _iPhoneXSMaxL256GbDLow = usedIphoneSheet['K80'].value #Cell position for D Grade Low of a locked iPhone XS Max 256Gb
   _iPhoneXSMaxL512GbAHigh = usedIphoneSheet['D81'].value #Cell position for A Grade High of a locked iPhone XS Max 512Gb
   _iPhoneXSMaxL512GbALow = usedIphoneSheet['E81'].value #Cell position for A Grade Low of a locked iPhone XS Max 512Gb
   _iPhoneXSMaxL512GbBHigh = usedIphoneSheet['F81'].value #Cell position for B Grade High of a locked iPhone XS Max 512Gb
   _iPhoneXSMaxL512GbBLow = usedIphoneSheet['G81'].value #Cell position for B Grade Low of a locked iPhone XS Max 512Gb
   _iPhoneXSMaxL512GbCHigh = usedIphoneSheet['H81'].value #Cell position for C Grade High of a locked iPhone XS Max 512Gb
   _iPhoneXSMaxL512GbCLow = usedIphoneSheet['I81'].value #Cell position for C Grade Low of a locked iPhone XS Max 512Gb
   _iPhoneXSMaxL512GbDHigh = usedIphoneSheet['J81'].value #Cell position for D Grade High of a locked iPhone XS Max 512Gb
   #Unlocked and Locked iPhone 11 Prices
   #
   _iPhone11UL64GbAHigh = usedIphoneSheet['D86'].value #Cell position for A Grade High of a unlocked iPhone 11 64Gb
   _iPhone11UL64GbALow = usedIphoneSheet['E86'].value #Cell position for A Grade Low of a unlocked iPhone 11 64Gb
   _iPhone11UL64GbBHigh = usedIphoneSheet['F86'].value #Cell position for B Grade High of a unlocked iPhone 11 64Gb
   _iPhone11UL64GbBLow = usedIphoneSheet['G86'].value #Cell position for B Grade Low of a unlocked iPhone 11 64Gb
   _iPhone11UL64GbCHigh = usedIphoneSheet['H86'].value #Cell position for C Grade High of a unlocked iPhone 11 64Gb
   _iPhone11UL64GbCLow = usedIphoneSheet['I86'].value #Cell position for C Grade Low of a unlocked iPhone 11 64Gb
   _iPhone11UL64GbDHigh = usedIphoneSheet['J86'].value #Cell position for D Grade High of a unlocked iPhone 11 64Gb
   _iPhone11UL64GbDLow = usedIphoneSheet['K86'].value #Cell position for D Grade Low of a unlocked iPhone 11 64Gb
   _iPhone11UL128GbAHigh = usedIphoneSheet['D87'].value #Cell position for A Grade High of a unlocked iPhone 11 128Gb
   _iPhone11UL128GbALow = usedIphoneSheet['E87'].value #Cell position for A Grade Low of a unlocked iPhone 11 128Gb
   _iPhone11UL128GbBHigh = usedIphoneSheet['F87'].value #Cell position for B Grade High of a unlocked iPhone 11 128Gb
   _iPhone11UL128GbBLow = usedIphoneSheet['G87'].value #Cell position for B Grade Low of a unlocked iPhone 11 128Gb
   _iPhone11UL128GbCHigh = usedIphoneSheet['H87'].value #Cell position for C Grade High of a unlocked iPhone 11 128Gb
   _iPhone11UL128GbCLow = usedIphoneSheet['I87'].value #Cell position for C Grade Low of a unlocked iPhone 11 128Gb
   _iPhone11UL128GbDHigh = usedIphoneSheet['J87'].value #Cell position for D Grade High of a unlocked iPhone 11 128Gb
   _iPhone11UL128GbDLow = usedIphoneSheet['K87'].value #Cell position for D Grade Low of a unlocked iPhone 11 128Gb
   _iPhone11UL256GbAHigh = usedIphoneSheet['D88'].value #Cell position for A Grade High of a unlocked iPhone 11 256Gb
   _iPhone11UL256GbALow = usedIphoneSheet['E88'].value #Cell position for A Grade Low of a unlocked iPhone 11 256Gb
   _iPhone11UL256GbBHigh = usedIphoneSheet['F88'].value #Cell position for B Grade High of a unlocked iPhone 11 256Gb
   _iPhone11UL256GbBLow = usedIphoneSheet['G88'].value #Cell position for B Grade Low of a unlocked iPhone 11 256Gb
   _iPhone11UL256GbCHigh = usedIphoneSheet['H88'].value #Cell position for C Grade High of a unlocked iPhone 11 256Gb
   _iPhone11UL256GbCLow = usedIphoneSheet['I88'].value #Cell position for C Grade Low of a unlocked iPhone 11 256Gb
   _iPhone11UL256GbDHigh = usedIphoneSheet['J88'].value #Cell position for D Grade High of a unlocked iPhone 11 256Gb
   _iPhone11UL256GbDLow = usedIphoneSheet['K88'].value #Cell position for D Grade Low of a unlocked iPhone 11 256Gb
   _iPhone11L64GbAHigh = usedIphoneSheet['D89'].value #Cell position for A Grade High of a unlocked iPhone 11 64Gb
   _iPhone11L64GbALow = usedIphoneSheet['E89'].value #Cell position for A Grade Low of a unlocked iPhone 11 64Gb
   _iPhone11L64GbBHigh = usedIphoneSheet['F89'].value #Cell position for B Grade High of a unlocked iPhone 11 64Gb
   _iPhone11L64GbBLow = usedIphoneSheet['G89'].value #Cell position for B Grade Low of a unlocked iPhone 11 64Gb
   _iPhone11L64GbCHigh = usedIphoneSheet['H89'].value #Cell position for C Grade High of a unlocked iPhone 11 64Gb
   _iPhone11L64GbCLow = usedIphoneSheet['I89'].value #Cell position for C Grade Low of a unlocked iPhone 11 64Gb
   _iPhone11L64GbDHigh = usedIphoneSheet['J89'].value #Cell position for D Grade High of a unlocked iPhone 11 64Gb
   _iPhone11L64GbDLow = usedIphoneSheet['K89'].value #Cell position for D Grade Low of a unlocked iPhone 11 64Gb
   _iPhone11L128GbAHigh = usedIphoneSheet['D90'].value #Cell position for A Grade High of a unlocked iPhone 11 128Gb
   _iPhone11L128GbALow = usedIphoneSheet['E90'].value #Cell position for A Grade Low of a unlocked iPhone 11 128Gb
   _iPhone11L128GbBHigh = usedIphoneSheet['F90'].value #Cell position for B Grade High of a unlocked iPhone 11 128Gb
   _iPhone11L128GbBLow = usedIphoneSheet['G90'].value #Cell position for B Grade Low of a unlocked iPhone 11 128Gb
   _iPhone11L128GbCHigh = usedIphoneSheet['H90'].value #Cell position for C Grade High of a unlocked iPhone 11 128Gb
   _iPhone11L128GbCLow = usedIphoneSheet['I90'].value #Cell position for C Grade Low of a unlocked iPhone 11 128Gb
   _iPhone11L128GbDHigh = usedIphoneSheet['J90'].value #Cell position for D Grade High of a unlocked iPhone 11 128Gb
   _iPhone11L128GbDLow = usedIphoneSheet['K90'].value #Cell position for D Grade Low of a unlocked iPhone 11 128Gb
   _iPhone11L256GbAHigh = usedIphoneSheet['D91'].value #Cell position for A Grade High of a unlocked iPhone 11 256Gb
   _iPhone11L256GbALow = usedIphoneSheet['E91'].value #Cell position for A Grade Low of a unlocked iPhone 11 256Gb
   _iPhone11L256GbBHigh = usedIphoneSheet['F91'].value #Cell position for B Grade High of a unlocked iPhone 11 256Gb
   _iPhone11L256GbBLow = usedIphoneSheet['G91'].value #Cell position for B Grade Low of a unlocked iPhone 11 256Gb
   _iPhone11L256GbCHigh = usedIphoneSheet['H91'].value #Cell position for C Grade High of a unlocked iPhone 11 256Gb
   _iPhone11L256GbCLow = usedIphoneSheet['I91'].value #Cell position for C Grade Low of a unlocked iPhone 11 256Gb
   _iPhone11L256GbDHigh = usedIphoneSheet['J91'].value #Cell position for D Grade High of a unlocked iPhone 11 256Gb
   _iPhone11L256GbDLow = usedIphoneSheet['K91'].value #Cell position for D Grade Low of a unlocked iPhone 11 256Gb
   #Unlocked and Locked iPhone 11 Pro Prices
   #
   _iPhone11Pro64GbAHigh = usedIphoneSheet['D95'].value #Cell position for A Grade High of a unlocked iPhone 11 Pro 64Gb
   _iPhone11Pro64GbALow = usedIphoneSheet['E95'].value #Cell position for A Grade Low of a unlocked iPhone 11 Pro 64Gb
   _iPhone11ProUL64GbBHigh = usedIphoneSheet['F95'].value #Cell position for B Grade High of a unlocked iPhone 11 Pro 64Gb
   _iPhone11ProUL64GbBLow = usedIphoneSheet['G95'].value #Cell position for B Grade Low of a unlocked iPhone 11 Pro 64Gb
   _iPhone11ProUL64GbCHigh = usedIphoneSheet['H95'].value #Cell position for C Grade High of a unlocked iPhone 11 Pro 64Gb
   _iPhone11ProUL64GbCLow = usedIphoneSheet['I95'].value #Cell position for C Grade Low of a unlocked iPhone 11 Pro 64Gb
   _iPhone11ProUL64GbDHigh = usedIphoneSheet['J95'].value #Cell position for D Grade High of a unlocked iPhone 11 Pro 64Gb
   _iPhone11ProUL64GbDLow = usedIphoneSheet['K95'].value #Cell position for D Grade Low of a unlocked iPhone 11 Pro 64Gb
   _iPhone11proUL256GbAHigh = usedIphoneSheet['D96'].value #Cell position for A Grade High of a unlocked iPhone 11 Pro 256Gb
   _iPhone11ProUL256GbALow = usedIphoneSheet['E96'].value #Cell position for A Grade Low of a unlocked iPhone 11 Pro 256Gb
   _iPhone11ProUL256GbBHigh = usedIphoneSheet['F96'].value #Cell position for B Grade High of a unlocked iPhone 11 Pro 256Gb
   _iPhone11ProUL256GbBLow = usedIphoneSheet['G96'].value #Cell position for B Grade Low of a unlocked iPhone1 1 Pro 256Gb
   _iPhone11ProUL256GbCHigh = usedIphoneSheet['H96'].value #Cell position for C Grade High of a unlocked iPhone 11 Pro 256Gb
   _iPhone11ProUL256GbCLow = usedIphoneSheet['I96'].value #Cell position for C Grade Low of a unlocked iPhone 11 Pro 256Gb
   _iPhone11ProUL256GbDHigh = usedIphoneSheet['J96'].value #Cell position for D Grade High of a unlocked iPhone 11 Pro 256Gb
   _iPhone11ProUL256GbDLow = usedIphoneSheet['K96'].value #Cell position for D Grade Low of a unlocked iPhone 11 Pro 256Gb
   _iPhone11ProUL512GbAHigh = usedIphoneSheet['D97'].value #Cell position for A Grade High of a unlocked iPhone 11 Pro 512Gb
   _iPhone11ProUL512GbALow = usedIphoneSheet['E97'].value #Cell position for A Grade Low of a unlocked iPhone 11 Pro512Gb
   _iPhone11ProUL512GbBHigh = usedIphoneSheet['F97'].value #Cell position for B Grade High of a unlocked iPhone 11 Pro 512Gb
   _iPhon11ProSUL512GbBLow = usedIphoneSheet['G97'].value #Cell position for B Grade Low of a unlocked iPhone 11 Pro 512Gb
   _iPhone11ProUL512GbCHigh = usedIphoneSheet['H97'].value #Cell position for C Grade High of a unlocked iPhone 11 Pro 512Gb
   _iPhone11ProUL512GbCLow = usedIphoneSheet['I97'].value #Cell position for C Grade Low of a unlocked iPhone 11 Pro 512Gb
   _iPhone11ProUL512GbDHigh = usedIphoneSheet['J97'].value #Cell position for D Grade High of a unlocked iPhone 11 Pro 512Gb
   _iPhone11ProUL512GbDLow = usedIphoneSheet['K97'].value #Cell position for D Grade Low of a unlocked iPhone 11 Pro 512Gb
   _iPhone11ProL64GbAHigh = usedIphoneSheet['D98'].value #Cell position for A Grade High of a locked iPhone 11 Pro 64Gb
   _iPhone11ProL64GbALow = usedIphoneSheet['E98'].value #Cell position for A Grade Low of a locked iPhone 11 Pro 64Gb
   _iPhone11ProL64GbBHigh = usedIphoneSheet['F98'].value #Cell position for B Grade High of a locked iPhone 11 Pro 64Gb
   _iPhone11ProL64GbBLow = usedIphoneSheet['G98'].value #Cell position for B Grade Low of a locked iPhone 11 Pro 64Gb
   _iPhone11ProL64GbCHigh = usedIphoneSheet['H98'].value #Cell position for C Grade High of a locked iPhone 11 Pro 64Gb
   _iPhone11ProL64GbCLow = usedIphoneSheet['I98'].value #Cell position for C Grade Low of a locked iPhone 11 Pro 64Gb
   _iPhone11ProL64GbDHigh = usedIphoneSheet['J98'].value #Cell position for D Grade High of a locked iPhone 11 Pro 64Gb
   _iPhone11ProL64GbDLow = usedIphoneSheet['K98'].value #Cell position for D Grade Low of a locked iPhone 11 Pro 64Gb
   _iPhone11ProL256GbAHigh = usedIphoneSheet['D99'].value #Cell position for A Grade High of a locked iPhone 11 Pro 256Gb
   _iPhone11ProL256GbALow = usedIphoneSheet['E99'].value #Cell position for A Grade Low of a locked iPhone 11 Pro 256Gb
   _iPhone11ProL256GbBHigh = usedIphoneSheet['F99'].value #Cell position for B Grade High of a locked iPhone 11 Pro 256Gb
   _iPhone11ProL256GbBLow = usedIphoneSheet['G99'].value #Cell position for B Grade Low of a locked iPhone 11 Pro 256Gb
   _iPhone11ProL256GbCHigh = usedIphoneSheet['H99'].value #Cell position for C Grade High of a locked iPhone 11 Pro 256Gb
   _iPhone11ProL256GbCLow = usedIphoneSheet['I99'].value #Cell position for C Grade Low of a locked iPhone 11 Pro 256Gb
   _iPhone11ProL256GbDHigh = usedIphoneSheet['J99'].value #Cell position for D Grade High of a locked iPhone 11 Pro 256Gb
   _iPhone11ProL256GbDLow = usedIphoneSheet['K99'].value #Cell position for D Grade Low of a locked iPhone 11 Pro 256Gb
   _iPhone11ProL512GbAHigh = usedIphoneSheet['D100'].value #Cell position for A Grade High of a locked iPhone 11 Pro 512Gb
   _iPhone11ProL512GbALow = usedIphoneSheet['E100'].value #Cell position for A Grade Low of a locked iPhone 11 Pro 512Gb
   _iPhone11ProL512GbBHigh = usedIphoneSheet['F100'].value #Cell position for B Grade High of a locked iPhone 11 Pro 512Gb
   _iPhone11ProL512GbBLow = usedIphoneSheet['G100'].value #Cell position for B Grade Low of a ocked iPhone 11 Pro 512Gb
   _iPhone11ProL512GbCHigh = usedIphoneSheet['H100'].value #Cell position for C Grade High of a locked iPhone 11 Pro 512Gb
   _iPhone11ProL512GbCLow = usedIphoneSheet['I100'].value #Cell position for C Grade Low of a locked iPhone 11 Pro 512Gb
   _iPhone11ProL512GbDHigh = usedIphoneSheet['J100'].value #Cell position for D Grade High of a locked iPhone 11 Pro 512Gb
   _iPhone11ProL512GbDLow = usedIphoneSheet['K100'].value #Cell position for D Grade Low of a locked iPhone 11 Pro 512Gb
   #Unlocked and Locked iPhone 11 Pro Prices
   #
   _iPhone11ProMax64GbAHigh = usedIphoneSheet['D104'].value #Cell position for A Grade High of a unlocked iPhone 11 Pro Max 64Gb
   _iPhone11ProMax64GbALow = usedIphoneSheet['E104'].value #Cell position for A Grade Low of a unlocked iPhone 11 Pro Max 64Gb
   _iPhone11ProMaxUL64GbBHigh = usedIphoneSheet['F104'].value #Cell position for B Grade High of a unlocked iPhone 11 Pro Max 64Gb
   _iPhone11ProMaxUL64GbBLow = usedIphoneSheet['G104'].value #Cell position for B Grade Low of a unlocked iPhone 11 Pro Max  64Gb
   _iPhone11ProMaxUL64GbCHigh = usedIphoneSheet['H104'].value #Cell position for C Grade High of a unlocked iPhone 11 Pro Max 64Gb
   _iPhone11ProMaxUL64GbCLow = usedIphoneSheet['I104'].value #Cell position for C Grade Low of a unlocked iPhone 11 Pro Max 64Gb
   _iPhone11ProMAxUL64GbDHigh = usedIphoneSheet['J104'].value #Cell position for D Grade High of a unlocked iPhone 11 Pro Max 64Gb
   _iPhone11ProMAxUL64GbDLow = usedIphoneSheet['K104'].value #Cell position for D Grade Low of a unlocked iPhone 11 Pro Max 64Gb
   _iPhone11ProMaxUL256GbAHigh = usedIphoneSheet['D105'].value #Cell position for A Grade High of a unlocked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxUL256GbALow = usedIphoneSheet['E105'].value #Cell position for A Grade Low of a unlocked iPhone 11 Pro Max 256Gb
   _iPhone11ProMAxUL256GbBHigh = usedIphoneSheet['F105'].value #Cell position for B Grade High of a unlocked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxUL256GbBLow = usedIphoneSheet['G105'].value #Cell position for B Grade Low of a unlocked iPhone1 1 Pro Max 256Gb
   _iPhone11ProMaxUL256GbCHigh = usedIphoneSheet['H104'].value #Cell position for C Grade High of a unlocked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxUL256GbCLow = usedIphoneSheet['I105'].value #Cell position for C Grade Low of a unlocked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxUL256GbDHigh = usedIphoneSheet['J105'].value #Cell position for D Grade High of a unlocked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxUL256GbDLow = usedIphoneSheet['K105'].value #Cell position for D Grade Low of a unlocked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxUL512GbAHigh = usedIphoneSheet['D106'].value #Cell position for A Grade High of a unlocked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxUL512GbALow = usedIphoneSheet['E106'].value #Cell position for A Grade Low of a unlocked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxUL512GbBHigh = usedIphoneSheet['F106'].value #Cell position for B Grade High of a unlocked iPhone 11 Pro Max 512Gb
   _iPhon11ProMaxSUL512GbBLow = usedIphoneSheet['G106'].value #Cell position for B Grade Low of a unlocked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxUL512GbCHigh = usedIphoneSheet['H106'].value #Cell position for C Grade High of a unlocked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxUL512GbCLow = usedIphoneSheet['I106'].value #Cell position for C Grade Low of a unlocked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxUL512GbDHigh = usedIphoneSheet['J106'].value #Cell position for D Grade High of a unlocked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxUL512GbDLow = usedIphoneSheet['K106'].value #Cell position for D Grade Low of a unlocked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxL64GbAHigh = usedIphoneSheet['D107'].value #Cell position for A Grade High of a locked iPhone 11 Pro Max 64Gb
   _iPhone11ProMaxL64GbALow = usedIphoneSheet['E107'].value #Cell position for A Grade Low of a locked iPhone 11 Pro max 64Gb
   _iPhone11ProMaxL64GbBHigh = usedIphoneSheet['F107'].value #Cell position for B Grade High of a locked iPhone 11 Pro Max 64Gb
   _iPhone11ProMaxL64GbBLow = usedIphoneSheet['G107'].value #Cell position for B Grade Low of a locked iPhone 11 Pro Max 64Gb
   _iPhone11ProMaxL64GbCHigh = usedIphoneSheet['H107'].value #Cell position for C Grade High of a locked iPhone 11 Pro Max 64Gb
   _iPhone11ProMaxL64GbCLow = usedIphoneSheet['I107'].value #Cell position for C Grade Low of a locked iPhone 11 Pro Max 64Gb
   _iPhone11ProMaxL64GbDHigh = usedIphoneSheet['J107'].value #Cell position for D Grade High of a locked iPhone 11 Pro Max 64Gb
   _iPhone11ProMaxL64GbDLow = usedIphoneSheet['K107'].value #Cell position for D Grade Low of a locked iPhone 11 Pro Max 64Gb
   _iPhone11ProMaxL256GbAHigh = usedIphoneSheet['D108'].value #Cell position for A Grade High of a locked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxL256GbALow = usedIphoneSheet['E108'].value #Cell position for A Grade Low of a locked iPhone 11 Max 256Gb
   _iPhone11ProMaxL256GbBHigh = usedIphoneSheet['F108'].value #Cell position for B Grade High of a locked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxL256GbBLow = usedIphoneSheet['G108'].value #Cell position for B Grade Low of a locked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxL256GbCHigh = usedIphoneSheet['H108'].value #Cell position for C Grade High of a locked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxL256GbCLow = usedIphoneSheet['I108'].value #Cell position for C Grade Low of a locked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxL256GbDHigh = usedIphoneSheet['J108'].value #Cell position for D Grade High of a locked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxL256GbDLow = usedIphoneSheet['K108'].value #Cell position for D Grade Low of a locked iPhone 11 Pro Max 256Gb
   _iPhone11ProMaxL512GbAHigh = usedIphoneSheet['D109'].value #Cell position for A Grade High of a locked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxL512GbALow = usedIphoneSheet['E109'].value #Cell position for A Grade Low of a locked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxL512GbBHigh = usedIphoneSheet['F109'].value #Cell position for B Grade High of a locked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxL512GbBLow = usedIphoneSheet['G109'].value #Cell position for B Grade Low of a ocked iPhone 11 Pro Max  512Gb
   _iPhone11ProMaxL512GbCHigh = usedIphoneSheet['H109'].value #Cell position for C Grade High of a locked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxL512GbCLow = usedIphoneSheet['I109'].value #Cell position for C Grade Low of a locked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxL512GbDHigh = usedIphoneSheet['J109'].value #Cell position for D Grade High of a locked iPhone 11 Pro Max 512Gb
   _iPhone11ProMaxL512GbDLow = usedIphoneSheet['K109'].value #Cell position for D Grade Low of a locked iPhone 11 Pro Max 512Gb

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



        