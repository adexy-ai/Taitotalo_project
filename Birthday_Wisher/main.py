import datetime as dt
import random
import smtplib


MY_GMAIL = "adex.dbaba@gmail.com"
MY_PASSWORD = "fhgvciamnejldnvo"

# 1. Update the birthdays.csv
with open('Birthday_Wisher/birthdays.csv', 'r') as file:
    data = file.readlines()

with open('Birthday_Wisher/quotes.txt', 'r') as file:
    quote = file.readlines()


    
# 2. Check if today matches a birthday in the birthdays.csv    
for item in data[1:]:
    item_ = item.strip().split(',')
    name = item_[0]
    email = item_[1]
    print(email)
    #print(name)
    item = '-'.join(item_)
    date_item = item[-5:]
    print(date_item)
    today = str(dt.datetime.now().date())
    today = today[-5:]
    print(today)
    #print(date_item == today)
    if today == date_item:
        print(f'Sending message to {name}')
        message = random.choice(quote).strip()
        

        
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv        
        file_path = f'Birthday_Wisher/letter_templates/letter_{random.randint(1,3)}.txt' 
        with open(file_path) as file:
            letter = file.read()
            #print(letter)
            if '[NAME]' in letter:
                #print('The [NAME] was found:','[NAME]' in letter)
                letter = letter.replace("[NAME]", name)
                #print(letter)
            
# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com") as conn:
    conn.starttls()
    conn.login(user=MY_GMAIL, password=MY_PASSWORD )
    conn.sendmail(
        from_addr=MY_GMAIL, 
        to_addrs=email, 
        msg=f"Subject:Happy Birthday\n\n{letter}")









