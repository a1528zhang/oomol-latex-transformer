from oocana import Context, TextPreviewPayload

from sympy.parsing.latex import parse_latex

def main(params: dict, context: Context):
  latex = params["latexString"]
  expr = parse_latex(latex)

  if expr is None:
    return None
  
  exprStr= str(expr)
  context.preview(payload=TextPreviewPayload(
    type= "text",
    data= exprStr,
  ))
  return { "expression": expr }