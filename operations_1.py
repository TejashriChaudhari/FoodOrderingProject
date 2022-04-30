import json
import string
import random
from json import JSONDecodeError

def Register(x,admins_1_json_file,users_1_json_file,Full_name,Phone_no,Address,Email_ID,Password):
    if x.lower()=="admin":
        fp= open(admins_1_json_file,"r+") 
        d={
            "Full_name":Full_name,
                "Phone_no":Phone_no,
                "Address":Address,
                "Email_ID":Email_ID,
                "Password":Password
               }
        try:
            content=json.load(fp)
            if d not in content:
                content.append(d)
                fp.seek(0)
                fp.truncate()
                json.dump(content,fp)
        except JSONDecodeError: 
            l=[]
            l.append(d)
            json.dump(l,fp)
        fp.close()    
       

    elif x.lower()=="users":
        fp=open(users_1_json_file,"r+")
        d={
                "Full_name":Full_name,
                 "Phone_no":Phone_no,
                  "Address":Address,
                   "Email_ID":Email_ID,
                   "Password":Password
                }
        try:
            content=json.load(fp)
            if d not in content:
                content.append(d)
                fp.seek(0)
                fp.truncate()
                json.dump(content,fp)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,fp)
        fp.close() 
        return True ##I didn't get this line         

            
def Login(x,admins_1_json_file,users_1_json_file,Email_ID,Password):
    if x.lower()=="admin":
        fp= open (admins_1_json_file,"r+")

    else:
        fp=open(users_1_json_file,"r+")

    try:
        content=json.load(fp)
    except:
        return False
    for i in range(len(content)):
        if content[i]["Email_ID"]==Email_ID and content[i]["Password"]==Password:
            d=True
            break
    fp.seek(0)
    fp.truncate()
    json.dump(content,fp)
    fp.close()
    # if d==0:
    #     return False
    return True        

def Auto_generated_Food_ID():
    f_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=4))
    return f_ID

def Auto_generated_Order_ID():
    O_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return O_ID


def Add_item(admin,menu1_json_file,f_ID,food_name,food_quantity,food_price,food_discount,available_stock):
    fp=open(menu1_json_file,"r+")
    d={
       "created by":admin,
       "Food ID": f_ID,
       "Food name":food_name,
       "Food quantity": food_quantity,
       "Food price": food_price,
       "Food discount":food_discount,
       "Available stock": available_stock
       }
    try:
        content=json.load(fp)
        if d not in content:
            content.append(d)
            fp.seek(0)
            fp.truncate()
            json.dump(content,fp)
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l,fp)  
    fp.close()    
       
def View_item(admin,menu1_json_file):
    fp=open(menu1_json_file,"r+")
    content=json.load(fp)
    itemlist=[]
    for i in content:
        if i["Created by"]==admin:
            itemlist.append(i)
    fp.close()

def View_item_by_Food_ID(menu1_json_file,f_id,details):
    fp=open(menu1_json_file,"r+")
    content=json.load(fp)
    for i in content:
        if i["Food ID"]==f_id:
            details.append(i)
            break
    fp.close()    

def Update_item(menu1_json_file,f_id,details_to_be_updated,new_value):
    fp=open(menu1_json_file,"r+")
    d={details_to_be_updated:new_value}
    try:
        content=json.load(fp)
        for i in content:
            if i["Food ID"]==f_id:
                i.update(d)
                fp.seek(0)
                fp.truncate()
                json.dump(content,fp)
                break
    except JSONDecodeError:
        return False
    fp.close()   
    return True 
               
def Delete_item(menu1_json_file,f_id):
    fp=open(menu1_json_file,"r+")
    try:
        content=json.load(fp)
        for i in content:
            if i["Food ID"]==f_id:
                del content[content.index(i)]
                fp.seek(0)
                fp.truncate()
                json.dump(content,fp)
                break
    except JSONDecodeError:
        return False
    fp.close()   
    return True 


def Update_profile(menu1_json_file,delivery_address,details_to_be_updated,Full_name):
    fp=open(menu1_json_file,"r+")
    d={details_to_be_updated:delivery_address}
    try:
        content=json.load(fp)
        for i in content:
            if i["Full name"]==Full_name:
                i.update(d)
                fp.seek(0)
                fp.truncate()
                json.dump(content,fp)
                break
    except JSONDecodeError:
        return False
    fp.close()   
    return True 
    
def Place_order(orders1_json_file,price_after_discount,price,discount,Order_ID,Food_name,quantity,f_id,ordered_by, delivery_address
):
    fp=open(orders1_json_file,"r+")
    price_after_discount=float(float(price)-((float(price)*float(discount[:-1]))/100))
    d={
        "Ordered by": Order_ID,
        "Food_name":  Food_name, 
        "Price":price,
        "Discount":discount,
        "Price_after_discount":price_after_discount,
        "Quantity":quantity,
        "Food ID": f_id,
        "Total cost":quantity*price_after_discount,
        "Ordered by":ordered_by,
        "Delivery address": delivery_address
         }
    try:
        content=json.load(fp)
        content.append(d)
        fp.seek(0)
        fp.truncate()
        json.dump(content,fp)
    except:
        l=[]
        l.append(d)
        json.dump(l,fp)
    fp.close()
    return True    


def Order_history(orders1_json_file,Name,details):
    fp=open(orders1_json_file,"r+")
    try:
        content=json.load(fp)
        for i in content:
            if i["Ordered by"]==Name:
                details.append(i)
    except JSONDecodeError:
        return False
    fp.close()   
    return True 
