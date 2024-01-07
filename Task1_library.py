import pandas as pd

#-------Data Base------------------------------------------------------------------------------------

#Sample books in the role of data in the database
database = {
    'id': [1],
    'name': ['Mystery'],
    'writer':['peter'] ,
    'subject': ['action'],
    'number_of_page': ['220']
}

#--------class---------------------------------------------------------------------------------------
class libaray():

    #bookid use for primary key at database in future
    bookid = len(database['id'])+1
    name = None
    writer = None
    subject = None
    number_of_page = None

    #-----------add----------------------------------------------
    def add_book(self,name,writer,subject,number_of_page):
        dct = {
                'id':self.bookid,
                'name':name,
                'writer':writer,
                'subject':subject,
                'number_of_page':number_of_page
              }
        for key,value in dct.items():
            database[key].append(value)  
        print('The book was added to the list of available books.')

    #----------delete--------------------------------------------
    def delete_book(self,bookid):
        if bookid in database['id']:
            indx = database['id'].index(bookid)
            for i in database.keys():
                database[i].pop(indx)
            print('your book is deleted.')
        else:
            print('your book in not found')

    #-----------update-------------------------------------------
    def update_book(self,bookid,updatename,updatewriter,updatesubject,updatenumber_of_page):
        if bookid in database['id']:
            indx = database['id'].index(bookid)
            a,b,c,d,f = database.values()
            a = a
            b[indx] = updatename
            c[indx] = updatewriter
            d[indx] = updatesubject
            f[indx] = updatenumber_of_page
    #------------------------------------------------------
    def search_book_by_id(self,bookid):
        if bookid in database['id']:
            indx = database['id'].index(bookid)
            a,b,c,d,f = database.values()
            return [a[indx],b[indx],c[indx],d[indx],f[indx]]
        
    #------------------------------------------------------
    def search_book_by_name(self,bookname):
        if bookname in database['name']:
            indx = database['name'].index(bookname)
            a,b,c,d,f = database.values()
            return [a[indx],b[indx],c[indx],d[indx],f[indx]]


#--------client code-----------------------------------------------------------------------------------------------------
        
#----------add book----------------------------
book_name = libaray()
book_name.add_book(
    input('please enter your book name : '),
    input('please enter book writer : '),
    input('please enter subject : '),
    input('please enter number of page : ')
)
df = pd.DataFrame(database)
print(df)
print('*'*50)
#-------delete book----------------------------
a = libaray()
a.delete_book(2)
print('*'*50)
#-------update book----------------------------
a.update_book(1,'ali','test','test','test')
df = pd.DataFrame(database)
print(df)
print('*'*50)
#-------search--------------------------------
print(a.search_book_by_id(1))
print(a.search_book_by_name('ali'))

