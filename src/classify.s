.globl classify
.text
    # =====================================
    # COMMAND LINE ARGUMENTS
    # =====================================
    # Args:
    #   a0 (int)    argc
    #   a1 (char**) argv
    #   a2 (int)    print_classification, if this is zero, 
    #               you should print the classification. Otherwise,
    #               this function should not print ANYTHING.
    # Returns:
    #   a0 (int)    Classification
    # Exceptions:
    # - If there are an incorrect number of command line args,
    #   this function terminates the program with exit code 89.
    # - If malloc fails, this function terminats the program with exit code 88.
    #
    # Usage:
    #   main.s <M0_PATH> <M1_PATH> <INPUT_PATH> <OUTPUT_PATH>
err_mall:
    # Function that handles Malloc errors
    jal free # Free space
    li a1, 88 # Set error code to 88
    j exit2
err_cl:
    # Function that handles command line args 
    li a1, 89 # Set error code to 89
    j exit2
classify:
    li x28, 5
    bne x28, a0, err_cl
    addi x2, x2, -52 # Set variable space
    sw ra, 0(x2)
    # Set all the registers to their respective spaces ^^^^
    sw x8, 4(x2)
    sw x9, 8(x2)
    # Set all the registers to their respective spaces ^^^^
    sw x18, 12(x2)
    sw x19, 16(x2)
    # Set all the registers to their respective spaces ^^^^
    sw x20, 20(x2)
    sw x21, 24(x2)
    # Set all the registers to their respective spaces ^^^^
    sw x22, 28(x2)
    sw x23, 32(x2)
    # Set all the registers to their respective spaces ^^^^
    sw x24, 36(x2)
    sw x25, 40(x2)
    # Set all the registers to their respective spaces ^^^^
    sw x26, 44(x2)
    sw x27, 48(x2)
    # Set all the registers to their respective spaces ^^^^
    mv x9, a1 # Set argv to x9
    mv x8, a0 # Set argc to x8 
    addi a0, x0, 8
    mv x18, a2
    jal malloc # Call malloc for space
    beq a0, x0, err_mall # If a0 is 0, handle as a malloc error
    mv x19, a0
    mv a1, x19
    addi a2, x19, 4
    lw a0, 4(x9) # Assign second element of x9 to a0
    jal read_matrix # Call to read matrix
    mv x21, a0 # Set a0 to x21
    addi a0, x0, 8 # Add a0 by 8
    jal malloc # Call malloc for space
    beq a0, x0, err_mall # If a0 is 0, handle as malloc error
    mv x20, a0
    mv a1, x20 # Set a1 as a0
    lw a0, 8(x9) # Load third element of x9 to a0
    addi a2, x20, 4
    jal read_matrix # Call to read matrix
    mv x22, a0
    addi a0, x0, 8
    jal malloc # Call malloc for space
    beq a0, x0, err_mall # If a0 is 0, handle as malloc error
    mv x23, a0 
    mv a1, x23 # Set a1 to a0
    lw a0, 12(x9) # Load fourth element of x9 to a0
    addi a2, x23, 4
    jal read_matrix # Call to read matrix
    li x28, 4
    mv x24, a0 
    lw x6, 4(x23) # Get row
    lw x7, 0(x19) # Get col
    mul x5, x7, x6 # col*row
    mv x26, x5 # Set x26 as col*row
    mul x5, x5, x28
    mv a0, x5
    jal malloc # Call malloc for space
    beq a0, x0, err_mall # If a0 is 0, handle as malloc erro
    mv x25, a0
    mv a0, x21
    lw a1, 0(x19)
    lw a2, 4(x19)
    mv a3, x24
    lw a4, 0(x23)
    lw a5, 4(x23)
    mv a6, x25
    # Unload values to registers a0-a6
    jal matmul # Call for matmul
    mv a0, x25
    mv a1, x26
    # Set a0 and a1 values for relu ^^^
    jal relu # Call for relu
    # Same procedure as above ^^^
    li x28, 4
    lw x7, 0(x20)
    lw x6, 4(x23)
    mul x5, x7, x6
    mv x26, x5
    mul x5, x5, x28
    mv a0, x5
    jal malloc # Call malloc for space
    beq a0, x0, err_mall # If a0 is zero, call for malloc error
    mv x27, a0
    mv a0, x22
    lw a1, 0(x20)
    lw a2, 4(x20)
    mv a3, x25
    lw a4, 0(x19)
    lw a5, 4(x23)
    mv a6, x27
    # Once again, same procedure for matmul as abovee
    jal matmul
    lw a0, 16(x9)
    mv a1, x27
    lw a2, 0(x20)
    lw a3, 4(x23)
    # Set a0-a3 values for write_matrix ^^^
    jal write_matrix # Call to write a matrix
    mv a0, x27
    mv a1, x26
    # Set a0 and a1 for argmax call
    jal argmax # Call for argmax
    mv x8, a0
    bne x18, x0, finish # If our counter is 0, end call.
    mv a1, x8
    jal print_int # Print integer
    li a1, 10
    jal print_char # Print character
finish:
    mv a0, x19
    jal free
    # Unpack values and free malloc'd space ^^^
    mv a0, x20
    jal free
    # Unpack values and free malloc'd space ^^^
    mv a0, x21
    jal free
    # Unpack values and free malloc'd space ^^^
    mv a0, x22
    jal free
    # Unpack values and free malloc'd space ^^^
    mv a0, x23
    jal free
    # Unpack values and free malloc'd space ^^^
    mv a0, x24
    # Move our x24 register to the value of a0
    jal free
    # Unpack values and free malloc'd space ^^^
    mv a0, x25
    jal free
    # Unpack values and free malloc'd space ^^^
    mv a0, x27
    jal free
    mv a0, x8
    # Unpack values and free malloc'd space ^^^
    lw ra, 0(x2)
    # Unpack the set values at start of code
    lw x8, 4(x2)
    lw x9, 8(x2)
    # Unpack the set values at start of code
    lw x18, 12(x2)
    lw x19, 16(x2)
    # Unpack the set values at start of code
    lw x20, 20(x2)
    lw x21, 24(x2)
    # Unpack the set values at start of code
    lw x22, 28(x2)
    lw x23, 32(x2)
    # Unpack the set values at start of code
    lw x24, 36(x2)
    lw x25, 40(x2)
    # Unpack the set values at start of code
    lw x26, 44(x2)
    lw x27, 48(x2)
    # Unpack the set values at start of code
    addi x2, x2, 52
    ret # Return
