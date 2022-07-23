.globl argmax
.text
# =================================================================
# FUNCTION: Given a int vector, return the index of the largest
#	element. If there are multiple, return the one
#	with the smallest index.
# Arguments:
# 	a0 (int*) is the pointer to the start of the vector
#	a1 (int)  is the # of elements in the vector
# Returns:
#	a0 (int)  is the first index of the largest element
# Exceptions:
# - If the length of the vector is less than 1,
#   this function terminates the program with error code 77.
# =================================================================
argmax:
    addi x2, x2, -24
    sw x7, 8(x2)
    sw x5, 0(x2)
    sw x6, 4(x2)
    sw x29, 16(x2)
    sw x28, 12(x2)
    sw x1, 20(x2) #Store all placeholder values within x2.
    li x28, -2048 # Store lowest value that is negative
    li x7, 1
    li x6, 0
    li x29, 0
    blt a1, x7, endifless # End if a1 is 0 or less.
    addi a1, a1, -1 # Otherwise, begin loop.
loop_start:
	lw x5, 0(a0)
    beq x5, x28, loop_continue
    blt x5, x28, loop_continue # Continue the loop if x5 is less than or equal to x28
    mv x28, x5
    add x29, x0, x6
loop_continue:
	beq a1, x6, done # If a1 is equal to our counter, finish loop.
    addi a0, a0, 4 # Move to next item in array.
    addi x6, x6, 1
    jal loop_start # Begin loop once again
endifless:
    lw x6, 4(x2)
    lw x7, 8(x2)
    lw x29, 16(x2)
    lw x1, 20(x2)
   	lw x28, 12(x2)
	lw x5, 0(x2) # Free all memory
    addi x2, x2, 24
    li a1, 77 #Exit code 77
	j exit2
done:
    lw x5, 0(x2)
   	lw x28, 12(x2)
    lw x7, 8(x2)
    lw x6, 4(x2)
	mv a0, x29
    lw x1, 20(x2)
    lw x29, 16(x2) # Free all memory.
    addi x2, x2, 24
	ret #Return
