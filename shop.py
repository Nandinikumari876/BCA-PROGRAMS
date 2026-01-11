import random
for i in range(100):
    x=random.randrange(000,999)
    print(" ✨✨✨welcome to our store ✨✨✨")
    print(''' prices:  
          💄 lipstick = 140
          💎 primer = 120
         🎨 concealer =130''')
    name=input(" enter your name : ")
    print(" welcome  ",name)
    user_contact=eval(input(" enter your contact number"))
    if user_contact==9084414:
        print(" your OTP : ",x)
        user_otp=eval(input(" enter your otp"))
        if user_otp==x:
            print(" verified successfully ✅✅")
            print(" enter quantity of products one by one and if yoy dont want any product then you press 0")
            lipstick_quantity=eval(input(" lipstick quantity : "))
            primer_quantity=eval(input(" primer quantity : "))
            concealer_quantity=eval(input(" concealer quantity : "))
            total_quantity=lipstick_quantity+primer_quantity+concealer_quantity
            lipstick = 140
            primer = 120
            concealer =130
            lipstick_bill=lipstick*lipstick_quantity
            primer_bill=primer*primer_quantity
            concealer_bill=concealer*concealer_quantity
            total_bill=lipstick_bill+primer_bill+concealer_bill
            print(" YOUR TOTAL BILL : ",total_bill)
            
            print(" .......🤩🤩🤩THANKYOU FOR SHOPPING🤩🤩🤩.....")
        else:
            print(" invalid OTP ")
    else:

        print(" invalid contact number ")
