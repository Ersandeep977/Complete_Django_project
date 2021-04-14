from module import DBHepler

def main():
    db=DBHepler()
    while True:
        print("************WELCOME*******************")
        print()
        print("PRESS 1 to Insert new User")
        print("PRESS 2 to Display all User")
        print("PRESS 3 to Delete User")
        print("PRESS 4 to Update User")
        print("PRESS 5 EXIT program")
        print()
        try:
            choice=int(input())
            if (choice==1):
                uid=int(input("Enter user id:"))
                userName=input("Enter user Name:")
                userphone=input("Enter user phone:")
                db.insert_user(uid,userName,userphone)
            elif choice==2:
                db.fetch_all()
                pass
            elif choice == 3:
                userID=int(input("Enter User id to which you to delete"))
                db.delete_user(userID)
            elif choice == 4:
                uid = int(input("Enter user ID:"))
                userName = input("Enter New name:")
                userphone = input("Enter New Phone:")
                db.update_user(uid,userName,userphone)
            elif choice == 5:
                break
            else:
                print('Invalid Input ! try agin')
        except Exception as e:
            print(e)
            print("Invalid Input ! try agin")
if __name__=="__main__":
    main()