export default async function(params, context) {
  context.preview({
    type:"image",
    data: params.inputImage
  })
  return { filePath: params.inputImage };
}
