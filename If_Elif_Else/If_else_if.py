#Check if all employee names start with a capital letter.
import re

emp_details =[{"name":"pari"},
              {"name":"Hari"},
              {"name":"Kari"},
              {"name":"Aari"},
              {"name":"Sari"},
              {"name":"wari"},
              {"name":"fari"}]

for record in emp_details:
    emp_name = record["name"]

    if emp_name.istitle():
        print(f"the {emp_name} is in correct formate have 1st charater capital")
    else:
        print(f"the {emp_name} is incorrect formate ")

#Validate phone numbers: Must be 10 digits and only numeric.

emp_details =[{"name":"pari","phone_num":9999888877},
              {"name":"Hari","phone_num":88769065433},
              {"name":"Kari","phone_num":1123778766789},
              {"name":"Aari","phone_num":8876659986},
              {"name":"Sari","phone_num":887332445},
              {"name":"wari","phone_num":8837487561},
              {"name":"fari","phone_num":2287768976}]


for record in emp_details:
    emp_name = record["name"]
    emp_pho_num = record["phone_num"]

    phone_str=str(emp_pho_num)

    if phone_str.isnumeric() and len(phone_str) == 10:
        print(f"The {emp_pho_num} is Valid phone number")
    else:
        print(f"The {emp_pho_num} is Invalid phone number")


emp_details =[{"name":"pari","phone_num":9999888877,"email":"p@gmail.com"},
              {"name":"Hari","phone_num":88769065433,"email":"Harigmail.com"},
              {"name":"Kari","phone_num":1123778766789,"email":"Kari@gmail.com"},
              {"name":"Aari","phone_num":8876659986,"email":"Aari@gmail.com"},
              {"name":"Sari","phone_num":887332445,"email":"Sari%gmail.com"},
              {"name":"wari","phone_num":8837487561,"email":"wari@gmail,com"},
              {"name":"fari","phone_num":2287768976,"email":"fari@gmail.com"}]

for record in emp_details:
    emp_email = record["email"]

    if "@" in emp_email and "." in emp_email:
        print(f"The {emp_email} has '@' and '.' its valid email ID")
    else:
        print(f"The {emp_email} doesnt have '@' or  '.' its valid email ID")

prod_price= [{"Prod_name":"table","Prod_price":20000},
             {"Prod_name":"chair","Prod_price":2000},
             {"Prod_name":"phone","Prod_price":9999},
             {"Prod_name":"toy","Prod_price":200},
             {"Prod_name":"necklace","Prod_price":500}
             ]

for record in prod_price:
    price = record["Prod_price"]
    product = record ["Prod_name"]
    if price > 0 and price < 10000:
        print(f"the {product} 's {price} is within range")
    else:
        print(f"the {product} 's {price} is out of  range")

emp_details =[{"name":"pari","Gender":"F"},
              {"name":"Hari","Gender":"M"},
              {"name":"Kari","Gender":"M"},
              {"name":"Aari","Gender":"F"},
              {"name":"Sari","Gender":"F"},
              {"name":"wari","Gender":"F"},
              {"name":"fari","Gender":"F"}]

for record in emp_details:
    emp_gen = record ["Gender"]

    if emp_gen == "M" or emp_gen == "F":
        print("Valid Gender")
    else:
        print("Invalid Gender")

item_price= [{"Prod_name":"table","Prod_price":20000,"discount":"20"},
             {"Prod_name":"chair","Prod_price":2000,"discount":"10"},
             {"Prod_name":"phone","Prod_price":9999,"discount":"50"},
             {"Prod_name":"toy","Prod_price":200,"discount":"80"},
             {"Prod_name":"necklace","Prod_price":500,"discount":"100"}
             ]

for record in item_price:
    item_disct= record["discount"]
    item_disct_int=int(item_disct)

    if item_disct_int <=50:
        print("Valid")
    else:
        print("invalid")
#In a list of invoice records, check if the total = quantity × unit_price. If not, flag.

invoice_details=[{"Prod_name":"table","Prod_price":20000,"unit":1,"total_Price":20000},
             {"Prod_name":"chair","Prod_price":2000,"unit":2,"total_Price":4000},
             {"Prod_name":"phone","Prod_price":10000,"unit":2,"total_Price":200000},
             {"Prod_name":"toy","Prod_price":200,"unit":5,"total_Price":1000},
             {"Prod_name":"necklace","Prod_price":500,"unit":3,"total_Price":1500}
             ]

for record in invoice_details:
    total_amount= record ["total_Price"]
    product_price= record ["Prod_price"]
    unit_num = record ["unit"]


    total_amount_int = int(total_amount)
    product_price_int = int(product_price)
    unit_num_int = int(unit_num)

    if total_amount_int == (product_price_int * unit_num_int):
        print("The total price is correct")
    else:
        print("The total Price is incorrect")


#Check if date_of_joining is before date_of_exit. If not, mark invalid.


from datetime import datetime

emp_details =[{"name":"pari","DOJ":"2024-12-22","DOE":"2022-02-19"},
              {"name":"Hari","DOJ":"2019-02-22","DOE":"2022-10-10"},
              {"name":"Kari","DOJ":"2022-10-03","DOE":"2016-10-10"},
              {"name":"Aari","DOJ":"2010-04-22","DOE":"2022-05-09"},
              {"name":"Sari","DOJ":"2021-11-20","DOE":"2022-12-28"},
              {"name":"wari","DOJ":"2000-12-29","DOE":"2000-01-17"},
              {"name":"fari","DOJ":"1999-12-15","DOE":"1996-12-28"}]

for record in emp_details:
    date_of_joining= record["DOJ"]
    date_of_exit = record["DOE"]
    emp_name= record["name"]

    #date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    DOJ_obj = datetime.strptime(date_of_joining, "%Y-%m-%d")
    DOE_obj = datetime.strptime(date_of_exit, "%Y-%m-%d")



    if DOJ_obj < DOE_obj:
        print(f"The {emp_name} has valid details of DOJ and DOE")
    else:
        print(f"The {emp_name} has Invalid details of DOJ and DOE, Please check")

#Check if PAN number is 10 characters and follows format: 5 letters, 4 digits, 1 letter.

emp_details =[{"name":"pari","PAN":"PARIN9999N"},
              {"name":"Hari","PAN":"HARIN7766N"},
              {"name":"Kari","PAN":"KARIN1425N"},
              {"name":"Aari","PAN":"AarIN1237N"},
              {"name":"Sari","PAN":"SARIN566N"},
              {"name":"wari","PAN":"WARIN6644"},
              {"name":"fari","PAN":"FARI2289f"}]

for record in emp_details:
    pan_no = record["PAN"]

    if re.fullmatch(r"^[A-Z]{5}[0-9]{4}[A-Z]$", pan_no):
        print(f"{pan_no} is a valid PAN")
    else:
        print(f"{pan_no} is NOT a valid PAN")
    #
    # if len(pan_no) == 10:
    #    print(f"the lenght of PAN number {pan_no} is 10")
    # else:
    #    print(f"invalid pan number {pan_no}")
    #
    # if pan_no[0:5].isalpha()    and pan_no[0:5].isupper():
    #     print(f"First 5 characters of {pan_no}  are all letters and are in upper")
    # else:
    #     print(f"First 5 characters of {pan_no}  are not letters and are not in upper")
    #
    # if pan_no[5:9].isdigit():
    #     print(f" next 4 characters of {pan_no}  are all digits")
    # else:
    #     print(f" next 4 characters of {pan_no}  are not digits")
    #
    # if pan_no[9].isalpha() and pan_no[9].upper():
    #     print("The last charater is alphabet and in upper case")
    # else:
    #     print("The last charater is not alphabet and in upper case")

    # if len(pan_no) == 10:
    #     print(f"the lenght of PAN number {pan_no} is 10")
    # elif pan_no[0:5].isalpha() and pan_no[0:5].isupper():
    #     print(f"First 5 characters of {pan_no}  are all letters and are in upper")
    # elif pan_no[5:9].isdigit():
    #     print(f" next 4 characters of {pan_no}  are all digits")
    # elif pan_no[9:].isalpha() and pan_no[9:].upper():
    #     print(f"All pass → PAN {pan_no} are valid")
    # else:
    #     print("Invalid PAN")
    #
    #
    #| Part       | Meaning                                    |
# | ---------- | ------------------------------------------ |
# | `^`        | Start of string                            |
# | `[A-Z]{5}` | First 5 characters must be capital letters |
# | `[0-9]{4}` | Next 4 characters must be digits           |
# | `[A-Z]`    | Last character must be a capital letter    |
# | `$`        | End of string                              |


# | Pattern         | Meaning                          | Example Match                                   |       |                          |
# | --------------- | -------------------------------- | ----------------------------------------------- | ----- | ------------------------ |
# | `.`             | Any character except newline     | `a.c` → `abc`, `axc`                            |       |                          |
# | `^`             | Start of string                  | `^abc` → matches “abc” only if at the beginning |       |                          |
# | `$`             | End of string                    | `xyz$` → matches “xyz” at the end               |       |                          |
# | `[abc]`         | a or b or c                      | `b` in `[abc]`                                  |       |                          |
# | `[a-z]`         | any lowercase letter             | `m`, `k`, `z`                                   |       |                          |
# | `[A-Z]`         | any uppercase letter             | `D`, `H`                                        |       |                          |
# | `[0-9]` or `\d` | any digit (0–9)                  | `7`, `3`                                        |       |                          |
# | `\w`            | Word char (letter, digit, \_)    | `abc_123`                                       |       |                          |
# | `\s`            | Whitespace (space, tab, newline) | `' '`                                           |       |                          |
# | `+`             | One or more                      | `a+` → `a`, `aaaa`                              |       |                          |
# | `*`             | Zero or more                     | `ba*` → `b`, `baaa`                             |       |                          |
# | `?`             | Zero or one                      | `ab?` → `a`, `ab`                               |       |                          |
# | `{n}`           | Exactly n times                  | `\d{4}` → `2023`                                |       |                          |
# | `{n,m}`         | Between n and m times            | `\d{2,4}` → 2–4 digits                          |       |                          |
# | \`              | \`                               | OR                                              | \`cat | dog`matches`cat`or`dog\` |
# | `()`            | Grouping                         | `(\d{4})-(\d{2})`                               |       |                          |
#
