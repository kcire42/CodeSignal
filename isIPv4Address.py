# An IP address is a numerical label assigned to each device 
# (e.g., computer, printer) participating in a computer 
# network that uses the Internet Protocol for communication. 
# There are two versions of the Internet protocol, and thus 
# two versions of addresses. One of them is the IPv4 address.

# Given a string, find out if it satisfies the 
# IPv4 address naming rules.



def isIPAddress(inputString):
    ip = inputString.split(".")
    #print(ip)
    if len(ip) == 4:
        for element in ip:
            try:
                if len(element) >= 2 and element[0] == '0':
                    return False
                else:
                    if int(element) <= 255 and int(element) >= 0:
                        
                        print(element)
                        continue
                    else:
                        return False
            except:
                return False
        return True 
    else:
        return False




def testing(input,output):
    if input == output:
        print("Test Pass")
    else:
        print("Test Fail")
    print(f"Input: {input}, Output: {output}")

if __name__ == "__main__":
    testing(isIPAddress("172.16.254.1"),True)
    testing(isIPAddress("172.16.254"),False)
    testing(isIPAddress("256.16.254.1"),False)
    testing(isIPAddress(".16.254.1"),False)
    testing(isIPAddress("64.233.161.00"),False)
    testing(isIPAddress("01.233.161.23"),False)
    # 172.16.254.1
    # 172.16.254
    # 256.16.254.1
    # 64.233.161.00
    # 01.233.161.23
    # 106.23.56.0
    # 106.00.23.0
    # 1.45.23.12