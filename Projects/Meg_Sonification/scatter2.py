#!/usr/bin/python
 
import numpy
from struct import pack
from math import sin, pi
import Image
import sys

data_file = numpy.asarray(Image.open(sys.argv[1]).convert('L'))

a = numpy.amin(data_file)
b = numpy.amax(data_file)
data_file = (data_file-a) * 1.0/b
data_file = numpy.matrix.transpose(data_file)

scaling_min = 1050.0
scaling_max = 2000.0
scaling_span = scaling_max-scaling_min


print( "Loading data..." )


freq_min = 1002.0
freq_max = 3002.0

duration_s = 8
duration_ms = duration_s*1000
duration_segments = duration_ms*8





#data = numpy.loadtxt( data_dir+data_file )

data = data_file
#data = data[:,100:200]

num_lines = len(data) #number of rows
print(num_lines)
num_freq_bins = len(data[0]) #number of columns
print(num_freq_bins)
stream_scaling_factor = duration_segments*1.0/num_lines #1 segment is 1/8 ms

time_stream = []
freq_factors = [ 2.0*pi*freq/8000.0 for freq in numpy.linspace(freq_min, freq_max,num_freq_bins) ]
freq_factors = numpy.array(freq_factors)

min_intensity = -0.00001
max_intensity = +0.00001
for seg in range(duration_segments):
    data_index = int( seg/stream_scaling_factor ) #what row are we currently looking at
    percentage = seg*100.0/(duration_segments)
    #if seg%100==0:
        #print( "Segment %d of %d (%.1f %%)..." % (seg, duration_segments, percentage) )
    
    #sin_seg = sin(seg*freq_factors[-150])
    data_line = data[data_index]
    #data_line = data[data_index,::-1]
    #data_line = numpy.sqrt( data[data_index] )
    
    intensities = numpy.sin(seg*freq_factors*( data_line ) ) #I understand this line except for the multiplication by seg --Joel
    intensity = numpy.sum( intensities )
    
    min_intensity = min(min_intensity,intensity)
    max_intensity = max(max_intensity,intensity)
    
    time_stream.append( intensity )
    
    

# Rescaling
wave_scaling = 1.0/max( abs(max_intensity), abs(min_intensity) )
for i, seg in enumerate( range(duration_segments) ):
    
    time_stream[i] = wave_scaling*time_stream[i]

def au_file_stream(stream, filename='test.au', vol_adjust=1.0):
    """
    creates an AU format audio file of a sine wave
    """
    
    size = len(stream)
    
    fout = open(filename, 'wb')
    # header needs size, encoding=2, sampling_rate=8000, channel=1
    fout.write('.snd' + pack('>5L', 24, size, 2, 8000, 2))
    
    # write data
    for seg in range(size):
        # sine wave calculations
        sin_seg = stream[seg]
        fout.write(pack('b', vol_adjust * 127 * sin_seg))
    fout.close()


au_file_stream( time_stream )

# create a soundfile in AU format playing a sine wave
# of a given frequency, duration and volume
# tested with Python25   by vegaseat     29jan2008


def au_file_single_freq(name='test.au', freq=440, dur=1000, vol=0.5):
    """
    creates an AU format audio file of a sine wave
    of frequency freq (Hz)
    for duration dur (milliseconds)
    at volume vol (max is 1.0)
    """
    fout = open(name, 'wb')
    # header needs size, encoding=2, sampling_rate=8000, channel=1
    fout.write('.snd' + pack('>5L', 24, 8*dur, 2, 8000, 1))
    factor = 2 * pi * freq/8000
    # write data
    for seg in range(8 * dur):
        # sine wave calculations
        sin_seg = sin(seg * factor)
        fout.write(pack('b', vol * 127 * sin_seg))
    fout.close()

def au_file_two_freq(name='test.au', freq1=440, freq2=800, dur=1000, vol=0.5):
    """
    creates an AU format audio file of a sine wave
    of frequency freq (Hz)
    for duration dur (milliseconds)
    at volume vol (max is 1.0)
    """
    fout = open(name, 'wb')
    # header needs size, encoding=2, sampling_rate=8000, channel=1
    fout.write('.snd' + pack('>5L', 24, 8*dur, 2, 8000, 1))
    factor1 = 2 * pi * freq1/8000
    factor2 = 2 * pi * freq2/8000
    # write data
    for seg in range(8 * dur):
        # sine wave calculations
        sin_seg = 0.5*sin(seg * factor1) + 0.5*sin(seg * factor2)
        fout.write(pack('b', vol * 127 * sin_seg))
    fout.close()

# test the module ...
if __name__ == '__main__':
    #au_file_two_freq(name='sound800.au', freq1=210, freq2=10, dur=2000, vol=0.8)
    au_file_single_freq(name='sound800.au', freq=101.0, dur=2000, vol=0.8)
    
