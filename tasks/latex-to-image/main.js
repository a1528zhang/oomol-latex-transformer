import { mathjax } from "mathjax-full/js/mathjax.js";
import { TeX } from "mathjax-full/js/input/tex.js";
import { SVG } from "mathjax-full/js/output/svg.js";
import { liteAdaptor } from "mathjax-full/js/adaptors/liteAdaptor.js";
import { RegisterHTMLHandler } from "mathjax-full/js/handlers/html.js";

export default async function(params, context) {
  const adaptor = liteAdaptor();
  RegisterHTMLHandler(adaptor);

  const tex = new TeX({
    packages: ["base", "ams", "mathtools"],
  });
  const svg = new SVG({ fontCache: "none" });
  const html = mathjax.document("", { InputJax: tex, OutputJax: svg });
  
  const tex2svg = (tex) => {
    const node = html.convert(tex);
    return adaptor.innerHTML(node).replaceAll("currentColor", "black");
  };
  
  const svgStr = tex2svg(params.latex)
  
  context.preview({
    type: "html",
    data: svgStr
  })
  return {
    svgString: svgStr,
  };
}