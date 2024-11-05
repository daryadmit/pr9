import re

def user_email(email):
    regular = r'^[a-zA-Z][\w.-]*@(.+)'
    m = re.match(regular, email)
    
    if m:
        name = email.split('@')[0]
        domen = m.group(1)
        return name, domen
    else:
        return None, None

def main():
    email = input("Введите email: ")
    n, d = user_email(email)
    
    if n and d:
        print(f"username: {n}")
        print(f"domain: {d}")
    else:
        print("Ошибка! Был введен неверный email.")

if __name__ == "__main__":
    main()