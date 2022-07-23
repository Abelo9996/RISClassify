from unittest import TestCase
from framework import AssemblyTest, print_coverage


class TestAbs(TestCase):
    def test_zero(self):
        t = AssemblyTest(self, "abs.s")
        # load 0 into register a0
        t.input_scalar("a0", 0)
        # call the abs function
        t.call("abs")
        # check that after calling abs, a0 is equal to 0 (abs(0) = 0)
        t.check_scalar("a0", 0)
        # generate the `assembly/TestAbs_test_zero.s` file and run it through venus
        t.execute()

    def test_one(self):
        # Test for a simple 1
        t = AssemblyTest(self, "abs.s")
        t.input_scalar("a0", 1)
        t.call("abs")
        t.check_scalar("a0", 1)
        t.execute()

    def test_minus_one(self):
        # Test for a simple -1
    	t = AssemblyTest(self, "abs.s")
    	t.input_scalar("a0", -1)
    	t.call("abs")
    	t.check_scalar("a0", 1)
    	t.execute()

    @classmethod
    def tearDownClass(cls):
        print_coverage("abs.s", verbose=False)


class TestRelu(TestCase):
    def test_simple(self):
        t = AssemblyTest(self, "relu.s")
        # create an array in the data section
        array0 = t.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
        # load address of `array0` into register a0
        t.input_array("a0", array0)
        # set a1 to the length of our array
        t.input_scalar("a1", len(array0))
        # call the relu function
        t.call("relu")
        # check that the array0 was changed appropriately
        t.check_array(array0, [1, 0, 3, 0, 5, 0, 7, 0, 9])
        # generate the `assembly/TestRelu_test_simple.s` file and run it through venus
        t.execute(code=0)

    def test_one(self):
        # Test for a simple -1 within the array
        t = AssemblyTest(self, "relu.s")
        array0 = t.array([-1])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("relu")
        t.check_array(array0, [0])
        t.execute(code=0)
        
    def test_two(self):
        # Test for a simple 0 within the array
        t = AssemblyTest(self, "relu.s")
        array0 = t.array([0])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("relu")
        t.check_array(array0, [0])
        t.execute()
 
    def test_three(self):
        # Test for a simple 1 within the array
        t = AssemblyTest(self, "relu.s")
        array0 = t.array([1])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("relu")
        t.check_array(array0, [1])
        t.execute()
 
    def test_four(self):
        # Test for a fully negative array.
        t = AssemblyTest(self, "relu.s")
        array0 = t.array([-1, -2, -3, -4, -5, -6, -7, -8, -9])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("relu")
        t.check_array(array0, [0, 0, 0, 0, 0, 0, 0, 0, 0])
        t.execute(code=0)
 
    def test_five(self):
        # Test for a fully zero array
        t = AssemblyTest(self, "relu.s")
        array0 = t.array([0,0,0,0,0])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("relu")
        t.check_array(array0, [0,0,0,0,0])
        t.execute()
        
    def test_six(self):
        # Test for a simple 1 up to 9 within the array
        t = AssemblyTest(self, "relu.s")
        array0 = t.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("relu")
        t.check_array(array0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        t.execute()

    def test_seven(self):
        # Test mix of positive, negative, and zero numbers.
        t = AssemblyTest(self, "relu.s")
        array0 = t.array([1, -2, 3, -4, 5, -6, 7, -8, 9,-10,-11,12,13,0,-14])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("relu")
        t.check_array(array0, [1, 0, 3, 0, 5, 0, 7, 0, 9,0,0,12,13,0,0])
        t.execute()
        
    def test_edge(self):
        # Edge case test for an empty array
        t = AssemblyTest(self, "relu.s")
        array0 = t.array([])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("relu")
        t.execute(code=78)

    def test_eight(self):
        # Test mix of large negative and positive numbers
        t = AssemblyTest(self, "relu.s")
        array0 = t.array([1234567891,-111112233,-99123456,-10,5000000,30509840, 0])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("relu")
        t.check_array(array0, [1234567891, 0,0,0,5000000,30509840,0])
        t.execute()

    def test_nine(self):
        # Test for -999 within array.
        t = AssemblyTest(self, "relu.s")
        array0 = t.array([-999])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("relu")
        t.check_array(array0, [0])
        t.execute()
    def test_ten(self):
        # Test for negative array.
        t = AssemblyTest(self, "relu.s")
        array0 = t.array([-9,-10,-11])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("relu")
        t.check_array(array0, [0,0,0])
        t.execute()

    @classmethod
    def tearDownClass(cls):
        print_coverage("relu.s", verbose=False)


class TestArgmax(TestCase):
    def test_simple(self):
        # Test for mix of negative and positive numbers.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 8)
        t.execute()
       
    def test_one(self):
        # Test for single element of 0.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([0])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 0)
        t.execute()
        
    def test_two(self):
        # Test for mix of negative and zero.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([0,-2])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 0)
        t.execute()
        
    def test_three(self):
        # Test for mix of negative, positive and zero.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([0,-2,1])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 2)
        t.execute()
        
    def test_four(self):
        # Large test for mix of negative, positive, and zero.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([0,-1,1,-2,2,-3,3,-4,4,-5,5])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 10)
        t.execute()
    def test_five(self):
        # Test for repetitive values.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([1,1,1,1,1])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 0)
        t.execute()
    def test_six(self):
        # Test for single negative element.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([-20])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 0)
        t.execute()
    def test_seven(self):
        # Test for large mix of negative and positive numbers.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([-3000,4000,5000,-6000])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 2)
        t.execute()
    def test_eight(self):
        # Test for close large values.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([100,110])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 1)
        t.execute()
    def test_nine(self):
        # Test for close low values.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([-100,-110])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 0)
        t.execute()
    def test_ten(self):
        # Test for repetitive negative numbers.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([-100,-100])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 0)
        t.execute()
    def test_eleven(self):
        # Test for single large element.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([45000])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 0)
        t.execute()
    def test_twelve(self):
        # Test for large array of zeros.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([0,0,0,0,0,0,0,0,0])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 0)
        t.execute()

    def test_thirteen(self):
        # Test for two negative elements.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([-2,-1])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.check_scalar("a0", 1)
        t.execute()

    def test_edge(self):
        # Edge case for empty array. Should return error code 77.
        t = AssemblyTest(self, "argmax.s")
        array0 = t.array([])
        t.input_array("a0", array0)
        t.input_scalar("a1", len(array0))
        t.call("argmax")
        t.execute(77)
        
    @classmethod
    def tearDownClass(cls):
        print_coverage("argmax.s", verbose=False)


class TestDot(TestCase):
    def test_simple(self):
        # Test for simple input mix of positive and negative numbers.
        t = AssemblyTest(self, "dot.s")
        array0 = t.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
        array1 = t.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", len(array0))
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 1)
        t.call("dot")
        t.check_scalar("a0", 285)
        t.execute()
    def test_stride(self):
        # Test for positive elements with different strides of 1 and 2.
        t = AssemblyTest(self, "dot.s")
        array0 = t.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        array1 = t.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", 3)
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 2)
        t.call("dot")
        t.check_scalar("a0", 22)
        t.execute()

    def test_edge1(self):
        # Edge case where length is 0, should return error code 75.
        t = AssemblyTest(self, "dot.s")
        array0 = t.array([-1, 2, -3, 4, -5, 6, -7, 8, -9])
        array1 = t.array([-1, 2, -3, 4, -5, 6, -7, 8, -9])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", 0)
        t.input_scalar("a3", 5)
        t.input_scalar("a4", 2)
        t.call("dot")
        t.execute(75)

    def test_one(self):
        # Test for large mix of negative and positive numbers with large size, different strides.
        t = AssemblyTest(self, "dot.s")
        array0 = t.array([-2, 4, 7, 11, -13, 15, -19, 22, 24, 15])
        array1 = t.array([-1, 3, 8, -10, 14, 16, -17, 20, -21, 55, 177])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", 4)
        t.input_scalar("a3", 3)
        t.input_scalar("a4", 2)
        t.call("dot")
        t.check_scalar("a0", -431)
        t.execute()

    def test_edge2(self):
        # Edge case test where one of the strides is less than 1.
        t = AssemblyTest(self, "dot.s")
        array0 = t.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
        array1 = t.array([1, -2, 3, -4, 5, -6, 7, -8, 9])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", 4)
        t.input_scalar("a3", 0)
        t.input_scalar("a4", 2)
        t.call("dot")
        t.execute(76)

    def test_two(self):
        # Test for large mix of negative and positive numbers.
        t = AssemblyTest(self, "dot.s")
        array0 = t.array([45, -886, 123, 9950, 1230, 5 , 1 ,24])
        array1 = t.array([4, -6001,430032,9902,-2405,5004, -294, 201])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", 1)
        t.input_scalar("a3", 3)
        t.input_scalar("a4", 5)
        t.call("dot")
        t.check_scalar("a0", 180)
        t.execute()

    def test_three(self):
        # Test for single element in array.
        t = AssemblyTest(self, "dot.s")
        array0 = t.array([72])
        array1 = t.array([2])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", 1)
        t.input_scalar("a3", 1)
        t.input_scalar("a4", 1)
        t.call("dot")
        t.check_scalar("a0", 144)
        t.execute()

    def test_four(self):
        # Test for simple input with different strides.
        t = AssemblyTest(self, "dot.s")
        array0 = t.array([10,11,12,13,14])
        array1 = t.array([1, 2, 3, 4, 5])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", 2)
        t.input_scalar("a3", 2)
        t.input_scalar("a4", 3)
        t.call("dot")
        t.check_scalar("a0", 58)
        t.execute()

    def test_five(self):
        # Test for large array with length of 3.
        t = AssemblyTest(self, "dot.s")
        array0 = t.array([2,3,5,7,11,13,17,23,29,31])
        array1 = t.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", 3)
        t.input_scalar("a3", 2)
        t.input_scalar("a4", 3)
        t.call("dot")
        t.check_scalar("a0", 198)
        t.execute()

    def test_six(self):
        # Test for large mix of negative, positive numbers with large difference in strides.
        t = AssemblyTest(self, "dot.s")
        array0 = t.array([25, -2, 3, 4, 5, 6, 7, 8, 9, -2, 45, 10])
        array1 = t.array([1, 2, 3, -4, 0, 12, 7, 8, 9])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", 3)
        t.input_scalar("a3", 4)
        t.input_scalar("a4", 2)
        t.call("dot")
        t.check_scalar("a0", 40)
        t.execute()

    def test_seven(self):
        # Test for large array with large positive numbers, but with a 0 stride for m1. Should return error 76.
        t = AssemblyTest(self, "dot.s")
        array0 = t.array([230, 2123, 343, 648, 653, 9996, 91207, 8312, 9123])
        array1 = t.array([132, 265, 873, 479, 650, 2126, 12347, 5698, 9333])
        t.input_array("a0", array0)
        t.input_array("a1", array1)
        t.input_scalar("a2", 5)
        t.input_scalar("a3", 3)
        t.input_scalar("a4", 0)
        t.call("dot")
        t.execute(76)

    @classmethod
    def tearDownClass(cls):
        print_coverage("dot.s", verbose=False)


class TestMatmul(TestCase):

    def do_matmul(self, m0, m0_rows, m0_cols, m1, m1_rows, m1_cols, result, code=0):
        t = AssemblyTest(self, "matmul.s")
        # we need to include (aka import) the dot.s file since it is used by matmul.s
        t.include("dot.s")
        # create arrays for the arguments and to store the result
        array0 = t.array(m0)
        array1 = t.array(m1)
        array_out = t.array([0] * len(result))
        t.input_array("a0", array0)
        t.input_scalar("a1", m0_rows)
        t.input_scalar("a2", m0_cols)
        t.input_array("a3", array1)
        t.input_scalar("a4", m1_rows)
        t.input_scalar("a5", m1_cols)
        t.input_array("a6", array_out) # Sets arrays, values,etc. within the given registers.
        t.call("matmul") # Calls matmul.
        t.check_array(array_out,result)
        t.execute(code=code) # Executes with a certain code

    def test_simple(self):
        # Test for square 3x3 matrices with simple numbers.
        self.do_matmul(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3,
            [1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3,
            [30, 36, 42, 66, 81, 96, 102, 126, 150]
        )

    def test_one(self):
        # Test for non-square matrices with simple numbers.
        self.do_matmul(
            [1, 2, 3, 4, 5, 6], 2, 3,
            [10,11,20,21,30,31], 3, 2,
            [140,146,320,335]
        )

    def test_two(self):
        # Test for non-square matrices with simple positive, negative, and zero numbers.
        self.do_matmul(
            [2,1,4,0,1,1], 2, 3,
            [6,3,-1,0,1,1,0,4,-2,5,0,2], 3, 4,
            [5,27,-2,12,-1,6,0,6]
        )

    def test_three(self):
        # More tests with different dimensions.
        self.do_matmul(
            [4,0,-2,1,-1,2,0,3], 2, 4,
            [3,-2,1,1,1,0,1,0,-2,0,6,2], 4, 3,
            [10,-2,10,-1,22,5]
        )
    def test_four(self):
        # Edge case with 1x1 matrices.
        self.do_matmul(
            [2], 1, 1,
            [5000], 1, 1,
            [10000]
        )

    def test_edge11(self):
        # Case where a column for m0 is less than 1, returns error 72.
        self.do_matmul(
            [35,55], -1, 2,
            [5000], 2, 1,
            [10000], 72
        )

    def test_edge12(self):
        # Case where a row for m0 is less than 1, returns error 72.
        self.do_matmul(
            [2,52,52], 1, -1,
            [5000], 1, 1,
            [10000], 72
        )

    def test_edge21(self):
        # Case where a column for m1 is less than 1, returns error 73.
        self.do_matmul(
            [35,55], 1, 2,
            [5000, 255, 25552], -1, 5,
            [10000], 73
        )

    def test_edge22(self):
        # Case where a row for m1 is less than 1, returns error 73.
        self.do_matmul(
            [2,52,52], 1, 3,
            [5000], 1, -1,
            [10000], 73
        )

    def test_edge31(self):
        # Case where column for m0 and row for m1 don't match, should return 74.
        self.do_matmul(
            [2], 3, 2,
            [5000], 3, 2,
            [10000], 74
        )

    def test_edge32(self):
        # Case where the columns of m0 are less than 1, returns error 72.
        self.do_matmul(
            [2], 1, 0,
            [5000], 1, 1,
            [10000], 72
        )

    def test_edge33(self):
        # Case where column for m0 and row for m1 don't match, should return 74.
        self.do_matmul(
            [2], 1, 2,
            [5000], 1, 1,
            [10000], 74 
        )

    @classmethod
    def tearDownClass(cls):
        print_coverage("matmul.s", verbose=False)


class TestReadMatrix(TestCase):

    def do_read_matrix(self, fail='', code=0):
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", "inputs/test_read_matrix/test_input.bin")

        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])
        # load the addresses to the output parameters into the argument registers
        t.input_array("a1", rows)
        t.input_array("a2", cols)
        # call the read_matrix function
        t.call("read_matrix")

        # check the output from the function
        t.check_array(rows,[3])
        t.check_array(cols,[3])
        t.check_array_pointer("a0",[1,2,3,4,5,6,7,8,9])
        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)

    def test_simple(self):
        self.do_read_matrix()
    def readmat(self,file,row,col,lst):
        #Function to easily repeat sample tests from input folders
        t = AssemblyTest(self, "read_matrix.s")
        # load address to the name of the input file into register a0
        t.input_read_filename("a0", file)
        # allocate space to hold the rows and cols output parameters
        rows = t.array([-1])
        cols = t.array([-1])
        # load the addresses to the output parameters into the argument registers
        t.input_array("a1", rows)
        t.input_array("a2", cols)
        # call the read_matrix function
        t.call("read_matrix")
        # check the output from the function
        t.check_array(rows,[row])
        t.check_array(cols,[col])
        t.check_array_pointer("a0",lst)
        # generate assembly and run it through venus
        t.execute(code=0)

    # Repetitive tests below.
    def test1(self):
        self.readmat("inputs/simple2/bin/inputs/input0.bin",2,3,[1,12,4,2,-3,-3]);
    def test2(self):
        self.readmat("inputs/simple2/bin/inputs/input1.bin",2,2,[1,3,3,-1]);
    def test3(self):
        self.readmat("inputs/simple2/bin/inputs/input2.bin",2,5,[51,3,1,-3,4,-12,2,21,-1,34]);
    def test4(self):
        self.readmat("inputs/simple2/bin/m0.bin",4,2,[11,-10,13,10,-23,-6,-22,10]);
    def test5(self):
        self.readmat("inputs/simple2/bin/m1.bin",3,4,[34,-14,63,15,12,-5,-25,-63,14,36,-8,25]);
    def test6(self):
        self.readmat("inputs/simple1/bin/inputs/input0.bin",4,1,[1,2,3,4]);
    def test7(self):
        self.readmat("inputs/simple1/bin/inputs/input1.bin",4,1,[3,-1,4,-6]);
    def test8(self):
        self.readmat("inputs/simple1/bin/inputs/input2.bin",4,1,[1,-2,-3,4]);
    def test9(self):
        self.readmat("inputs/simple1/bin/m0.bin",3,4,[-1,-2,3,4,-5,6,-7,8,9,-10,11,-12]);
    def test10(self):
        self.readmat("inputs/simple1/bin/m1.bin",5,3,[1,-3,4,46,-2,-5,2,-62,0,1,3,13,26,-7,34]);
    def test11(self):
        self.readmat("inputs/simple0/bin/inputs/input0.bin",3,1,[1,1,1]);
    def test12(self):
        self.readmat("inputs/simple0/bin/inputs/input1.bin",3,1,[1,2,3]);
    def test13(self):
        self.readmat("inputs/simple0/bin/inputs/input2.bin",3,1,[2,1,6]);
    def test14(self):
        self.readmat("inputs/simple0/bin/m0.bin",3,3,[1,2,3,4,5,6,7,8,9]);
    def test15(self):
        self.readmat("inputs/simple0/bin/m1.bin",3,3,[1,3,5,7,9,11,13,15,17]);

    def testerror1(self):
        # Testing Malloc Errors
        self.do_read_matrix(fail="malloc", code=88)
    def testerror2(self):
        # Testing fopen Errors
        self.do_read_matrix(fail="fopen", code=90)
    def testerror3(self):
        # Testing fread Errors
        self.do_read_matrix(fail="fread", code=91)
    def testerror4(self):
        # Testing fclose Errors
        self.do_read_matrix(fail="fclose", code=92)

    @classmethod
    def tearDownClass(cls):
        print_coverage("read_matrix.s", verbose=False)


class TestWriteMatrix(TestCase):

    def do_write_matrix(self, fail='', code=0):
        t = AssemblyTest(self, "write_matrix.s")
        outfile = "outputs/test_write_matrix/student.bin"
        # load output file name into a0 register
        t.input_write_filename("a0", outfile)
        # load input array and other arguments
        mat = t.array([1,2,3,4,5,6,7,8,9])
        t.input_array("a1", mat)
        t.input_scalar("a2", 3)
        t.input_scalar("a3", 3)
        # call `write_matrix` function
        t.call("write_matrix")
        # generate assembly and run it through venus
        t.execute(fail=fail, code=code)
        # compare the output file against the reference
        if not fail:
            # Check for output if there is no failing option available.
            t.check_file_output(outfile, "outputs/test_write_matrix/reference.bin")
    def writemat(self,inputval,outputval,row,col,lst):
        # Summary code for different input tests below.
        t = AssemblyTest(self, "write_matrix.s")
        outfile = outputval
        # load output file name into a0 register
        t.input_write_filename("a0", outfile)
        # load input array and other arguments
        mat = t.array(lst)
        t.input_array("a1", mat)
        t.input_scalar("a2", row)
        t.input_scalar("a3", col)
        # call `write_matrix` function
        t.call("write_matrix")
        # generate assembly and run it through venus
        t.execute(code=0)
        # compare the output file against the reference
        t.check_file_output(outfile, inputval)     
    # Sample tests below   
    def test_simple(self):
        self.do_write_matrix()
    def test1(self):
        self.writemat("inputs/simple0/bin/m1.bin", "outputs/test_write_matrix/simple0_M1.bin",3,3,[1,3,5,7,9,11,13,15,17]);
    def test2(self):
        self.writemat("inputs/simple1/bin/m1.bin","outputs/test_write_matrix/simple1_M1.bin",5,3,[1,-3,4,46,-2,-5,2,-62,0,1,3,13,26,-7,34]);
    def test3(self):
        self.writemat("inputs/simple2/bin/m0.bin","outputs/test_write_matrix/simple2_M0.bin",4,2,[11,-10,13,10,-23,-6,-22,10]);
    def test4(self):
        self.writemat("inputs/simple2/bin/m1.bin","outputs/test_write_matrix/simple2_M1.bin",3,4,[34,-14,63,15,12,-5,-25,-63,14,36,-8,25]);
    def testerror1(self):
        # Test to check fopen error
        self.do_write_matrix(fail="fopen", code=93)
    def testerror2(self):
        # Test to check fwrite error
        self.do_write_matrix(fail="fwrite", code=94)
    def testerror3(self):
        # Test to check fclose error
        self.do_write_matrix(fail="fclose", code=95)

    @classmethod
    def tearDownClass(cls):
        print_coverage("write_matrix.s", verbose=False)


class TestClassify(TestCase):

    def make_test(self):
        t = AssemblyTest(self, "classify.s")
        t.include("argmax.s")
        t.include("dot.s")
        t.include("matmul.s")
        t.include("read_matrix.s")
        t.include("relu.s")
        t.include("write_matrix.s")
        return t

    def test1(self):
        # Test for input0
        t = self.make_test()
        # Set args
        out_file = "outputs/test_mnist_main/student_input_mnist_output.bin"
        args = ["inputs/mnist/bin/m0.bin","inputs/mnist/bin/m1.bin","inputs/mnist/bin/inputs/mnist_input0.bin","outputs/test_mnist_main/student_mnist_output.bin"]
        # Sets to print out value
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, verbose=False)
        # Check for the output value
        t.check_stdout("6")

    def test2(self):
        # Test for input1
        t = self.make_test()
        # Set args
        out_file = "outputs/test_mnist_main/student_input_mnist_output.bin"
        args = ["inputs/mnist/bin/m0.bin","inputs/mnist/bin/m1.bin","inputs/mnist/bin/inputs/mnist_input1.bin","outputs/test_mnist_main/student_mnist_output.bin"]
        # Sets to print out value
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, verbose=False)
        # Check for the output value
        t.check_stdout("9")

    def test3(self):
        # Test for input2
        t = self.make_test()
        # Set args
        out_file = "outputs/test_mnist_main/student_input_mnist_output.bin"
        args = ["inputs/mnist/bin/m0.bin","inputs/mnist/bin/m1.bin","inputs/mnist/bin/inputs/mnist_input2.bin","outputs/test_mnist_main/student_mnist_output.bin"]
        # Sets to print out value
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, verbose=False)
        # Check for the output value
        t.check_stdout("7")

    def test4(self):
        # Test for input3
        t = self.make_test()
        # Set args
        out_file = "outputs/test_mnist_main/student_input_mnist_output.bin"
        args = ["inputs/mnist/bin/m0.bin","inputs/mnist/bin/m1.bin","inputs/mnist/bin/inputs/mnist_input3.bin","outputs/test_mnist_main/student_mnist_output.bin"]
        # Sets to print out value
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, verbose=False)
        # Check for the output value
        t.check_stdout("2")

    def test5(self):
        # Test for input4
        t = self.make_test()
        # Set args
        out_file = "outputs/test_mnist_main/student_input_mnist_output.bin"
        args = ["inputs/mnist/bin/m0.bin","inputs/mnist/bin/m1.bin","inputs/mnist/bin/inputs/mnist_input4.bin","outputs/test_mnist_main/student_mnist_output.bin"]
        # Sets to print out value
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, verbose=False)
        # Check for the output value
        t.check_stdout("9")

    def test6(self):
        # Test for input5
        t = self.make_test()
        # Set args
        out_file = "outputs/test_mnist_main/student_input_mnist_output.bin"
        args = ["inputs/mnist/bin/m0.bin","inputs/mnist/bin/m1.bin","inputs/mnist/bin/inputs/mnist_input5.bin","outputs/test_mnist_main/student_mnist_output.bin"]
        # Sets to print out value
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, verbose=False)
        # Check for the output value
        t.check_stdout("4")

    def test7(self):
        # Test for input6
        t = self.make_test()
        # Set args
        out_file = "outputs/test_mnist_main/student_input_mnist_output.bin"
        args = ["inputs/mnist/bin/m0.bin","inputs/mnist/bin/m1.bin","inputs/mnist/bin/inputs/mnist_input6.bin","outputs/test_mnist_main/student_mnist_output.bin"]
        # Sets to print out value
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, verbose=False)
        # Check for the output value
        t.check_stdout("4")

    def test8(self):
        # Test for input7
        t = self.make_test()
        # Set args
        out_file = "outputs/test_mnist_main/student_input_mnist_output.bin"
        args = ["inputs/mnist/bin/m0.bin","inputs/mnist/bin/m1.bin","inputs/mnist/bin/inputs/mnist_input7.bin","outputs/test_mnist_main/student_mnist_output.bin"]
        # Sets to print out value
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, verbose=False)
        # Check for the output value
        t.check_stdout("2")

    def test9(self):
        # Test for input8
        t = self.make_test()
        # Set args
        out_file = "outputs/test_mnist_main/student_input_mnist_output.bin"
        args = ["inputs/mnist/bin/m0.bin","inputs/mnist/bin/m1.bin","inputs/mnist/bin/inputs/mnist_input8.bin","outputs/test_mnist_main/student_mnist_output.bin"]
        # Sets to print out value
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args, verbose=False)
        # Check for the output value
        t.check_stdout("7")

    def testerr1(self):
        # Test for Incorrect args
        t = self.make_test()
        # Set args
        out_file = "outputs/test_basic_main/mnist0.bin"
        ref_file = "outputs/test_basic_main/reference0.bin"
        args = ["inputs/mnist/bin/m0.bin", "inputs/mnist/bin/m1.bin",
                "inputs/mnist/bin/inputs/mnist_input0.bin"]
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args,code=89)

    def testerr2(self):
        # Test for Incorrect args
        t = self.make_test()
        # Set args
        out_file = "outputs/test_basic_main/mnist0.bin"
        ref_file = "outputs/test_basic_main/reference0.bin"
        args = ["inputs/mnist/bin/m0.bin", "inputs/mnist/bin/m1.bin",
                "inputs/mnist/bin/inputs/mnist_input0.bin",out_file,ref_file]
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args,code=89)

    def testerror3(self):
        # Test for Malloc errors
        t = self.make_test()
        # Set args
        out_file = "tests/outputs/test_mnist_main/student_input_mnist_output.bin"
        ref_file = "outputs/test_basic_main/reference0.bin"
        args = ["inputs/mnist/bin/m0.bin", "inputs/mnist/bin/m1.bin",
                "inputs/mnist/bin/inputs/mnist_input0.bin",out_file]
        t.input_scalar("a2",0)
        # call classify function
        t.call("classify")
        # generate assembly and pass program arguments directly to venus
        t.execute(args=args,fail='malloc',code=88)

    @classmethod
    def tearDownClass(cls):
        print_coverage("classify.s", verbose=False)


class TestMain(TestCase):

    def run_main(self, inputs, output_id, label):
        args = [f"{inputs}/m0.bin", f"{inputs}/m1.bin", f"{inputs}/inputs/input0.bin",
                f"outputs/test_basic_main/student{output_id}.bin"]
        reference = f"outputs/test_basic_main/reference{output_id}.bin"
        t = AssemblyTest(self, "main.s", no_utils=True)
        t.call("main")
        t.execute(args=args, verbose=False)
        t.check_stdout(label)
        t.check_file_output(args[-1], reference)

    def test0(self):
        # Run test with simple0 directory
        self.run_main("inputs/simple0/bin", "0", "2")

    def test1(self):
        # Run test with simple1 directory
        self.run_main("inputs/simple1/bin", "1", "1")

    def test2(self):
        # Run test with simple2 directory
        self.run_main("inputs/simple2/bin", "2", "7")
