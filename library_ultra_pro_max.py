
import mysql.connector
from datetime import date


fine_per_day =1.0
def clear():
  for _ in range(65):
     print("!",end="")


def add_book():
  conn = mysql.connector.connect(
       host='localhost', database='dj1',port='3307',user='root',password='dj123')
  cursor = conn.cursor()

  title = input('Enter Book Title :')
  author = input('Enter Book Author : ')
  publisher = input('Enter Book Publisher : ')
  pages = input('Enter Book Pages : ')
  price = input('Enter Book Price : ')
  edition = input('Enter Book Edition : ')
  copies  = int(input('Enter copies : '))
  sql = 'insert into book(title,author,price,pages,publisher,edition,status) values ( "' + \
       title + '","' + author+'",'+price+','+pages+',"'+publisher+'","'+edition+'","available");'
  for _ in range(0,copies):
    cursor.execute(sql)
  conn.commit()
  conn.close()
  print('\n\nNew Book added successfully')
  wait = input('\n\n\n Press any key to continue....')


def add_member():
  conn = mysql.connector.connect(
      host='localhost', database='dj1',port='3307', user='root', password='dj123')
  cursor = conn.cursor()

  name = input('Enter Member Name :')
  clas = input('Enter Member Class & Section : ')
  address = input('Enter Member Address : ')
  phone = input('Enter Member Phone  : ')
  email = input('Enter Member Email  : ')
  
 
  sql = 'insert into member(name,class,address,phone,email) values ( "' + \
      name + '","' + clas+'","'+address+'","'+phone + \
        '","'+email+'");'  
  cursor.execute(sql)
  conn.commit()
  conn.close()
  print('\n\nNew Member added successfully')
  wait = input('\n\n\n Press any key to continue....')


def modify_book():
    conn = mysql.connector.connect(
        host='localhost', database='dj1',port='3307', user='root', password='dj123')
    cursor = conn.cursor()
    clear()
    print('Modify BOOK Details Screen ')
    print('-'*120)
    print('\n1. Book Title')
    print('\n2. Book Author')
    print('\n3. Book Publisher')
    print('\n4. Book Pages')
    print('\n5. Book Price')
    print('\n6. Book Edition')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'title'
    if choice == 2:
        field = 'author'
    if choice == 3:
        field = 'publisher'
    if choice == 4:
        field = 'pages'
    if choice == 5:
        field = 'price'
    book_id = input('Enter Book ID :')
    value = input('Enter new value :')
    if field =='pages' or field == 'price':
        sql = 'update book set ' + field + ' = '+value+' where id = '+book_id+';'
    else:
        sql = 'update book set ' + field + ' = "'+value+'" where id = '+book_id+';'

    cursor.execute(sql)
    print('\n\n\nBook details Updated.....')
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def modify_member():
    conn = mysql.connector.connect(
        host='localhost', database='dj1', user='root',port='3307', password='dj123')
    cursor = conn.cursor()
    clear()
    print('Modify Memeber Information Screen ')
    print('-'*120)
    print('\n1. Name')
    print('\n2. Class')
    print('\n3. address')
    print('\n4. Phone')
    print('\n5. Emaile')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field =''
    if choice == 1:
        field ='name'
    if choice == 2:
        field = 'class'
    if choice ==3:
        field ='address'
    if choice == 4:
        field = 'phone'
    if choice == 5:
        field = 'email'
    mem_id =input('Enter member ID :')
    value = input('Enter new value :')
    sql = 'update member set '+ field +' = "'+value+'" where id = '+mem_id+';'

    cursor.execute(sql)
    print('Member details Updated.....')
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def mem_issue_status(mem_id):
    conn = mysql.connector.connect(
        host='localhost', database='dj1', user='root',port='3307',password='dj123')
    cursor = conn.cursor()
    sql ='select * from transaction where m_id ='+mem_id +' and dor is NULL;'
    #print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results



def book_status(book_id):
    conn = mysql.connector.connect(
        host='localhost', database='dj1',port='3307',user='root', password='dj123')
    cursor = conn.cursor()
    sql = 'select * from book where id ='+book_id + ';'
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[5]

def book_issue_status(book_id,mem_id):
    conn = mysql.connector.connect(
        host='localhost', database='dj1',port='3307',user='root', password='dj123')
    cursor = conn.cursor()
    sql = 'select * from transaction where b_id ='+book_id + ' and m_id ='+ mem_id +' and dor is NULL;'
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def issue_book():
    conn = mysql.connector.connect(
      host='localhost', database='dj1',port='3307',user='root', password='dj123')
    cursor = conn.cursor()

    clear()
    print('\n BOOK ISSUE SCREEN ')
    print('-'*120)
    book_id = input('Enter Book  ID : ')
    mem_id  = input('Enter Member ID :')
   
    
    result = book_status(book_id)
    result1 = mem_issue_status(mem_id)
    #print(result1)
    today = date.today()
    if len(result1) == 0:
      if result == 'available':
          sql = 'insert into transaction(b_id, m_id, doi) values('+book_id+','+mem_id+',"'+str(today)+'");'
          sql_book = 'update book set status="issue" where id ='+book_id + ';'
          cursor.execute(sql)
          cursor.execute(sql_book)
          print('\n\n\n Book issued successfully')
      else:
          print('\n\nBook is not available for ISSUE... Current status :',result1)
    else:
      if len(result1)<1:
        sql = 'insert into transaction(b_id, m_id, doi) values(' + \
             book_id+','+mem_id+',"'+str(today)+'");'
        sql_book = 'update book set status="issue" where id ='+book_id + ';'
        #print(len(result))
        cursor.execute(sql)
        cursor.execute(sql_book)
        print('\n\n\n Book issued successfully')
      else:
        print('\n\nMember already have book from the Library')
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def return_book():
    conn = mysql.connector.connect(
        host='localhost', database='dj1',port='3307',user='root', password='dj123')
    cursor = conn.cursor()
    global fine_per_day
    clear()
    print('\n BOOK RETURN SCREEN ')
    print('-'*120)
    book_id = input('Enter Book  ID : ')
    mem_id = input('Enter Member ID :')
    today =date.today()
    result = book_issue_status(book_id,mem_id)
    if result==None:
       print('Book was not issued...Check Book Id and Member ID again..')
    else:
       sql='update book set status ="available" where id ='+book_id +';'
       din = (today - result[3]).days
       fine = din * fine_per_day    #  fine per data
       sql1 = 'update transaction set dor ="'+str(today)+'" , fine='+str(fine)+' where b_id='+book_id +' and m_id='+mem_id+' and dor is NULL;' 
       
       cursor.execute(sql)
       cursor.execute(sql1)
       print('\n\nBook returned successfully')
    conn.commit()
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def main_menu():
    while True:
      clear()
      print(' L I B R A R Y    M E N U')
      print("\n1.  Add Books")
      print('\n2.  Add Member')
      print('\n3.  Modify Book Information')
      print('\n4.  Modify Student Information')
      print('\n5.  Issue Book')
      print('\n6.  Return Book')
      
      print('\n0.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_book()
      if choice == 2:
        add_member()
      if choice == 3:
        modify_book()
      if choice == 4:
        modify_member()
      if choice == 5:
        issue_book()
      if choice == 6:
        return_book()
      
        
      if choice == 0:
        break


if __name__ == "__main__":
    main_menu()

