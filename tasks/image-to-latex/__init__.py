from oocana import Context, TextPreviewPayload

from pix2text import Pix2Text, set_logger

def main(params: dict, context: Context):
  p2t = Pix2Text.from_config()
  outs = p2t.recognize_formula(params["input"])

  context.preview(payload=TextPreviewPayload(
    type= "text",
    data= outs,
  ))
  return { "latexString": outs }