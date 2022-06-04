from dbhelper import DBHelper

def main():
    db=DBHelper
    
    while True:
        print("********WELCOME************\n")
        print("Press=>1 Insert data")
        print("Press=>2 Dispaly daata")
        print("Press=>3 Delete daata")
        print("Press=>4 Update daata")
        print("Press=>5 exit ")
        try:
            choice = int(input("Enter the choice:"))
            if choice == 1: 
                userid1=int(input("enter user id"))
                username=input("enterr name")
                phone=input("enter phone")
                db.insert_data(userid,username,phone)
                print("successfully")
            elif choice == 2:
                db.fetch_all()
                pass
            elif choice == 3:
                userid=int(input("enter user id t be deleted"))
                db.delete_record(userid)
                pass
            elif choice == 4:
                pass
            else:
                print("exit")
                break

        except:
            print("Please enter valid choice")


if __name__ == "__main__":
    main()
