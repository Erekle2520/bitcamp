def main():

  Question=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")


  match Question:
      case "42" | "forty two" | "forty-two" :
          print("Yes")
      case _:
          print("No")
main()          
        
'''if Question=="42" or Question== "Forty Two" or Question=="forty-two":
    print("Yes")
else:
    print("No")

match Question:
    case "42":
        print("Yes")
    case "forty two":
        print("Yes")
    case "forty-two":
        print("yes")

    case _:
        print("No")
'''       
