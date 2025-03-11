value = input("Enter a value: ")

try:
    int_value = int(value)
    print(f"The value '{value}' is of type: Integer")
except ValueError:
    try:
  
        float_value = float(value)
        print(f"The value '{value}' is of type: Float")
    except ValueError:
      
        print(f"The value '{value}' is of type: String")
print("samiya,23")
