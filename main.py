import femm
import matplotlib.pyplot as plt
import numpy as np
import os

def drawroundedcorner_box(femm, group, width, length, x_center, y_center, corner_radius, one_sided):
    x1 = x_center - width / 2
    y1 = y_center - length / 2
    x2 = x1 + width
    y2 = y1 + length

    # mc = .02 * inches

    mc = corner_radius
    # first create nodes at the 4 corners
    # because they will be joined by an arc segment

    c1_x = x1
    c1_y = y1

    c2_x = x2
    c2_y = y1

    c3_x = x2
    c3_y = y2

    c4_x = x1
    c4_y = y2

    # now make blunted edge magnet based on it
    n1x = c1_x
    n1y = c1_y + mc

    n2x = c1_x + mc
    n2y = c1_y

    n3x = c2_x - mc
    n3y = c2_y

    n4x = c2_x
    n4y = c2_y + mc

    n5x = c3_x
    n5y = c3_y - mc

    n6x = c3_x - mc
    n6y = c3_y

    n7x = c4_x + mc
    n7y = c4_y

    n8x = c4_x
    n8y = c4_y - mc

    # If drawing all 4 corners
    if (one_sided == 0):
        femm.mi_addnode(n1x, n1y)
        femm.mi_addnode(n2x, n2y)
        femm.mi_addnode(n3x, n3y)
        femm.mi_addnode(n4x, n4y)
        femm.mi_addnode(n5x, n5y)
        femm.mi_addnode(n6x, n6y)
        femm.mi_addnode(n7x, n7y)
        femm.mi_addnode(n8x, n8y)

        femm.mi_addarc(n1x, n1y, n2x, n2y, 90, 3)
        femm.mi_addsegment(n2x, n2y, n3x, n3y)

        femm.mi_addarc(n3x, n3y, n4x, n4y, 90, 3)
        femm.mi_addsegment(n4x, n4y, n5x, n5y)

        femm.mi_addarc(n5x, n5y, n6x, n6y, 90, 3)
        femm.mi_addsegment(n6x, n6y, n7x, n7y)
        femm.mi_addarc(n7x, n7y, n8x, n8y, 90, 3)
        femm.mi_addsegment(n8x, n8y, n1x, n1y)

        femm.mi_clearselected()
        # femm.mi_drawrectangle(x1, mag_y1, mag_x2, mag_y2)
        # femm.mi_selectrectangle(x1, mag_y1, mag_x2, mag_y2,0)

        femm.mi_selectsegment(c1_x, c1_y)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c1_x + width / 4, c1_y)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c2_x, c2_y)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c3_x, c3_y + length / 2)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c3_x, c3_y)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c3_x - width / 4, c3_y)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c4_x, c4_y)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c4_x, c4_y - length / 2)
        femm.mi_setgroup(group)

        #femm.mi_clearselected()

    # if drawing only rounded corners on far side
    # because location is on axis.
    if (one_sided == 1):

        femm.mi_addnode(c1_x, c1_y)
        femm.mi_addnode(n3x, n3y)
        femm.mi_addnode(n4x, n4y)
        femm.mi_addnode(n5x, n5y)
        femm.mi_addnode(n6x, n6y)
        femm.mi_addnode(c4_x, c4_y)

        femm.mi_addsegment(c4_x, c4_y, c1_x, c1_y)

        femm.mi_addsegment(c1_x, c1_y, n3x, n3y)

        femm.mi_addarc(n3x, n3y, n4x, n4y, 90, 3)
        femm.mi_addsegment(n4x, n4y, n5x, n5y)

        femm.mi_addarc(n5x, n5y, n6x, n6y, 90, 3)
        femm.mi_addsegment(n6x, n6y, c4_x, c4_y)

        femm.mi_clearselected()
        femm.mi_selectsegment(c1_x, c1_y + length / 2)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c1_x + width / 2, c1_y)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c2_x, c2_y)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c2_x, c2_y + length / 2)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c3_x, c3_y)
        femm.mi_setgroup(group)
        femm.mi_selectsegment(c3_x - width / 2, c3_y)
        femm.mi_setgroup(group)

        #femm.mi_clearselected()


femm.openfemm(0)
femm.opendocument("setup.fem")   # Load a template that has all the required materials already
                                 # pre-loaded, i.e when calling 'femm.mi_setblockprop('NdFeB 52 MGOe'.."
                                 # This is how it knows where to get that property 'NdFeB 52 MGOe'
femm.mi_saveas("temporary.fem")       # this changes the working file so that 'template.fem' is always whats in use


# This is Wire Gauge Data from MWS industries
# it may not line up exactly with the magnet wire in FEMM
# so it is good to be aware of this
# its 14 to 32 AWG
AWG_list=np.linspace(14,32,32-14+1).tolist()
OD_list=[ 0.06695,0.05975,0.0534,0.0478,0.04275,0.0382,0.03425,0.0306,0.02735,0.0246,0.02205,
    0.0197,0.01765,0.0159,0.01425,0.0128,0.01145,0.0103,0.00935]

### DEFINE THE COIL
inches=1.0                                  # Define units
AWG_coil=22
od_wire=OD_list[AWG_list.index(AWG_coil)]   # find the AWG

N_layers=6                                  # Number of stacked layers of wire
id_coil=1*inches                            # inner coil diameter
Lc=0.77*inches                              # Length of the Coil
N_turns=round(Lc/od_wire)                   # Define lengthwise turns
current=-6                                  # Define the amount of current in the coil
femm.mi_addcircprop('icoil', current, 1)    # Add it to the FEMM model

od_coil=id_coil+2*N_layers*od_wire          # outer coil diameter

coil_group_number=5                         # Define coil number different as magnet
# Call this function to draw a box with rounded corners
# I find this introduces less errors
coil_center_x=id_coil/2+(od_coil-id_coil)/4
coil_center_y=0
drawroundedcorner_box(femm,coil_group_number,(od_coil-id_coil)/2,Lc,coil_center_x,coil_center_y,od_wire,0)
# With segments now drawn, label it
femm.mi_addblocklabel(coil_center_x,coil_center_y)                        # Create a label within the coil segments
femm.mi_selectlabel(coil_center_x,coil_center_y)                          # Select that label
femm.mi_setblockprop('22 AWG', 0, 1, 'icoil', 0, 0, N_layers*N_turns)   # Apply properties to the label
femm.mi_clearselected()

### DEFINE AIR REGION

air_x=od_coil/2+id_coil/4
air_y=0
femm.mi_addblocklabel(air_x,air_y)
femm.mi_selectlabel(air_x,air_y)
femm.mi_setblockprop('Air', 0, 1, '<none>', 0, 0, 0)
femm.mi_clearselected()

# DEFINE THE PERMANENT MAGNET
Lm = 0.6 * inches              # Magnet length
od_m = 0.5 * inches             # Magnet Diameter(assumes cylindrical magnet)
mag_y_loc_o=Lc/2+2*Lc           # Initial position of the magnet
mag_y_loc=mag_y_loc_o           # current position of the magnet (can change)

magnet_corner_radius=.01*inches # Approximate,
mag_label_x = od_m / 4          # x location for magnet property node
mag_label_y = mag_y_loc         # y location for magnet property node
one_sided_magnet_flag=1      # the magnet is on axis, so only needs rounded corners on one side

drawroundedcorner_box(femm,3,od_m/2,Lm,mag_label_x,mag_label_y,magnet_corner_radius,one_sided_magnet_flag)

femm.mi_addblocklabel(mag_label_x, mag_label_y)
femm.mi_selectlabel(mag_label_x, mag_label_y)
femm.mi_setblockprop('NdFeB 52 MGOe', 0, 1, '<none>', 90, 0, 0)
femm.mi_setgroup(3) # seems i needed this as well.. # MAJOR ADDITION
femm.mi_selectlabel(mag_label_x, mag_label_y)
femm.mi_setgroup(3)
femm.mi_clearselected()


# DEFINE ABSORBING BOUNDARY CONDITIONS
# THIS IS LIKELY A SOURCE OF ERROR IF YOU CHANGE THE COIL AND MAGNET SIZES
sim_diameter=mag_y_loc_o+Lm/2+Lc/2+Lc
y_center_of_ABC=sim_diameter/4-Lm/2
x_center_of_ABC=0
femm.mi_makeABC(7, sim_diameter/2*1.2, x_center_of_ABC, y_center_of_ABC, 0)



##  RUNN 1
z_start=mag_y_loc_o
z_end=0
num_points=25                       # resolution of points inbetween z_start and z_end
dz=(z_end-z_start)/(num_points-1)
z=np.linspace(z_start,z_end,num_points)
fz=[]




# START OF MOTION
counter=0 # Initialize a counter because I was too lazy to get the index in the for loop
for z_loc in z:
    mag_y_loc=z_loc
    # Only start after the initial position has been used.
    if (counter>0):
        femm.mi_movetranslate(0, dz)

    femm.mi_analyze(0)
    femm.mi_loadsolution()
    femm.mi_selectgroup(3)
    femm.mo_selectblock(0,mag_y_loc)
    fz.append(femm.mo_blockintegral(21)*2)

    counter=counter+1
# END OF MOTION



# POST-PROCESSING
femm.mi_saveas("final.fem")        # Save the final simulation step
max_loc=fz.index(max(fz))          # Find the location of maximum force


plt.figure(1)
plt.plot(z-z[max_loc],fz)
plt.show()
plt.xlabel('z (in)')
plt.ylabel('F [N]')

# Save plot data to text file
os.mkdir('output_data')
out_file=open('output_data/femm_N_vs_mm_'+str(int(100*Lm))+'_'+str(int(100*od_m))+'.txt','w+')

counter=0
for z_loc in z:

    out_file.write("%f \t %f \n" %(25.4*(z[counter]-z[max_loc]), fz[counter]))
    counter=counter+1

print("Force data saved to:\t"+out_file.name)
out_file.close()


