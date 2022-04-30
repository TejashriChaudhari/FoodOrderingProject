import operations_1
import json
from json import JSONDecodeError
print("-------------------------(: Welcome to AaojiKhawoji!!! :) -------------------------------")
a=1
while a!=0:
    print("Press")
    print("0 for exit")
    print("1 for admin's registration")
    print("2 for users' registration")
    print("3 for admin's login ")
    print("4 for users' login")

    m=int(input("Now enter no: "))
    if m==1:
        print("Enter your full name")
        F=input()
        print("Enter your phone no")
        PN=input()
        print("Enter your address")
        A=input()
        print("Enter your email ID")
        E=input()
        print("Create your password")
        P=input()
        
        if len(F)!=0 and  len(PN)!=0 and len(A)!=0 and len(P)!=0  and "@" in E and ".com" in E :
            operations_1.Register("admin","admins_1.json","users_1.json",F,PN,A,E,P)
            print("Registration for admin has SUCCESSFUL!!!")
        else:
            print("Registration has failed, please try again")
   

    elif m==2:
        print("Enter your full name")
        F=input()
        print("Enter your phone no")
        PN=input()
        print("Enter your address")
        A=input()
        print("Enter your email ID")
        E=input()
        print("Create your password")
        P=input()
        
        if len(F)!=0 and  len(PN)!=0 and len(A)!=0 and len(P)!=0  and "@" in E and ".com" in E :
            cond=operations_1.Register("users","admins_1.json","users_1.json",F,PN,A,E,P)  ##as we have to pass info ,after satisfying the cond thats y we are passing address of py operation file inside if cond
            if cond==True:
                print("Registration for user has SUCCESSFUL!!!")
        else:
            print("Registration has failed, please try again")
 

    elif m==3:
        print("Enter your Email ID")
        E=input()
        print("Enter your password")
        P=input()
        cond=operations_1.Login("admin","admins_1.json","users_1.json",E,P)
        if cond==True:
            with open ("admins_1.json","r") as fp:
               content1=json.load(fp)
               admin_details=[]
               for i in range(len(content1)):
                   if content1[i]["Email_ID"]==E and content1[i]["Password"]==P:
                       admin_details.append(content1)
                       break ##this break is to stop further iteration after satisfying require cond
               while True:
                    print("Press")
                    print("0 for exit")
                    print("1 for add an item")
                    print("2 for view an item list")
                    print("3 for update an item")
                    print("4 for delete an item")
                    n=int(input())
                    if n==1:
                        f_ID=operations_1.Auto_generated_Food_ID()
                        print("Generated Food id is: "+str(f_ID))
                        print("Enter food name: ")
                        food_name=input()
                        print("Enter food quantity: ")
                        food_quantity=input()
                        print("Enter Food price: ")
                        food_price=input()
                        print("Enter discount for food: ")
                        food_discount=input()
                        if   "%" not in food_discount:
                            food_discount+="%"
                        print("Enter available stock: ")
                        available_stock=input()
                        try:
                           int(food_price)
                        except ValueError:
                           food_price=""
                        try:
                           int(available_stock)
                        except:
                           available_stock=""
                        if len(f_ID)!=0 and len(food_name)!=0 and len(food_quantity)!=0 and len(food_price)!=0 and len(food_discount)!=0 and len(available_stock)!=0 and len(admin_details[0])!=0:
                            cond1=operations_1.Add_item((admin_details[0][0]),"menu_1.json",f_ID,food_name,food_quantity,food_price,food_discount,available_stock)
                            if cond1==True:
                                print("Items added successfully")
                            
                        else:
                            print("Please provide valid data") 
                    elif n==2:
                        print("Press")
                        print("1 for view all items")       
                        print("2 for view item by food id")
                        o=int(input())
                        if o==1:
                            cond2=operations_1.View_item(admin_details[0],"menu_1.json")
                            if len(cond2)==0:
                                print("No item has added yet!!")
                            else:
                                for i in range(len(cond2)):
                                    print("Admin name:"+str(cond2[i]["Admin name"]))
                                    print("Food ID: "+str(cond2[i]["f_id"]))
                                    print("Food Name: "+str(cond2[i]["food_name"]))
                                    print("Food Quantity: "+str(cond2[i]["food_quantity"]))
                                    print("Food discount: "+str(cond2[i]["food_discount"]))
                                    print("Available stock of food: "+str(cond2[i]["available_stock"]))
                        elif o==2:
                            print("Food ID: ")
                            f_ID=(input())    
                            details=[]
                            operations_1.View_item_by_Food_ID("menu_1.json",f_ID,details)
                            if len(details)==0:
                                print("Invalid data")
                            else:
                                print("Admin name:"+str(cond[i]["Admin name"]))
                                print("Food ID: "+str(details[i]["Food ID"]))
                                print("Food Name: "+str(details[i]["Food Name"]))
                                print("Food Quantity: "+str(details[i]["Food Quantity"]))
                                print("Food discount: "+str(details[i]["Discount"]))
                                print("Available stock of food: "+str(details[i]["Total Stock Available"]))  

                        else:
                            print("Invalid choice")

                    elif n==3:
                        print("Enter food id")
                        f_ID=input()
                        print("Enter the details which you have to update:")
                        details_to_be_updated=input()
                        print("Enter updated details: ")
                        dt_updated=input()
                        cond3=operations_1.Update_item("menu_1.json",f_ID,details_to_be_updated,dt_updated)
                        if cond3==True:
                            print("Items updated successfully!!")
                        else:
                            print("Invalid details of items")

                    elif n==4:
                        print("Enter food id")
                        f_ID=input()
                        cond4=operations_1.Delete_item("menu_1.json",f_ID)
                        if cond4==True:
                            print("Items deleted successfully!!")
                        else:
                            print("Invalid food id,try again")   

                    elif n==0:
                        break
                    else:
                        print("Invalid choice")    
        else:
            print("Invalid login credentials") 

    elif m==4:
        print("Enter your email ID:" )
        E=input()
        print("Enter your password: ")
        P=input()
        cond5=operations_1.Login("users","users_1.json","admins_1.json",E,P)
        if cond5== True:
            fp=open("users_1.json","r")
            content2=json.load(fp)
            users_details=[]
            for i in range(len(content2)):
                if content2[i]["Email_ID"]==E and content2[i]["Password"] ==P:
                    users_details.append(content2[i])
                    break
                while True:
                    print("Press")
                    print("1  for create an order")
                    print("2  for  view an order history")
                    print("3 for updation of profile ")
                    print("4 for logging out")
                    p=int(input())
                    if p==1:
                        fp=open("menu_1.json","r")
                        try:
                            content3=json.load(fp)
                            fp.close()
                            print("Available items are:")
                            for i in range(len(content3)):
                                print(content3[i]["Food ID"])
                            print("Enter your food id")
                            f_ID=input()
                            print("Enter quantity of food:")
                            food_quantity=int(input())
                            O_id=operations_1.AutoGenerate_OrderID()
                            cond6=operations_1.Place_order("orders_1.json",users_details[0]["Full name"])
                            if cond6==True:
                                print("Your order has placed successfully with order id: "+str(O_id))
                            else:
                                print("Order has unsuccessful!!!")
                        except:
                            print("No items are available,please order something else")

                    elif p==2:
                        l=[]
                        operations_1.Order_history("orders_1.json",users_details[0]["Full name"],l) 
                        if len(l)==0:
                            print("No orders are placed yet")
                        else:
                            for i in range(len(l)):
                                print("Order ID: "+str(l[i]["Order ID"]))
                                print("Food Name: "+str(l[i]["Food name"]))  
                                print("MRP: "+str(l[i]["Price"]))
                                print("Discount: "+str(l[i]["Discount"]))
                                print("Price after Discount: "+str(l[i]["Price after Discount"]))
                                print("Quantity: "+str(l[i]["Quantity"]))
                                print("Grand Total: "+str(l[i]["Total Cost"]))
                                print("Delivering to: "+str(l[i]["Delivering to"]))             
                    
                    elif p==3:
                        print("Enter details to be updated")
                        details_tb_updated=input()
                        print("Enter updated detail: ")
                        updated_detail=input()
                        cond7=operations_1.Update_profile("users_1.json",users_details[0]["Full name"],details_tb_updated,updated_detail)
                        if cond7==True:
                            print("Details of user updated successfully!!!")
                        else:
                            print("Invalid details")
                    else:
                        print("Invalid given data")

    elif m==0:
        break
    else:
        print("Invalid choice")







                                    
                             





                        

                               


                


                