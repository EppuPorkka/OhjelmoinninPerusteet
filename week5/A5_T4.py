print("Program starting.")

def askDimension(PPrompt: str) -> float:
    value = float(input(f"Insert {PPrompt}: "))
    return value

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    Sum = PWidth * PHeight
    return Sum

width = askDimension("width")
height = askDimension("height")
Area = calcRectangleArea(width,height)
print("")
print(f"Area is {Area}²")
print("Program ending.")