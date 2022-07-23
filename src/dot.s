.globl dot

.text
# =======================================================
# FUNCTION: Dot product of 2 int vectors
# Arguments:
#   a0 (int*) is the pointer to the start of v0
#   a1 (int*) is the pointer to the start of v1
#   a2 (int)  is the length of the vectors
#   a3 (int)  is the stride of v0
#   a4 (int)  is the stride of v1
# Returns:
#   a0 (int)  is the dot product of v0 and v1
# Exceptions:
# - If the length of the vector is less than 1,
#   this function terminates the program with error code 75.
# - If the stride of either vector is less than 1,
#   this function terminates the program with error code 76.
# =======================================================
dot:
    li x5, 1
    bge a2, x5, firststr # If the length is not less than 1, carry on.
    li a1, 75 # Error code 75
    jal x1 exit2
secondstr:
    li x5, 1
    bge a4, x5, init # If the stride is not less than 1, carry on.
    li a1, 76 # Error code 76
    jal x1 exit2
init:
    li x6, 0
    li x5, 0 # Initialize x5 and x6 to be 0 foor the use in loops.
    j loop_start
firststr:
    li x5, 1
    bge a3, x5, secondstr # If the stride is not less than 1, carry on.
    li a1, 76 # Error code 76
    jal x1 exit2
loop_start:
    bge x6, a2, loop_end # End the loop if iterative variable has reached the end.
    slli x7, x6, 2 # Shift left by 2 (Logicalaly)
    mul x29, x7, a4
    mul x28, x7, a3
    add x29, x29, a1
    add x28, x28, a0 # Set up a1 and a0 variables in temp values for calculation.
    lw x28, 0(x28)
    lw x29, 0(x29)
    mul x7, x28, x29 # Multiply each vector value
    addi x6, x6, 1 # Increment counter
    add x5, x5, x7
    j loop_start
loop_end:
    mv a0, x5 # Set a0 to value of x5, and end call.
    ret
