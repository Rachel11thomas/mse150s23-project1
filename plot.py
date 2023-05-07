import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
data = np.loadtxt(raw_data   # Attempts to load filename into local variable data.
delimiter= ',', skiprows=2, dtype=float)
## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ python plot.py raw-data/Sp22_245L_sec-001_tensiletest-pekk_bulk.raw
# at the command line.


## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp22_245L_sec-001_tensiletest-pekk_bulk.raw
# Make sure to include axis labels and units!
# plt.plot(xdata, ydata, arguments-to-make-plot-pretty)
xdata=data[:,0]
ydata=data[:,1]
plt.plot(xdata,ydata)
plt.xlabel('strain')
plt.ylabel('stress (MPa)')

## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable
# Don't worry about deleting parts you might need later -- that's why we use git!


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)
x_linear= xdata[start:end]
y_linear=ydata[start:end]
fit=np.polyfit(x_linear,y_linear,1)
youngus_modulus=fit[0]
plt.plot(x_linear, y_linear)
plt.plot(x_linear, fit[0]*x_linear+fit[1])
plt.legend(['data','fit'])
print('Young's modulus=',youngus_modulus, MPa)

## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.
input_dir= 'raw_data/'
output_dir='output/'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
for filename in os.listdir(input_dir):
    data=np.loadtxt(input_dir+filename,delimiter(',', skiprows=2, dtype=float)
    xdata=data[:,0]
    ydata=data[:,1]
    plt.plot(xdata,ydata)
    start = ...
    end = ...
    xlinear=xdata[start:end]
    ylinear=ydata[start:end]
    fit=np.polyfit(x_linear,y_linear,1)
    youngus_modulus=fit[0]
    plt.legend(['data','linear fit'])
    plt.xlabel('strain')
    plt.ylabel('stress (MPa)')
    plt.title(stress-strain Curve:'+filename)
    output_file=output_dir+filename[:-4]+'.png'
    plt.savefig(output_file)
    print('young\'s modulus for',filename,'=',youngus_modulus, 'MPa'
    plt.clf()
    

