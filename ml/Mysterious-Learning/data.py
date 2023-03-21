#!/user/bin/env python3
import h5py


# Read in the data file
f = h5py.File("alien.h5", 'r')

#find the strutcture of the data
for h1 in f.keys():
    print('*',h1)
    for h2 in f.require_group(h1).keys():
        print("|__",h2)
        # for h3 in f[h1+'/'+h2].keys():
        #     path = h1 + '/' + h2 + '/' + h3
        #     print(path+':\t',f[path].values)


data = f['model_weights']
data.dtype