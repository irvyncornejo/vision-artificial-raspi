const video = document.getElementById('video')
const sizeVideo = { width:720, height:560 }

const startVideo = () => {
  navigator.mediaDevices.getUserMedia(
      { 
        audio: false,
        video:  sizeVideo
      }
  )
    .then(stream => video.srcObject = stream)
    .catch(error => console.error(error))
}

const main = () => {
  Promise.all([
    faceapi.nets.tinyFaceDetector.loadFromUri("static/js/models"),
    faceapi.nets.faceLandmark68Net.loadFromUri("static/js/models"),
    faceapi.nets.faceRecognitionNet.loadFromUri("static/js/models"),
    faceapi.nets.faceExpressionNet.loadFromUri("static/js/models"),
  ])
    .then(startVideo)
    .catch(error => console.error(error))
}

const videoDetectionHandler = () => {
  const canvas = faceapi.createCanvasFromMedia(video)
  const videoContainer = document.getElementById('videoContainer')
  videoContainer.appendChild(canvas)
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
}

main()