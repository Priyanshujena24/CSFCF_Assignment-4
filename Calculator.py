number1=int(input("Enter your first number:- "))
number2=int(input("Enter your Second number:- "))

print("Choose the Operation you want to perfome")

choice=int(input("\n 1.Add \n 2.Substract \n 3.Multiply \n 4.Divide \n 5.Exit \n"))

if choice==1:
    print(number1+number2)

elif choice==2:
    print(number1-number2)

elif choice==3:
    print(number1*number2)

elif choice==4:
    print(number1/number2)

elif choice == 5:
    print("Goodbye!")

else:
    print("Invalid option. Try again.")