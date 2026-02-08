#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Enter the temperature in Fahrenheit:  ")
  tmp = float(tempF)

  tempC =   (((tmp -32) * 5) / 9)

  print(tempF, "is ", f"{tempC:.1f}", "degrees celsius.")
if __name__ == '__main__':
  main()
