.globl matmul
.text
# =======================================================
# FUNCTION: Matrix Multiplication of 2 integer matrices
# 	d = matmul(m0, m1)
# Arguments:
# 	a0 (int*)  is the pointer to the start of m0 
#	a1 (int)   is the # of rows (height) of m0
#	a2 (int)   is the # of columns (width) of m0
#	a3 (int*)  is the pointer to the start of m1
# 	a4 (int)   is the # of rows (height) of m1
#	a5 (int)   is the # of columns (width) of m1
#	a6 (int*)  is the pointer to the the start of d
# Returns:
#	None (void), sets d = matmul(m0, m1)
# Exceptions:
#   Make sure to check in top to bottom order!
#   - If the dimensions of m0 do not make sense,
#     this function terminates the program with exit code 72.
#   - If the dimensions of m1 do not make sense,
#     this function terminates the program with exit code 73.
#   - If the dimensions of m0 and m1 don't match,
#     this function terminates the program with exit code 74.
# =======================================================
matmul:
    addi x2, x2, -40  # Store all values into perm. regs to use.
    sw x8, 0(x2) # Store all values into perm. regs to use.
    sw x1, 24(x2) # Store all values into perm. regs to use.
    sw x18, 8(x2) # Store all values into perm. regs to use.
    sw x20, 16(x2) # Store all values into perm. regs to use.
    sw x22, 28(x2) # Store all values into perm. regs to use.
    sw x9, 4(x2) # Store all values into perm. regs to use.
    sw x19, 12(x2) # Store all values into perm. regs to use.
    sw x21, 20(x2) # Store all values into perm. regs to use.
    sw x23, 32(x2) # Store all values into perm. regs to use.
    sw x24, 36(x2) # Store all values into perm. regs to use.
    li x29, 4 # Shift values into newly created registers.
    mv x19, a5 # Shift values into newly created registers.
    mv x23, a5 # Shift values into newly created registers.
    mv x18, a4 # Shift values into newly created registers.
    mv x20, a6 # Shift values into newly created registers.
    mv x9, a2 # Shift values into newly created registers.
    mv x24, a2 # Shift values into newly created registers.
    mv x21, a3 # Shift values into newly created registers.
    mv x8, a1 # Shift values into newly created registers.
    mul x22, x29, x9 # Set value of x22 to be a multiple of x29*x9.
    sub x5, a0, x22 # Subtract the pointer by x22.
    mv x7, a3
    mv x28, x0
    li x6, 0
    li x31, 1 # Set values for counter, values, etc.
    j test10 # Move to first test
test3:
    beq x9, x18, outer_loop_start # If dimensions match, continue
    li a1, 74 # Error code 74
    j exit2
test10:
    mv x29, x8
    bge x29, x31, test11 # If number of rows are 1 and more, move to next test.
    li a1, 72 # Exit code 72.
    j exit2
test21:
    mv x29, x18
    bge x29, x31, test22 # If number of rows are 1 and more, move to next test.
    li a1, 73 # Exit code 73.
    j exit2
test11:
    mv x29, x9
    bge x29, x31, test21 # If number of columns are 1 and more, move to next test.
    li a1, 72 # Error code 72.
    j exit2
test22:
    mv x29, x19
    bge x29, x31, test3 # If number of columns are 1 and more, move to next test.
    li a1, 73 # Error code 73.
    j exit2
outer_loop_start:
    beq x6, x8, outer_loop_end # Begin outer loop if counter has not reached max
    add x5, x5, x22
    mv a4, x19 # Set new value to a4
    addi x6, x6, 1
    addi x7, x21, -4 # Move x21 by -4 to set in x7.
    mv a2, x9
    li a3, 1
    li x28, 0 # Initiate counter and values
inner_loop_start:
    beq x28, x19, outer_loop_start # Begin inner loop if counter has not reached max
    addi x7, x7, 4 # Move by 4
    addi x2, x2, -16
    li a3, 1
    addi x28, x28, 1 # Increment x28 by 1
    sw x5, 0(x2)
    sw x28, 12(x2)
    sw x7, 8(x2) # Store values from x2 to other registers.
    sw x6, 4(x2)
    mv a2, x24 # Transfer values to new vals.
    mv a0, x5
    mv a4, x23
    mv a1, x7
    jal x1 dot # Call for dot.s function.
inner_loop_end:
    lw x5, 0(x2)
    lw x7, 8(x2)
    lw x28, 12(x2)
    lw x6, 4(x2) # Free values to different registers.
    sw a0, 0(x20) # Set new val to a0
    addi x20, x20, 4
    addi x2, x2, 16
    j inner_loop_start # Begin next loop.
outer_loop_end:
    lw x20, 16(x2) # Free all registers and unload to values
    lw x23, 32(x2) # Free all registers and unload to values
    lw x9, 4(x2) # Free all registers and unload to values
    lw x19, 12(x2) # Free all registers and unload to values
    lw x22, 28(x2) # Free all registers and unload to values
    lw x24, 36(x2) # Free all registers and unload to values
    lw x8, 0(x2) # Free all registers and unload to values
    lw x21, 20(x2) # Free all registers and unload to values
    lw x18, 8(x2) # Free all registers and unload to values
    lw x1, 24(x2) # Free all registers and unload to values
    addi x2, x2, 40 # Skip by 40, since 0 to 36 were used.
    ret # Return
