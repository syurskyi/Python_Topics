____ ?.?C.. ______ *
____ ?.?M.. ______ *

app _ QCoreApplication(  # list)

___ camera_info __ ?CI__.availableCameras
    print('Camera: ', camera_info.deviceName())
    camera _ QCamera(camera_info)
    r _ ?MR..(camera)
    print('\tAudio Codecs: ', r.supportedAudioCodecs())
    print('\tVideo Codecs: ', r.supportedVideoCodecs())
    print('\tAudio Sample Rates: ', r.supportedAudioSampleRates())
    print('\tFrame Rates: ', r.supportedFrameRates())
    print('\tResolutions: ', r.supportedResolutions())
    print('\tContainers: ', r.supportedContainers())
    print('\n\n')
