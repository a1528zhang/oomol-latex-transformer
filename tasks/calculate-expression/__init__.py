from oocana import Context
import numbers

from sympy import integrate, diff, symbols
from torch.autograd import variable

# transfer array params to symbols, and filter number
# sample: transfer ["x", 1, "2", "y"] to {"x": Symbol("x"), "y": Symbol("y")}
def filterSymbols(exprParams) -> dict[str, str]: 
  parmaAndSymbol: dict[str, str] = dict()

  variables = list()
  for v in exprParams:
    if isinstance(v, str) and not v.isnumeric():
      variables.append(v)


  # deduplicate
  variables = list(set(variables))

  for v in variables:
    s = symbols(v)
    parmaAndSymbol[v] = s

  return parmaAndSymbol

def main(params: dict, context: Context):
  expr = params["expression"]
  op = params["operation"]
  exprParams = params["params"]

  parmaAndSymbol: dict[str, str] = filterSymbols(exprParams)
  
  print("exprParams ", parmaAndSymbol)

  p = list()
  for v in exprParams:
    if isinstance(v, numbers.Number):
      p.append(v)
    elif isinstance(v, str) and v.isnumeric():
      if ("." in v):
         p.append(float(v))
      else :
         p.append(int(v))
    else :
      p.append(parmaAndSymbol[v])

  result= None
  match op:
    case "derivatives":
      result= diff(expr, *p)
    case "integral":
      result = integrate(expr, *p)
  
  return { "expression": result }