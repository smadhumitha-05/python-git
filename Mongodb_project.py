from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from pymongo import ReturnDocument

mongourl=MongoClient("mongodb+srv://Madhumitha:madhu123@cluster0.e7embqe.mongodb.net/?appName=Cluster0")
mydatabase=mongourl["ecommerce-project"]
usercollection=mydatabase["user"]
productcollection=mydatabase["product"]
ordercollecttion=mydatabase["order"]


#========================= USER COLLECTION =============================


# TASK 1 - Add user data collection

usercollection.create_index("email",unique=True)
def add_user():
    try:
        name=input("Enter your name:")
        email=input("Enter your email:")
        password=input("Enter your password:")
        mobile=input("Enter your mobile number:")
        address=input("Enter your address:")

        if not name:
            print("Name cannot be empty")
            return
        
        if not email:
            print("Email cannot be empty")
            return
        
        if not password:
            print("Password cannot be empty")
            return

        if not mobile:
            print("Mobile number cannot be empty")
            return

        if not address:
            print("Address cannot be empty")
            return
        
        user_data={
            "name":name,
            "email":email,
            "password":password,
            "mobile":mobile,
            "address":address,
            "createdAt":datetime.now()
        }

        result=usercollection.insert_one(user_data)
        print("user added successfully😀")

    except DuplicateKeyError:
        print("Email already exists⚠️")


#TASK 2 - Check Email & Password
def check_login():
    mail=input("Enter your email:")
    pword=input("Enter your pword:")

    user=usercollection.find_one({
        "email":mail,
        "password":pword
    })

    if user:
        print("Login successfully✅")
    else:
        print("Invalid email or password⚠️")


#TASK 3 - Get all users data
def getAllusers():
    users=usercollection.find()
    count=1
    for i in users:
        print("User",count)
        print("_id:",i["_id"])
        print("Name:",i["name"])
        print("Email:",i["email"])
        print("Mobile:",i["mobile"])
        print("Address:",i["address"])
        print("Created At:",i["createdAt"])
        print("---------------------------")

        count+=1

        
#TASK 4 - Get specific user data
def getspecificuserdata():
    try:
        user_id=input("Enter user id:")
        specificdata=usercollection.find_one({"_id":ObjectId(user_id)})

        if specificdata:
            print("User")

            print("Name:",specificdata["name"])
            print("Email:",specificdata["email"])
            print("Mobile:",specificdata["mobile"])
            print("Address:",specificdata["address"])
            print("Created At:",specificdata["createdAt"])
            print("---------------------------")

        else:
            print("User not found❌")

    except Exception as e:
        print("Error:",e)


#TASK 5 - Update user data
def updateuser():
    try:
        user_id=input("Enter user id:")
        user=usercollection.find_one({
            "_id":ObjectId(user_id),
        })

        if not user:
            print("User not found")
            return

        name=input("Enter your name to update:")
        email=input("Enter your email to update:")
        password=input("Enter your password to update:").strip()
        mobile=input("Enter your mobile number to update:").strip()
        address=input("Enter your address to update:").strip()

        update_data={}
        if name:
            update_data["name"]=name
        if email:
            update_data["email"]=email
        if password:
            update_data["password"]=password
        if mobile:
            update_data["mobile"]=mobile
        if address:
            update_data["address"]=address

        if update_data:
            usercollection.update_one(
                {"_id":ObjectId(user_id)},
                {"$set":update_data}
            ) 

            print("User updated successfully✅")
        else:
            print("No changes made")

    except DuplicateKeyError:
        print("Email already exists⚠️")
    except Exception:
        print("Invalid user ID⚠️")
    
#TASK 6 - Delete user data
def deleteuserData():
    try:
        user_id=input("Enter a user id:")
        userrecord=usercollection.find_one_and_delete({"_id":ObjectId(user_id)})

        if userrecord:
            print("Data deleted successfully🗑️")
        else:
            print("User not found❌")
    except Exception as e:
        print("Error:",e)


#========================= PRODUCT COLLECTION =============================


# TASK 7 - Add product collection
def add_product():
        
    name=input("Enter product name:")
    price=int(input("Enter product price:"))
    model=input("Enter product model:")
    color=input("Enter product color:")
    stock=int(input("Enter product stock:"))
    discount=int(input("Enter product discount (%):"))

    if not name:
        print("Name cannot be empty")
        return
    if not price:
        print("Price cannot be empty")
        return
    if not model:
        print("Model cannot be empty")
        return
    if not color:
        print("Color cannot be empty")
        return
    if not stock:
        print("Stock cannot be empty")
        return
    if not discount:
        print("Discount cannot be empty")
        return

    product={
        "name":name,
        "price":price,
        "model":model,
        "color":color,
        "stock":stock,
        "discount":discount
    }

    productcollection.insert_one(product)
    print("Product added successfully✅")



#TASK 8 - Get all product data
def getallproductdata():
    product=productcollection.find()
    count=1
    for i in product:
        print("Product",count)
        print("_id:",i["_id"])
        print("Name:",i["name"])
        print("Price:",i["price"])
        print("Model:",i["model"])
        print("Color:",i["color"])
        print("Stock:",i["stock"])
        print("Discount:",i["discount"])
        print("---------------------------")

        count+=1

#TASK 9 - Get specific data
def getspecificproduct():
    try:
        product_id=input("Enter product id:")
        specificdata=productcollection.find_one({"_id":ObjectId(product_id)})
        if specificdata:
            print("Product")

            print("Name:",specificdata["name"])
            print("Price:",specificdata["price"])
            print("Model:",specificdata["model"])
            print("Color:",specificdata["color"])
            print("Stock:",specificdata["stock"])
            print("Discount:",specificdata["discount"])
            print("---------------------------")

        else:
            print("User not found❌")

    except Exception as e:
        print("Error:",e)


#TASK 10 - Update product data
def updateproduct():
    try:
        product_id=input("Enter product id:")
        product=productcollection.find_one({
            "_id":ObjectId(product_id)
        })

        if not product:
            print("Product not found")
            return

        name=input("Enter new name:")
        price=input("Enter new price:")
        model=input("Enter new model:")
        color=input("Enter new color:")
        stock=input("Enter new stock:")
        discount=input("Enter new discount:")

        update_data={}
        if name:
            update_data["name"]=name
        if price:
            update_data["price"]=float(price)
        if model:
            update_data["model"]=model
        if color:
            update_data["color"]=color
        if stock:
            update_data["stock"]=int(stock)
        if discount:
            update_data["discount"]=float(discount)

        if update_data:
            productcollection.update_one(
                {"_id":ObjectId(product_id)},
                {"$set":update_data}
            )

            print("Product updated successfully✅")
        else:
            print("No changes made")


    except Exception:
        print("Invalid product ID")

    
#TASK 11 - Delete product data
def deleteproductData():
    try:
        product_id=input("Enter a product id:")
        productrecord=productcollection.find_one_and_delete({"_id":ObjectId(product_id)})

        if productrecord:
            print("Data deleted successfully🗑️")
        else:
            print("product not found❌")
    except Exception as e:
        print("Error:",e)


# =========================== ORDER COLLECTION =============================


# TASK 12 - Order product
def place_order():
    try:
        user_id=input("Enter userID:")
        product_id=input("Enter productID:")
        quantity=int(input("Enter quantiy:"))
        is_paid=input("Is paid? (True/False):")

        user_id=ObjectId(user_id)
        product_id=ObjectId(product_id)

        user=usercollection.find_one({
            "_id":user_id
        })

        product=productcollection.find_one({
            "_id": product_id
        })

        if user is None:
            print("User not found❌")
            return
        if product is None:
            print("Product not found❌")
            return
        if quantity<=0:
            print("Invalid quantity")
            return
        if product["stock"]<quantity:
            print("Insufficient stock")
            return
        is_paid = is_paid.lower()=="true"
        price=float(product["price"])
        discount=float(product["discount"])
        total_price= price * quantity
        discount_amount= total_price * discount/100
        amount= total_price - discount_amount
        order_data={
            "userID":user_id,
            "productID":product_id,
            "amount":amount,
            "ispaid":is_paid,
            "quantity":quantity,
            "orderedData":datetime.now(),
            "isdelivered":False
        }

        ordercollecttion.insert_one(order_data)
        productcollection.update_one(
            {
                "_id": product_id
            },
            {
                "$inc":{
                    "stock":-quantity
                }
            }
        )

        print("\n====================ORDER SUMMARY======================")

        print("User ID:",user_id)
        print("Product ID:",product_id)
        print("Price:",price)
        print("Discount:",discount,"%")
        print("Quantity:",quantity)
        print("Total Amount:",amount)
        print("Is Paid:",is_paid)
        print("Is Delivered:",False)

        print("Order placed successfully✅")

    except Exception as e:
        print("Error:",e)


# TASK 13 - Get all ordered product details & user details
def get_all_ordersdetails():
    try:
        orders=ordercollecttion.find()
        count=1
        for order in orders:
            user=usercollection.find_one({
                "_id":order["userID"]
            })

            product=productcollection.find_one({
                "_id":order["productID"]
            })

            print("\nOrder",count)
            if user is not None:
                print("\nUser Details")
                print("User Name:",user["name"])
                print("User Email:",user["email"])
                print("Mobile:",user["mobile"])
                print("Address:",user["address"])
                print("CreatedAt:",user["createdAt"])
            else:
                print("\nUser Details not found")

            if product is not None:
                print("\nProduct Details")
                print("Product Name:",product["name"])
                print("Price:",product["price"])
                print("Model:",product["model"])
                print("Color:",product["color"])
                print("Discount:",product["discount"],"%")
            else:
                print("\nProduct Details not found")
            print("\nOrder Details")
            print("Quantity:",order["quantity"])
            print("Amount:",order["amount"])
            print("isPaid:",order["ispaid"])
            print("OrderedData:",order["orderedData"])
            print("isDelivered:",order["isdelivered"])
            print("-----------------------------------")
            
            count+=1

    except Exception as e:
        print("Error:",e)


# TASK 14 - Get ordered product by passing user ID
def getorderdetails_by_userid():
    user_id=input("Enter user ID:")
    try:
        user_id=ObjectId(user_id)
        orders=ordercollecttion.find({
            "userID":user_id
        })
        count=1
        for i in orders:
            print("\nOrder",count)
            print("User ID:",i["userID"])
            print("Product ID:",i["productID"])
            print("Amount:",i["amount"])
            print("isPaid:",i["ispaid"])
            print("Quantity:",i["quantity"])
            print("OrderedData:",i["orderedData"])
            print("isDelivered:",i["isdelivered"])
            print("-------------------------------")

            count+=1
    except Exception as e:
        print("Error:",e)


# TASK 15 - Update isDelivered Status True
def update_delivery_status():
    order_id=input("Enter order ID:")
    result=ordercollecttion.update_one(
        {
            "_id":ObjectId(order_id)
        },
        {
            "$set":{
                "isdelivered":True
            }
        }
    )
    if result.modified_count>0:
        print("Delivery status updated successfully✅")
    else:
        print("Order not found or already delivered")



# ==============================USER MENU====================================

def usermenu():
    while True:
        print("\nHi😇")
        print("WELCOME TO USER COLLECTION ")

        print("1. Add User")
        print("2. Login")
        print("3. Get All Users")
        print("4. Get Specific User")
        print("5. Update User")
        print("6. Delete User")
        print("7. Exit")

        choice=input("Enter your choice:")
        if choice=="1":
            print("Come on lets create a account🙌")
            add_user()
        elif choice=="2":
            check_login()
        elif choice=="3":
            getAllusers()
        elif choice=="4":
            getspecificuserdata()
        elif choice=="5":
            updateuser()
        elif choice=="6":
            deleteuserData()
        elif choice=="7":
            break
        else:
            print("Invalid choice⚠️")



# =================================PRODUCT MENU==============================


def productmenu():
    while True:
        print("\n---------WELCOME TO PRODUCT COLLECTION----------")

        print("1. Add Product")
        print("2. Get All Product")
        print("3. Get Specific Product")
        print("4. Update product")
        print("5. Delete product")
        print("6. Exit")

        choice=input("Enter your choice:")

        if choice=="1":
            add_product()
        elif choice=="2":
            getallproductdata()
        elif choice=="3":
            getspecificproduct()
        elif choice=="4":
            updateproduct()
        elif choice=="5":
            deleteproductData()
        elif choice=="6":
            break
        else:
            print("Invalid choice⚠️")



# ===============================ORDER MENU===============================


def ordermenu():
    while True:
        print("\n--------WELCOME TO ORDER COLLECTION---------")

        print("1. Place Order")
        print("2. Get All Orders")
        print("3. Get Orders By User ID")
        print("4. Update Delivery Status")
        print("5. Exit")

        choice=input("Enter your choice:")

        if choice=="1":
            place_order()
        elif choice=="2":
            get_all_ordersdetails()
        elif choice=="3":
            getorderdetails_by_userid()
        elif choice=="4":
            update_delivery_status()
        elif choice=="5":
            break
        else:
            print("Invalid choice⚠️")
            


# ===========================MAIN MENU================================


while True:
    print("\n-----------WELCOME😊--------------")

    print("1. User Collection")
    print("2. Product Collection")
    print("3. Order Collection")
    print("4. Exit")

    choice=input("What do you want to do?")

    if choice=="1":
        usermenu()
    elif choice=="2":
        productmenu()
    elif choice=="3":
        ordermenu()
    elif choice=="4":
        print("Thank you🤗")
        break
    else:
        print("Invalid choice⚠️")
        