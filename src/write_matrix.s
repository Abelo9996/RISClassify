.globl write_matrix

.text
# ==============================================================================
# FUNCTION: Writes a matrix of integers into a binary file
# FILE FORMAT:
#   The first 8 bytes of the file will be two 4 byte ints representing the
#   numbers of rows and columns respectively. Every 4 bytes thereafter is an
#   element of the matrix in row-major order.
# Arguments:
#   a0 (char*) is the pointer to string representing the filename
#   a1 (int*)  is the pointer to the start of the matrix in memory
#   a2 (int)   is the number of rows in the matrix
#   a3 (int)   is the number of columns in the matrix
# Returns:
#   None
# Exceptions:
# - If you receive an fopen error or eof,
#   this function terminates the program with error code 93.
# - If you receive an fwrite error or eof,
#   this function terminates the program with error code 94.
# - If you receive an fclose error or eof,
#   this function terminates the program with error code 95.
# ==============================================================================
end_open:
    # Taking care of fopen error
    li a1, 93 # Assigning 93 as exit code
    j exit2
end_errcl:
    # Taking care of fclose error
    li a1, 95 # Assigning 95 as exit code
    j exit2
end_write:
    # Taking care of fwrite error
    li a1, 94 # Assigning 94 as exit code
    j exit2
write_matrix:
    addi x2, x2, -28 # Set sp size
    sw ra, 0(x2)
    sw x8, 4(x2)
    sw x9, 8(x2)
    sw x18, 12(x2)
    sw x19, 16(x2)
    sw x20, 20(x2)
    sw x21, 24(x2)
    # Setting up values in sp that we assigned
    mv x9, a1
    mv x8, a0
    mv x18, a2
    li a2, 1
    mv x19, a3
    mv a1, a0
    # Setting values above ^^^
    jal fopen # fopen our file
    li x5, -1
    beq x5, a0, end_open # Take care of fopen errors
    addi x2, x2, -8
    sw x18, 0(x2)
    sw x19, 4(x2)
    # Setting up values for row and col
    mv x21, a0
    mv a2, x2
    mv a1, x21
    li a3, 2
    li a4, 4
    # Setting up values for fwrite ^^^
    jal fwrite # fwrite our file
    li x5, 2
    bne a0, x5, end_write # Take care of fwrite errors
    mul x20, x18, x19 # Entire size of matrix
    li a4, 4
    mv a2, x9
    mv a3, x20
    mv a1, x21
    addi x2, x2, 8
    # Set up values for fwrite ^^^
    jal fwrite # fwrite our matrix part
    bne a0, x20, end_write # Take care of fwrite errors
    mv a1, x21
    jal fclose # fclose the file
    li x5, -1
    beq x5, a0, end_errcl # Take care of fclose errors
    lw ra, 0(x2)
    lw x18, 12(x2)
    lw x21, 24(x2)
    lw x19, 16(x2)
    lw x8, 4(x2)
    lw x20, 20(x2)
    lw x9, 8(x2)
    # Retreive and assign values once again ^^^
    addi x2, x2, 28
    ret # Return
