import speedtest
import time


print("-"*90)
print(" "*40,"Speed Test"," "*40)
print("-"*90)
print()
      
def main():
    print('''wait for some seconds approx 90-95 sec from your life.
    It is not too much time
    but it will give to the accurate answer
    ''')
    print()
    
    
    st = speedtest.Speedtest()
    downl = st.download() /1024
    down = downl/1024
    print(f'DOWNLOAD Speed ==> {down} mbps')
    upl = st.upload() /1024
    up = upl/1024
    print(f'UPLOAD Speed ==> {up} mbps')
    servernames =[]   
    st.get_servers(servernames)
    print()

n = input("Want To Continue Again YES/NO ==> ")

if n == "YES" or n == "yes" or n == "Yes":
    print("YEAP WE GO AGAIN ")
    main()
else:
    print("NO Problem")

main()


