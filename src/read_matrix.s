.globl read_matrix

.text
# ==============================================================================
# FUNCTION: Allocates memory and reads in a binary file as a matrix of integers
#
# FILE FORMAT:
#   The first 8 bytes are two 4 byte ints representing the # of rows and columns
#   in the matrix. Every 4 bytes afterwards is an element of the matrix in
#   row-major order.
# Arguments:
#   a0 (char*) is the pointer to string representing the filename
#   a1 (int*)  is a pointer to an integer, we will set it to the number of rows
#   a2 (int*)  is a pointer to an integer, we will set it to the number of columns
# Returns:
#   a0 (int*)  is the pointer to the matrix in memory
# Exceptions:
# - If malloc returns an error,
#   this function terminates the program with error code 88.
# - If you receive an fopen error or eof, 
#   this function terminates the program with error code 90.
# - If you receive an fread error or eof,
#   this function terminates the program with error code 91.
# - If you receive an fclose error or eof,
#   this function terminates the program with error code 92.
# ==============================================================================
end_errcl:
    # Function taking care of fclose errors
    li a1, 92 #Set error to 92
    j exit2
end_open:
    # Function taking care of fopen errors
    li a1, 90 # Set error to 90
    j exit2
end_read:
    # Function taking care of fread errors
    li a1, 91 # Set error to 91
    j exit2
end_mall:
    # Function taking care of malloc errors
    jal free # Free variables
    li a1, 88 # Set error to 88
    j exit2
read_matrix:
    addi x2, x2, -44 # Space Size
    sw ra, 0(x2)
    sw a0, 4(x2)
    sw a1, 8(x2)
    sw a2, 12(x2)
    sw x8, 16(x2)
    sw x9, 20(x2)
    sw x18, 24(x2)
    sw x19, 28(x2)
    sw x20, 32(x2)
    sw x21, 36(x2)
    sw x22, 40(x2)
    # ^^^ Setting values for our sp register
    li a0, 8
    jal malloc # Malloc space
    beq a0, x0, end_mall # Take care of malloc errors
    li a2, 0
    lw a1, 4(x2)
    mv x19, a0
    jal fopen # Open file
    li x5, -1
    beq x5, a0, end_open # Take care of fopen error
    mv a2, x19
    mv x20, a0
    li a3, 8
    mv a1, x20
    jal fread # Read file
    li x5, 8
    bne x5, a0, end_read # Take care of fread error
    lw x21, 0(x19)
    lw x22, 4(x19)
    li x5, 4
    mul x8, x21, x22
    mul x9, x8, x5
    mv a0, x9
    blt x21, x0, end_mall # Take care of malloc error
    blt x22, x0, end_mall # Take care of malloc error
    jal malloc # Malloc space
    beq a0, x0, end_mall # Take care of malloc error
    mv x18, a0
    mv a2, x18
    mv a3, x9
    mv a1, x20
    jal fread # Read file
    bne x9, a0, end_read # Take care of fread error
    mv a1, x20
    jal fclose # Close file
    li x5, -1
    beq x5, a0, end_errcl # Take care of close error
    lw a0, 4(x2)
    lw ra, 0(x2)
    lw x9, 20(x2)
    lw a1, 8(x2)
    sw x21, 0(a1)
    lw a2, 12(x2)
    sw x22, 0(a2)
    lw x21, 36(x2)
    lw x8, 16(x2)
    lw x19, 28(x2)
    mv a0, x18
    lw x20, 32(x2)
    lw x18, 24(x2)
    lw x22, 40(x2)
    # Free values and store x18 to a0 ^^^
    addi x2, x2, 44
    ret
