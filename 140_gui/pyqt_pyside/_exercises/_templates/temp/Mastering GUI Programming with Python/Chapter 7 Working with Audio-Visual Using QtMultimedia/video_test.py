____ ?.QtCore ______ *
____ ?.QtMultimedia ______ *

app _ QCoreApplication([])

for camera_info in QCameraInfo.availableCameras
    print('Camera: ', camera_info.deviceName())
    camera _ QCamera(camera_info)
    r _ QMediaRecorder(camera)
    print('\tAudio Codecs: ', r.supportedAudioCodecs())
    print('\tVideo Codecs: ', r.supportedVideoCodecs())
    print('\tAudio Sample Rates: ', r.supportedAudioSampleRates())
    print('\tFrame Rates: ', r.supportedFrameRates())
    print('\tResolutions: ', r.supportedResolutions())
    print('\tContainers: ', r.supportedContainers())
    print('\n\n')
