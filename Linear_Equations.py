# Two Simultaneous Linear Equations solved by using matrices 
def Linear_Equation(InputX: int, InputB: int):
   x = InputX
   b = InputB 

   n = [i for i in reversed(x)]
   n[2] = (-([i for i in reversed(x)][1]))
   n[1] = (-([i for i in reversed(x)][2]))

   X = (n[0]*b[0] + n[1]*b[1]) / (x[0]*x[3] - x[2]*x[1])
   Y = (n[2]*b[0] + n[3]*b[1]) / (x[0]*x[3] - x[2]*x[1])
   C = InputX[0]*X + InputX[1]*Y
   F = InputX[2]*X + InputX[3]*Y

   return InputB[0], InputB[1], X, Y, C, F

def response(n):
   if (n[0] == n[4]): return n[2], n[3]
   if (n[1] == n[5]): return n[2], n[3]
   else: return 'false'

def Solver(a:int, b:int, d:int, e:int, c:int, f:int):
   n = Linear_Equation([a, b, d, e], [c, f])
   Response = response(n)
   
   if len(Response) == 2: 
      result = f'x = {Response[0]}, y = {Response[1]}'
   else: 
      result = f'{Response}'
   print(result)

Solver(3, 4, 2, -1, 19, 9)
