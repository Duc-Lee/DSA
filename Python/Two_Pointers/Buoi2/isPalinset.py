def isPalinset(s) : 
    left  = 0 
    right = len(s) -1 
    while (left < right ) : 
        # kiem tra phan tu dau tien neu la chu or so
        # tang bien left len neu khong phai 
        # neu no la ki tu dac biet
        if not s[left].isalnum() : 
            left += 1
        # tiep tuc kiem tra ca phan tu ben right
        # neu no la ki tu dac biet thi giam right 
        elif not s[right].isalnum() : 
            right -= 1
        # kiem tra xem 2 phan bang nhau khong
        # xem co doi xung khong 
        elif s[left].lower() == s[right].lower() :
            left += 1
            right -= 1
        # neu tat ca cac truong hop deu khong xay ra
        # tuc la mang bat doi xung
        else : 
            return False
    return True


if __name__ == "__main__" :
    print(isPalinset("A man, a plan, a canal: Panama")) 
    print(isPalinset("race a car")) 
    print(isPalinset("abdce sae")) 