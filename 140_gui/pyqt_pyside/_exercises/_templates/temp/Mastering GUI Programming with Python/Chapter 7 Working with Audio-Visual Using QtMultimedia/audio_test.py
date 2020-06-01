____ ?.?C.. ______ *
____ ?.QtMultimedia ______ *

app _ QCoreApplication([])

r _ QAudioRecorder()

print('Inputs: ', r.audioInputs())
print('Codecs: ', r.supportedAudioCodecs())
print('Sample Rates: ', r.supportedAudioSampleRates())
print('Containers: ', r.supportedContainers())
