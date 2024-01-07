#----------------------data base-------------------------------------------------------
database = {
    'customerid':[1],
    'accountnumber':['1234'],
    'name': ['ali'],
    'cash' : [350000],
    'password': ['admin']
}
#----------------------class-------------------------------------------------------
class bank():

    #customer id  used for database
    customerid = len(database['customerid'])+1
    accountnumber = None
    name = None
    cash = None
    password = None

    #----------create account----------------------------------------
    def createaccount(self,accountnumber,name,cash,password):
        dct = {
            'customerid':self.customerid,
            'accountnumber':accountnumber,
            'name': name,
            'cash' : cash,
            'password': password
        }
        for key,value in dct.items():
            database[key].append(value)  
        print('your account is created.')

    #-----------delete account-----------------------------------------------------
    def deletaccount(self,cid):
        if cid in database['customerid']:
            indx = database['customerid'].index(cid)
            for i in database.keys():
                database[i].pop(indx)
            print('your count is deleted')
        else:
            print('your account is not found')

    #------------------------------------------------------------------------------
    def setcash(self,cid,gcash):
        if cid in database['customerid']:
            indx = database['customerid'].index(cid)
            csh = database['cash']
            csh[indx] = gcash+csh[indx]
            print('your cash is update')
        else:
            print('your account is not found.')
    
    
    #------------------------------------------------------------------------------
    def getcash(self,cid,scash):
        if cid in database['customerid']:
            indx = database['customerid'].index(cid)
            csh = database['cash']
            csh[indx] = csh[indx]-scash
            print('your cash is update')
        else:
            print('your account is not found.')
    
    #--------------#read cash-------------------------------------------------------
    def readcash(self,cid):

        if cid in database['customerid']:
            indx = database['customerid'].index(cid)
            for i in database.keys():
                lst = []
                lst.append(database[i].pop(indx))
            return lst
        else:
            return 'your account is not found'

#---------------------------------------------------------------
    
#------------client code----------------------------------------
    
customer1 = bank()
customer1.createaccount(
    input('please enter your accountnumber : '),
    input('please enter your name : '),
    int(input('please enter your cash : ')),
    input('please enter your password : ')

)
print(database)
print("*"*50)

customer1.deletaccount(1)
print(database)
print("*"*50)

customer1.readcash(1)
print(database)
print("*"*50)


customer1.setcash(2,50)
print(database)
print("*"*50)

customer1.getcash(2,20)
print(database)
print("*"*50)