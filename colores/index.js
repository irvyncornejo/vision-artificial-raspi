const path = require('path')
const getColors = require('get-image-colors')

const main = async () =>{
  try{
    const ruta  = process.argv.slice(2)[0]
    const image = path.join(__dirname, ruta)
    const colores_imagenes = {}
    await getColors(image).then(colors => {
      // `colors` is an array of color objects
      const colores = ['Cyan', 'Magenta', 'Amarillo', 'Negro']
      colors.forEach(color=>{
        const definicionColor = {}
        color.cmyk().forEach((cmyk, index) => definicionColor[`${colores[index]}`]= cmyk > 0 ? Math.ceil(cmyk*100, -2) : cmyk)
        const hex = color.hex().replace('#', '')
        colores_imagenes[`${hex}`] = {
          'rgb': color.rgb(),
          'cmyk': definicionColor
        }
      })
    })
    console.log(JSON.stringify(colores_imagenes))
  }catch(e){
    console.log(e)
  }
}


main()