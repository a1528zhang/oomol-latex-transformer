from re import escape
from sympy import Integral, latex
from oocana import Context, TextPreviewPayload

def main(params: dict, context: Context):
  expression = params["expression"]
  latexString = latex(expression)

  context.preview(payload=TextPreviewPayload(
    type= "text",
    data= latexString,
  ))
  return { "latexString": latexString }