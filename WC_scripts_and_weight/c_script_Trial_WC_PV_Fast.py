#!/usr/bin/python
#
# The following script replicates the results of Horwitz, Warner et al (2005), Figure 3.
#
# There are 6 trials total: 3 DMS trials and 3 control trials
#
# Total number of timesteps is 6600 = 33 seconds
#
# The number of timesteps in each trial is 1100 = 5.5 seconds
#
# The DMS trials are MATCH, MISMATCH, MATCH. The attention parameter in DMS trials is 0.3
# The control trials are 'passive viewing': random shapes are presented and low attention (0.05)
# is used. Passive viewing trials are also organized as MATCH, MISMATCH, MATCH.
#
# The first 200 timesteps = 1000 ms we do nothing. We assume 1 timestep = 5 ms, as in Horwitz
# et al (2005)
#
# To maintain consistency with Husain et al (2004) and Tagamets and Horwitz (1998),
# we are assuming that each simulation timestep is equivalent to 5 milliseconds
# of real time. 
                
# now we present S1 by manually inserting it into the MGN module and leaving S1 there
# for 200 timesteps (1 second).

# define the simulation time in total number of timesteps
# Each timestep is roughly equivalent to 5ms
LSNM_simulation_time = 5000
                
# Define list of parameters the the script is going to need to modify the LSNM neural network
# They are organized in the following order:
# [lo_att_level, hi_att_level, lo_inp_level, hi_inp_level, att_step, ri1, ri2]
script_params = [0.05, 0.7, 0.05, .675, 0.02, [], []]
# try to drop attenion


# the following is random shape1, this shape has the same luminance as an 'O'
rand_shape1 = rdm.sample(range(81),18)
rand_indeces1 = np.unravel_index(rand_shape1,(9,9))
script_params[5] = zip(*rand_indeces1)

# A second random shape in inserted for a mismatch
rand_shape2 = rdm.sample(range(81),18)
rand_indeces2 = np.unravel_index(rand_shape2,(9,9))
script_params[6] = zip(*rand_indeces2)
        
def o_shape(modules, script_params):
    
    """
    generates an o-shaped visual input to neural network with parameters given
    Good intensity is about .69625 and this appears to be very sensitive
    """
    
    modules['atts'][8][0][0][0] = script_params[1]
    
    # insert the inputs stimulus into LGN and see what happens
    # the following stimulus is an 'o' shape
    modules['lgns'][8][3][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][3][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][3][5][0] = 0.7 #script_params[3]
    modules['lgns'][8][3][6][0] = 0.7 #script_params[3]
    modules['lgns'][8][3][7][0] = 0.7 #script_params[3]
    modules['lgns'][8][3][8][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][5][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][6][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][7][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][8][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][5][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][6][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][7][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][8][0] = 0.7 #script_params[3]
    modules['lgns'][8][5][8][0] = 0.7 #script_params[3]
    modules['lgns'][8][6][8][0] = 0.7 #script_params[3]
    modules['lgns'][8][7][8][0] = 0.7 #script_params[3]
    
def T_shape(modules, script_params):
    
    """
    generates a t-shaped visual input to neural network with parameters given"
    Good intensity is about .69625 and this appears to be very sensitive
    """
    modules['atts'][8][0][0][0] = script_params[1]

    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'T' shape
    modules['lgns'][8][0][0][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][2][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][5][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][6][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][7][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][8][0] = 0.7 #script_params[3]
    # stem
    modules['lgns'][8][1][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][2][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][3][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][5][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][6][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][7][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][4][0] = 0.7 #script_params[3]

def cross_shape(modules, script_params):
    """
    generates a cross(+)-shaped visual input to neural network with parameters given"
    Good intensity is about .69625 and this appears to be very sensitive
    """
    modules['atts'][8][0][0][0] = script_params[1]

    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'cross' shape
    modules['lgns'][8][4][0][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][2][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][5][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][6][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][7][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][8][0] = 0.7 #script_params[3]
    # the other part of the t
    modules['lgns'][8][0][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][1][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][2][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][3][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][5][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][6][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][7][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][4][0] = 0.7 #script_params[3]

def trident_shape(modules, script_params):
    """
    generates a trident-shaped visual input to neural network with parameters given"
    Good intensity is about .65
    """
    modules['atts'][8][0][0][0] = script_params[1]

    # insert the inputs stimulus into LGN and see what happens
    # Trident
    # left prong 
    modules['lgns'][8][1][1][0] = 0.65 #script_params[3]
    modules['lgns'][8][1][2][0] = 0.65 #script_params[3]
    modules['lgns'][8][1][3][0] = 0.65 #script_params[3]
    # left side
    modules['lgns'][8][2][3][0] = 0.65 #script_params[3]
    modules['lgns'][8][3][3][0] = 0.65 #script_params[3]
    # center piece
    modules['lgns'][8][4][1][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][2][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][3][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][4][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][5][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][6][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][7][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][8][0] = 0.65 #script_params[3]
    # right side
    modules['lgns'][8][5][3][0] = 0.65 #script_params[3]
    modules['lgns'][8][6][3][0] = 0.65 #script_params[3]
    # left prong 
    modules['lgns'][8][7][1][0] = 0.65 #script_params[3]
    modules['lgns'][8][7][2][0] = 0.65 #script_params[3]
    modules['lgns'][8][7][3][0] = 0.65 #script_params[3]

def E_shape(modules, script_params):
    """
    generates a E-shaped visual input to neural network with parameters given"
    good intensity of .655
    """
    modules['atts'][8][0][0][0] = script_params[1]

    # insert the inputs stimulus into LGN and see what happens
    # E Stimulus: 17 units
    modules['lgns'][8][0][2][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][4][0] = 0.7 #script_params[3]
    # middle
    modules['lgns'][8][4][2][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][4][0] = 0.7 #script_params[3]
    # bottom
    modules['lgns'][8][8][2][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][4][0] = 0.7 #script_params[3]
    # stem
    modules['lgns'][8][0][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][1][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][2][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][3][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][5][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][6][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][7][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][1][0] = 0.7 #script_params[3]
# ------------------------------------------------------------------------

def o_shape_LA(modules, script_params):
    
    """
    generates an o-shaped visual input to neural network with parameters given
    Good intensity is about .69625 and this appears to be very sensitive
    """
    
    modules['atts'][8][0][0][0] = script_params[0]
    
    # insert the inputs stimulus into LGN and see what happens
    # the following stimulus is an 'o' shape
    modules['lgns'][8][4][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][5][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][6][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][7][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][8][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][5][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][6][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][7][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][8][0] = 0.7 #script_params[3]
    modules['lgns'][8][5][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][6][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][7][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][5][8][0] = 0.7 #script_params[3]
    modules['lgns'][8][6][8][0] = 0.7 #script_params[3]
    modules['lgns'][8][7][8][0] = 0.7 #script_params[3]
    
def T_shape_LA(modules, script_params):
    
    """
    generates a t-shaped visual input to neural network with parameters given"
    Good intensity is about .69625 and this appears to be very sensitive
    """
    modules['atts'][8][0][0][0] = script_params[0]

    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'T' shape
    modules['lgns'][8][0][0][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][2][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][5][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][6][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][7][0] = 0.7 #script_params[3]
    modules['lgns'][8][0][8][0] = 0.7 #script_params[3]
    # stem
    modules['lgns'][8][1][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][2][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][3][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][5][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][6][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][7][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][4][0] = 0.7 #script_params[3]

def cross_shape_LA(modules, script_params):
    """
    generates a cross(+)-shaped visual input to neural network with parameters given"
    Good intensity is about .69625 and this appears to be very sensitive
    """
    modules['atts'][8][0][0][0] = script_params[0]

    # insert the inputs stimulus into LGN and see what happens
    # the following is a 'cross' shape
    modules['lgns'][8][4][0][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][1][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][2][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][3][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][5][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][6][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][7][0] = 0.7 #script_params[3]
    modules['lgns'][8][4][8][0] = 0.7 #script_params[3]
    # the other part of the t
    modules['lgns'][8][0][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][1][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][2][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][3][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][5][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][6][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][7][4][0] = 0.7 #script_params[3]
    modules['lgns'][8][8][4][0] = 0.7 #script_params[3]

def trident_shape_LA(modules, script_params):
    """
    generates a trident-shaped visual input to neural network with parameters given"
    Good intensity is about .65
    """
    modules['atts'][8][0][0][0] = script_params[0]

    # insert the inputs stimulus into LGN and see what happens
    # Trident
    # left prong 
    modules['lgns'][8][1][1][0] = 0.65 #script_params[3]
    modules['lgns'][8][1][2][0] = 0.65 #script_params[3]
    modules['lgns'][8][1][3][0] = 0.65 #script_params[3]
    # left side
    modules['lgns'][8][2][3][0] = 0.65 #script_params[3]
    modules['lgns'][8][3][3][0] = 0.65 #script_params[3]
    # center piece
    modules['lgns'][8][4][1][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][2][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][3][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][4][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][5][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][6][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][7][0] = 0.65 #script_params[3]
    modules['lgns'][8][4][8][0] = 0.65 #script_params[3]
    # right side
    modules['lgns'][8][5][3][0] = 0.65 #script_params[3]
    modules['lgns'][8][6][3][0] = 0.65 #script_params[3]
    # left prong 
    modules['lgns'][8][7][1][0] = 0.65 #script_params[3]
    modules['lgns'][8][7][2][0] = 0.65 #script_params[3]
    modules['lgns'][8][7][3][0] = 0.65 #script_params[3]

def E_shape_LA(modules, script_params):
    """
    generates a E-shaped visual input to neural network with parameters given"
    good intensity of .655
    """
    modules['atts'][8][0][0][0] = script_params[0]

    # insert the inputs stimulus into LGN and see what happens
    # E Stimulus: 17 units
    modules['lgns'][8][0][2][0] = 0.655 #script_params[3]
    modules['lgns'][8][0][3][0] = 0.655 #script_params[3]
    modules['lgns'][8][0][4][0] = 0.655 #script_params[3]
    # middle
    modules['lgns'][8][4][2][0] = 0.655 #script_params[3]
    modules['lgns'][8][4][3][0] = 0.655 #script_params[3]
    modules['lgns'][8][4][4][0] = 0.655 #script_params[3]
    # bottom
    modules['lgns'][8][8][2][0] = 0.655 #script_params[3]
    modules['lgns'][8][8][3][0] = 0.655 #script_params[3]
    modules['lgns'][8][8][4][0] = 0.655 #script_params[3]
    # stem
    modules['lgns'][8][0][1][0] = 0.655 #script_params[3]
    modules['lgns'][8][1][1][0] = 0.655 #script_params[3]
    modules['lgns'][8][2][1][0] = 0.655 #script_params[3]
    modules['lgns'][8][3][1][0] = 0.655 #script_params[3]
    modules['lgns'][8][4][1][0] = 0.655 #script_params[3]
    modules['lgns'][8][5][1][0] = 0.655 #script_params[3]
    modules['lgns'][8][6][1][0] = 0.655 #script_params[3]
    modules['lgns'][8][7][1][0] = 0.655 #script_params[3]
    modules['lgns'][8][8][1][0] = 0.655 #script_params[3]
# ------------------------------------------------------------------------

def random_shape_1(modules, script_params):
    """
    generates a random visual input to neural network with parameters given
    
    """
    modules['atts'][8][0][0][0] = script_params[0]

    for k1 in range(len(script_params[5])):
        modules['lgns'][8][script_params[5][k1][0]][script_params[5][k1][1]][0] = script_params[3]
    
def random_shape_2(modules, script_params):
    """
    generates a random visual input to neural network with parameters given
    
    """
    
    modules['atts'][8][0][0][0] = script_params[0]

    for k1 in range(len(script_params[6])):
        modules['lgns'][8][script_params[6][k1][0]][script_params[6][k1][1]][0] = script_params[3]
# ------------------------------------------------------------------------

def random_shape_o_Hi(modules, script_params):
    """
    generates a random visual input to neural network with parameters given
    """
    modules['atts'][8][0][0][0] = script_params[1]

    for k1 in range(len(script_params[5])):
        modules['lgns'][8][script_params[5][k1][0]][script_params[5][k1][1]][0] = script_params[3]
    
def random_shape_T_Hi(modules, script_params):
    """
    generates a random visual input to neural network with parameters given
    """
    
    modules['atts'][8][0][0][0] = script_params[1]

    for k1 in range(len(script_params[6])):
        modules['lgns'][8][script_params[6][k1][0]][script_params[6][k1][1]][0] = script_params[3]


def random_shape_cross_Hi(modules, script_params):
    """
    generates a random visual input to neural network with parameters given
    """
    modules['atts'][8][0][0][0] = script_params[1]

    for k1 in range(len(script_params[5])):
        modules['lgns'][8][script_params[5][k1][0]][script_params[5][k1][1]][0] = script_params[3]
    
def random_shape_trident_Hi(modules, script_params):
    """
    generates a random visual input to neural network with parameters given
    """
    modules['atts'][8][0][0][0] = script_params[1]

    for k1 in range(len(script_params[6])):
        modules['lgns'][8][script_params[6][k1][0]][script_params[6][k1][1]][0] = script_params[3]
# ------------------------------------------------------------------------

def random_shape_o_Lo(modules, script_params):
    """
    generates a random visual input to neural network with parameters given 
    """
    modules['atts'][8][0][0][0] = script_params[0]

    for k1 in range(len(script_params[5])):
        modules['lgns'][8][script_params[5][k1][0]][script_params[5][k1][1]][0] = script_params[3]
    
def random_shape_T_Lo(modules, script_params):
    """
    generates a random visual input to neural network with parameters given
    """   
    modules['atts'][8][0][0][0] = script_params[0]

    for k1 in range(len(script_params[6])):
        modules['lgns'][8][script_params[6][k1][0]][script_params[6][k1][1]][0] = script_params[3]

def random_shape_cross_Lo(modules, script_params):
    """
    generates a random visual input to neural network with parameters given
    """
    modules['atts'][8][0][0][0] = script_params[0]

    for k1 in range(len(script_params[5])):
        modules['lgns'][8][script_params[5][k1][0]][script_params[5][k1][1]][0] = script_params[3]
    
def random_shape_trident_Lo(modules, script_params):
    """
    generates a random visual input to neural network with parameters given   
    """
    modules['atts'][8][0][0][0] = script_params[0]

    for k1 in range(len(script_params[6])):
        modules['lgns'][8][script_params[6][k1][0]][script_params[6][k1][1]][0] = script_params[3]

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      
def delay_period(modules, script_params):
    
    """
    modifies neural network with delay period parameters given

    """
    
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['lgns'][0]):
        for y in range(modules['lgns'][1]):
            modules['lgns'][8][x][y][0] = script_params[2]

def end_trial(modules, script_params):
    
    """
    modifies neural network with delay period parameters given
    """
    # turn attention to 'LO', as the current trial has ended
    modules['atts'][8][0][0][0] = script_params[0]
    # turn off input stimulus but leave small level of activity there
    for x in range(modules['lgns'][0]):
        for y in range(modules['lgns'][1]):
            modules['lgns'][8][x][y][0] = script_params[2]

def intertrial_interval(modules, script_params):
    """
    resets the visual inputs and short-term memory using given parameters

    """

    # reset 
    for x in range(modules['efd1'][0]):
        for y in range(modules['efd1'][1]):
            modules['efd1'][8][x][y][0] = .2 #script_params[2]
            modules['efd2'][8][x][y][0] = .2 #script_params[2]
            
            

    # turn off input stimulus but leave small level of activity there
    for x in range(modules['lgns'][0]):
        for y in range(modules['lgns'][1]):
            modules['lgns'][8][x][y][0] = script_params[2]

    # turn attention to 'LO', as the current trial has ended
    modules['atts'][8][0][0][0] = script_params[0]

def increase_attention(modules, script_params):
    """
    Increases 'hi_att_level' by a step given by 'att_step'

    """

    script_params[1] = script_params[1] + script_params[4]


    
# define a dictionary of simulation events functions, each associated with
# a specific simulation timestep
# ridiculous spacing for fMRI to resolve the HRF, hopefully
simulation_events = {
       	'200':	T_shape_LA,
	'400':	delay_period,
	'800':	T_shape_LA,
	'1000':	end_trial,
	'1200':intertrial_interval,
	'1400':T_shape_LA,
	'1600':delay_period,
	'2000':cross_shape_LA,
	'2200':end_trial,
	'2400':intertrial_interval,
	'2600':cross_shape_LA,
	'2800':delay_period,
	'3200':cross_shape_LA,
	'3400':end_trial,
	'3600':intertrial_interval,
	'3800':cross_shape_LA,
	'4000':delay_period,
	'4400':T_shape_LA,
	'4600':end_trial,
	'4800':intertrial_interval
}
