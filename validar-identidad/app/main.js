const video = document.getElementById('video')

const startVideo = () => {
  navigator.mediaDevices.getUserMedia(
      { audio: false,
        video: {width:720, height:560} 
      })
    .then(stream => video.srcObject = stream)
    .catch(error => console.error(error))
}

const main = () => {
  Promise.all([
    faceapi.nets.tinyFaceDetector.loadFromUri('./models'),
    faceapi.nets.faceLandmark68Net.loadFromUri('./models'),
    faceapi.nets.faceRecognitionNet.loadFromUri('./models'),
    faceapi.nets.faceExpressionNet.loadFromUri('./models'),
  ])
    .then(startVideo)
    .catch(error => console.error(error))
}

video.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video)
  document.body.append(canvas)
  const displaySizeVideo = { width: video.width, height: video.height }
  faceapi.matchDimensions(canvas, displaySizeVideo)
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(
      video,
      new faceapi.TinyFaceDetectorOptions())
        .withFaceLandmarks()
        .withFaceExpressions()
      const resizedDetections = faceapi.resizeResults(detections, displaySizeVideo)
      canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
      faceapi.draw.drawDetections(canvas, resizedDetections)
  }, 200)
})

main()