def program():
    file_name = input("Write SOMETHING special in file which is named ")
    print("------------------------------")

    def wri_file() :
        try:
            
            ## To read file
            domainss = open(file_name,"r")
            print(domainss.read())
            for dom in domainss.readlines():
                print(dom)
            domainss.close()
            print("------------------------------")

            ## To Write Files
            domain_file = open(file_name,"a")
            number = int(input("No. oF lines You Want To write ==> "))
            for domain in range(0,number):
                a = input("enter your term ==>")
                domain_file.write(a +"\n")

            domain_file.close()
            print("------------------------------")


            domainss = open(file_name,"r")
            print(domainss.read())
            for dom in domainss.readlines():
                print(dom)
            domainss.close()
            print("------------------------------")
            wri_file()

        except:
            print("file Not Found")
            program()
            
    wri_file()

program()
