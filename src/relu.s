.globl relu

.text
# ==============================================================================
# FUNCTION: Performs an inplace element-wise ReLU on an array of ints
# Arguments:
# 	a0 (int*) is the pointer to the array
#	a1 (int)  is the # of elements in the array
# Returns:
#	None
# Exceptions:
# - If the length of the vector is less than 1,
#   this function terminates the program with error code 78.
# ==============================================================================
relu:
    li x5, 1
    bge a1, x5, init #Begins loop if a1 is not less than 1
    addi a1, x0, 78 #Error code of 78
    jal x1 exit2
init:
    li x5, 0 # Set counter to 0
loop_start:
    bge x5, a1,loop_end #End loop if all vectors checked
    slli x6, x5, 2
    add x7, a0, x6
    lw x28, 0(x7)
    bge x28, zero, loop_continue # Skip to next element if vector is non-negative
    sw zero, 0(x7)
loop_continue:
    addi x5, x5, 1
    j loop_start # Next iteration of array
loop_end:
    ret
