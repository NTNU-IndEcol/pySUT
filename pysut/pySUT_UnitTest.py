# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 16:19:39 2014

@author: Stefan Pauliuk, NTNU
"""

import numpy as np
import numpy.testing as npt
# import pylab
from pySUT import SUT
import unittest

###############################################################################
"""Input for SUT test"""

Y_Test = np.array([11,4,3,0,5])

V_Test = np.array([ [30,1,1,1,0],
                    [1,5,1,0,0],
                    [2,0,3,1,0],
                    [0,0,1,0,0],
                    [0,0,0,0,8]])

U_Test = np.array([ [12,4,5,1,0],
                    [1,1,1,0,0],
                    [0,1,1,1,0],
                    [1,0,0,0,0],
                    [0,1,1,1,0]])               
                    
F_Test = np.array([ [30,5,18,22.03,7],
                    [0.4,0.04,1,0.98,0.8]])   
                    
"""Output from SUT test"""                    
IndSupply_Use = np.array([0.666666667,0.428571429,0.5,1,0.375])

SupplyDiag = np.array([[1,	0,	0,	0,	0,	33,	33],
                    [1,	0,	0,	0,	0,	7,	6],
                    [1,	0,	0,	0,	0,	6,	6],
                    [0,	1,	0,	0,	0,	1,	2],
                    [1,	0,	0,	0,	0,	8,	8]])

g_V = np.array([33,6,6,2,8])
q_V = np.array([33,7,6,1,8])
m_b = np.array([0,0,0,0,0])

# after removing non-diag products:
V_Test2 = np.array([ [30,1,1,0,0],
                     [1,5,1,0,0],
                     [2,0,3,0,0],
                     [0,0,1,0,0],
                     [0,0,0,0,8]])

U_Test2 = np.array([ [12,4,5,0,0],
                     [1,1,1,0,0],
                     [0,1,1,0,0],
                     [1,0,0,0,0],
                     [0,1,1,0,0]])      
                     
V_New   = np.array([ [30,1,1,0,0],
                     [1,5,1,0,0],
                     [2,0,3,0,0],
                     [0,0,1,1,0],
                     [0,0,0,0,8]])                     
                            
V_NewD  = np.array([ [30,0,0,0,0],
                     [0,5,0,0,0],
                     [0,0,3,0,0],
                     [0,0,0,1,0],
                     [0,0,0,0,8]])  

V_NewOD = np.array([ [0,1,1,0,0],
                     [1,0,1,0,0],
                     [2,0,0,0,0],
                     [0,0,1,0,0],
                     [0,0,0,0,0]])  

# Test constructs:
                     
A_BTC   = np.array([ [0.4,	0.6,	1.333333333,	0,	0],
                    [0,	0.2,	0,	0,	0],
                    [-0.066666667,	0.2,	0.333333333,	0,	0],
                    [0.033333333,	0,	-0.333333333,	0,	0],
                    [0,	0.2,	0.333333333,	0,	0]])


Am_BTC   = np.array([ [0.4,	0.8,	1.666666667,	0,	0],
                    [0.033333333,	0.2,	0.333333333,	0,	0],
                    [0,	0.2,	0.333333333,	0,	0],
                    [0.033333333,	0,	0,	0,	0],
                    [0,	0.2,	0.333333333,	0,	0]])


Ab_BTC   = np.array([ [0,	0.2,	0.333333333,	0,	0],
                    [0.033333333,	0,	0.333333333,	0,	0],
                    [0.066666667,	0,	0,	0,	0],
                    [0,	0,	0.333333333,	0,	0],
                    [0,	0,	0,	0,	0]])

S_BTC   = np.array([ [1,	1,	6,	22.03,	0.875],
                     [0.013333333,	0.008,	0.333333333,	0.98,	0.1]])
                     
A_CTC_cxc = np.array([ [0.287015945,	0.742596811,	1.323462415,	0,	0],
                        [0.009111617,	0.198177677,	0.264236902,	0,	0],
                        [-0.025056948,	0.20501139,	     0.273348519,	0,	0],
                        [0.034168565,	-0.006833713,	-0.009111617,	0,	0],
                        [-0.025056948,	0.20501139,	    0.273348519,	0,	0]])

A_CTC_ixi = np.array([ [0.403189066,	0.664009112,	0.851936219,	0,	0],
                        [0.031476496,	0.125284738,	0.123006834,	0,	0],
                        [-0.048871402,	0.25284738,  	0.230068337,	0,	0],
                        [0.038448264,	-0.04214123,	-0.038344723,	0,	0],
                        [0,	0.166666667,	0.166666667,	0,	0]])


S_CTC   = np.array([ [1.10546697,	0.778906606,	-1.971457859,	22.03,	0.875],
                     [0.013120729,	0.005375854,	0.000501139,	0.98,	0.1]])
                 
A_ITC_cxc = np.array([ [0.387784091,	0.647186147,	0.645454545,	0.416666667,	0],
                        [0.038825758,	0.147186147,    0.112121212,	0.083333333,	0],
                        [0.010416667,	0.142857143,	0.1,	         0.083333333,	0],
                        [0.028409091,	0.004329004,	0.012121212,	0,	0],
                        [0.010416667,	0.142857143,	0.1,	         0.083333333,	0]])


A_ITC_ixi = np.array([ [0.345238095,	0.71547619,	0.87172619,	0,	0],
                       [0.033008658,	0.139880952,	0.145089286,	0,	0],
                       [0.030844156,	0.144642857,	0.14985119,	0,	0],
                       [0.015151515,	0,	0,	0,	0],
                       [0,	0.166666667,	0.166666667,	0,	0]])



S_ITC   = np.array([ [0.972064394,	1.153679654,	2.163636364,	12.515,	0.875],
                    [0.016780303,	0.03030303,	0.104848485,	0.573333333,	0.1]])
   
# Test aggregation of SUT:
Y_Testx = np.array([11,4,1,2,0,5])

V_Testx = np.array([ [30,1,1,1,0],
                    [1,5,1,0,0],
                    [1,0,2,0.5,0],
                    [1,0,1,0.5,0],
                    [0,0,1,0,0],
                    [0,0,0,0,8]])

U_Testx = np.array([ [12,4,5,1,0],
                    [1,1,1,0,0],
                    [0.5,0,1,0,1],
                    [0,0,0.5,0,0],
                    [1,0,0,0,0],
                    [0,1,1,1,0]])               
                    
F_Testx = np.array([ [30,5,18,22.03,7],
                     [0.4,0.04,1,0.98,0.8]])    
   
PA     = np.array([ [1,0,0,0,0,0],
                    [0,1,0,0,0,0],
                    [0,0,1,1,0,0],
                    [0,0,0,0,1,0],
                    [0,0,0,0,0,1]])              

PR     = np.array([ [0,1,0,0,0],
                    [1,0,0,0,0],
                    [0,0,0,0,1],
                    [0,0,0,1,0],
                    [0,0,1,0,0]])      

# Aggregate first, but do not resort                    
U_agg = np.array([ [12,4,5,1,0],
                    [1,1,1,0,0],
                    [0.5,0,1.5,0,1],
                    [1,0,0,0,0],
                    [0,1,1,1,0]])                      
                    
V_agg = np.array([ [30,1,1,1,0],
                    [1,5,1,0,0],
                    [2,0,3,1,0],
                    [0,0,1,0,0],
                    [0,0,0,0,8]])  
                    
Y_agg = np.array([11,4,3,0,5])                    

# resort in a second step:
U_res = np.array([ [1,1,0,0,1],
                    [4,12,0,1,5],
                    [1,0,0,1,1],
                    [0,1,0,0,0],
                    [0,0.5,1,0,1.5]])                      
                    
V_res = np.array([ [5,1,0,0,1],
                    [1,30,0,1,1],
                    [0,0,8,0,0],
                    [0,0,0,0,1],
                    [0,2,0,1,3]])  
                    
Y_res = np.array([4,11,5,0,3])

F_res = np.array([ [5,30,7,22.03,18],
                     [0.04,0.4,0.8,0.98,1]]) 
              
###############################################################################
"""Create Dynamic Stock Models and hand over the pre-defined values."""
# For fixed LT
mySUT  = SUT(V = V_Test.copy(), U = U_Test.copy(), Y = Y_Test.copy(), F = F_Test.copy())

mySUT2 = SUT(V = V_Test.copy(), U = U_Test.copy(), Y = Y_Test.copy(), F = F_Test.copy())
mySUT2.clear_non_diag_supply()

mySUT3 = SUT(V = V_Test.copy(), U = U_Test.copy(), Y = Y_Test.copy(), F = F_Test.copy())
mySUT3.clear_non_diag_supply()
mySUT3.add_ones_to_diagonal()

mySUT4 = SUT(V = V_Testx.copy(), U = U_Testx.copy(), Y = Y_Testx.copy(), F = F_Testx.copy())
mySUT4.aggregate_rearrange_products(PA,np.eye(5))

mySUT5 = SUT(V = V_Testx.copy(), U = U_Testx.copy(), Y = Y_Testx.copy(), F = F_Testx.copy())
mySUT5.aggregate_rearrange_products(PA,PR)
###############################################################################
"""Unit Test Class"""
class KnownResults(unittest.TestCase):    
    def setUp(self):
        # Case 0: 3 regions, 2 industries, 2 products (square) 
        self.V_3r2i2p = np.array(
                      #I   J     I   J       I   J
                     [[9., 0.,   0., 0.,     0., 0.],    # i
                      [3., 3.,   0., 0.,     0., 0.],    # j
                                                         #
                      [0., 0.,   4., 4.,     0., 0.],    # i
                      [0., 0.,   0., 0.,     0., 0.],    # j  <-- no production
                                                         #
                      [0., 0.,   0., 0.,     2., 0.],    # i
                      [0., 0.,   0., 0.,     1., 2.]])   # j
                     #               ^
                     #               |
                     #               "Fake J", does not produce j, prim prod i

        self.E_bar_3r2i2p = np.array(
                         [[1, 0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0, 0],
                          [0, 0, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 0, 1]])

        # Case 1: 3 regions, 2 industries, 2 products:
        #--------------------------------------------

        self.Vmr = np.array([
                         #   Ca   Ca     No   No     US   US
                         #   I    J      I    J      I    J
                         [   4.,  0.,    0.,  0.,    0.,  0.,  ],     #i  Ca
                         [   0.,  0.,    0.,  0.,    0.,  0.,  ],     #j  Ca
                         [   0.,  3.,    0.,  0.,    0.,  0.,  ],     #k  Ca
                         #
                         [   0.,  0.,    0.,  0.,    0.,  0.,  ],     #i  No
                         [   0.,  0.,    3.,  0.,    0.,  0.,  ],     #j  No
                         [   0.,  0.,    0.,  0.,    0.,  0.,  ],     #k  No
                         #
                         [   0.,  0.,    0.,  0.,    8.,  0.,  ],     #i  US
                         [   0.,  0.,    0.,  0.,    0.,  0.,  ],     #j  US
                         [   0.,  0.,    0.,  0.,    0.,  9.,  ]])    #k  US

    def test_SUT_balances(self):
        """Test simple balances of SUT"""
        np.testing.assert_array_almost_equal(mySUT.compare_IndustrialUseAndSupply(),IndSupply_Use,9)
        np.testing.assert_array_equal(mySUT.supply_diag_check(),SupplyDiag)
        np.testing.assert_array_equal(mySUT.g_V(),g_V)
        np.testing.assert_array_equal(mySUT.q_V(),q_V)
        np.testing.assert_array_equal(mySUT.market_balance(),m_b)

    def test_SUT_product_removal(self):
        """Test whether certain products and industries are correctly removed from the SUT."""
        np.testing.assert_array_equal(mySUT2.V,V_Test2)        
        np.testing.assert_array_equal(mySUT2.U,U_Test2)        
        
    def test_V_diagonal(self):
        """Test whether the supply table is correctly adjusted."""
        np.testing.assert_array_equal(mySUT3.V,V_New)   
        np.testing.assert_array_equal(mySUT3.return_diag_V(),V_NewD)   
        np.testing.assert_array_equal(mySUT3.return_offdiag_V(),V_NewOD)     
        
    def test_BTC_construct(self):
        """Test the A and S matrices for the BTC construct."""
        np.testing.assert_array_almost_equal(mySUT3.Build_BTC_A_matrix(),A_BTC,8) 
        np.testing.assert_array_almost_equal(mySUT3.Build_BTC_Am_matrix(),Am_BTC,8) 
        np.testing.assert_array_almost_equal(mySUT3.Build_BTC_Ab_matrix(),Ab_BTC,8)         
        np.testing.assert_array_almost_equal(mySUT3.Build_BTC_S(),S_BTC,9) 
        
    def test_CTC_construct(self):
        """Test the A and S matrices for the CTC construct."""
        np.testing.assert_array_almost_equal(mySUT3.Build_CTC_A_matrix_cxc(),A_CTC_cxc,8) 
        np.testing.assert_array_almost_equal(mySUT3.Build_CTC_A_matrix_ixi(),A_CTC_ixi,8) 
        np.testing.assert_array_almost_equal(mySUT3.Build_CTC_cxc_S(),S_CTC,9) 
        
    def test_ITC_construct(self):
        """Test the A and S matrices for the CTC construct."""
        np.testing.assert_array_almost_equal(mySUT3.Build_ITC_A_matrix_cxc(),A_ITC_cxc,8) 
        np.testing.assert_array_almost_equal(mySUT3.Build_ITC_A_matrix_ixi(),A_ITC_ixi,8) 
        np.testing.assert_array_almost_equal(mySUT3.Build_ITC_cxc_S(),S_ITC,9)         

    def test_aggregation(self):
        np.testing.assert_array_equal(mySUT4.U,U_agg)   
        np.testing.assert_array_equal(mySUT4.V,V_agg)   
        np.testing.assert_array_equal(mySUT4.Y,Y_agg)   
        
    def test_aggregation_resort(self):
        np.testing.assert_array_equal(mySUT5.U,U_res)   
        np.testing.assert_array_equal(mySUT5.V,V_res)   
        np.testing.assert_array_equal(mySUT5.Y,Y_res)         
        np.testing.assert_array_equal(mySUT5.F,F_res)         

    def test_generate_mainproduct_matrix_simpleExclusiveProd(self):

        V = np.array([[1.4, 0, 0,  12],
                      [5.,  3, 6., 0],
                      [0,   0, 0,  0.1],
                      [0,   0, 0,  0]])
        sut = SUT(V=V)
        sut.generate_mainproduct_matrix()
        E_bar0 = np.array([[1, 0, 0, 0],
                           [0, 1, 1, 0],
                           [0, 0, 0, 1],
                           [0, 0, 0, 0]])
        npt.assert_array_equal(E_bar0, sut.E_bar)

        sut.generate_mainproduct_matrix(prefer_exclusive=False)
        E_bar0 = np.array([[1, 0, 0, 1],
                           [0, 1, 1, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0]])
        npt.assert_array_equal(E_bar0, sut.E_bar)


    def test_generate_mainproduct_matrix_notsquare(self):

        V = np.array([[1.4, 0, 0,  12,  0],
                      [5.,  3, 6., 0,   0],
                      [0,   0, 0,  0.1, 0],
                      [0,   0, 0,  0,   0]])
        sut = SUT(V=V)

        sut.generate_mainproduct_matrix()
        E_bar0 = np.array([[0, 0, 0, 0, 0],
                           [1, 1, 1, 0, 0],
                           [0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 0]])
        npt.assert_array_equal(E_bar0, sut.E_bar)

        sut.generate_mainproduct_matrix(prefer_exclusive=False)
        E_bar0 = np.array([[0, 0, 0, 1, 0],
                           [1, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]])
        npt.assert_array_equal(E_bar0, sut.E_bar)

    def test_generate_mainproduct_matrix_multipleExclusive(self):

        V = np.array([[1.4, 0, 0,  12,  0],
                      [5.,  3, 6., 0,   0],
                      [0,   0, 0,  0.1, 0],
                      [0,   0, 0,  0,   0],
                      [0,   0, 0,  0.2, 0]])
        sut = SUT(V=V)

        sut.generate_mainproduct_matrix()
        E_bar0 = np.array([[1, 0, 0, 0, 0],
                           [0, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0]])
        npt.assert_array_equal(E_bar0, sut.E_bar)

        sut.generate_mainproduct_matrix(prefer_exclusive=False)
        E_bar0 = np.array([[1, 0, 0, 1, 0],
                           [0, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]])
        npt.assert_array_equal(E_bar0, sut.E_bar)

    def test_generate_mainproduct_matrix_negatives(self):

        # native value, should not alter results
        V = np.array([[1.4, 0, 0,  12,   0],
                      [5.,  3, 6., 0,    0],
                      [0,   0, 0,  0.1,  0],
                      [0,   0, 0,  0,    0],
                      [0,   0, 0,  -0.2, 0]])
        sut = SUT(V=V)

        sut.generate_mainproduct_matrix()
        E_bar0 = np.array([[1, 0, 0, 0, 0],
                           [0, 1, 1, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0]])
        npt.assert_array_equal(E_bar0, sut.E_bar)


    def test_V_bar_tilde(self):

        # Initialize sut
        V = np.array([[1.4, 0, 0,  12],
                      [5.,  3, 6., 0],
                      [0,   0, 0,  0.1],
                      [0,   0, 0,  0]])
        E_bar = np.array([[1, 0, 0, 0],
                          [0, 1, 1, 0],
                          [0, 0, 0, 1],
                          [0, 0, 0, 0]])
        sut = SUT(V=V, E_bar=E_bar)

        # Test V_bar: primary supply flows only
        V0 = np.array([[1.4, 0, 0,  0],
                       [0.,  3, 6., 0],
                       [0,   0, 0,  0.1],
                       [0,   0, 0,  0]])
        npt.assert_array_equal(V0, sut.V_bar())

        # Test V_tild: secondary supply flows only
        V0 = np.array([[0,   0, 0,  12],
                       [5.,  0, 0,  0],
                       [0,   0, 0,  0],
                       [0,   0, 0,  0]])
        npt.assert_array_equal(V0, sut.V_tild())




    def test_aggregate_regions_vectorised_rowsAndColumns(self):
        U = np.arange(54).reshape((9,6))
        av = np.array([1,2,2])
        sut = SUT()

        Uout = sut._aggregate_regions_vectorised(U, av, axis=0)
        U0 = np.array([[ 0,  1,  2,  3,  4,  5],
                       [ 6,  7,  8,  9, 10, 11],
                       [12, 13, 14, 15, 16, 17],
                       [54, 56, 58, 60, 62, 64],
                       [66, 68, 70, 72, 74, 76],
                       [78, 80, 82, 84, 86, 88]])
        npt.assert_array_equal(U0, Uout)

        Uout = sut._aggregate_regions_vectorised(U, av, axis=1)
        U0 = np.array([[  0,   1,   6,   8],
                       [  6,   7,  18,  20],
                       [ 12,  13,  30,  32],
                       [ 18,  19,  42,  44],
                       [ 24,  25,  54,  56],
                       [ 30,  31,  66,  68],
                       [ 36,  37,  78,  80],
                       [ 42,  43,  90,  92],
                       [ 48,  49, 102, 104]])
        npt.assert_array_equal(U0, Uout)


    def test_aggregate_regions_vectorised_bothAxes(self):
        U = np.arange(54).reshape((9,6))
        av = np.array([1,2,2])
        sut = SUT()

        # Test aggregation of both axes
        Uout = sut._aggregate_regions_vectorised(U, av)
        U0 = np.array([[  0,   1,   6,   8],
                       [  6,   7,  18,  20],
                       [ 12,  13,  30,  32],
                       [ 54,  56, 120, 124],
                       [ 66,  68, 144, 148],
                       [ 78,  80, 168, 172]])
        npt.assert_array_equal(U0, Uout)

    def test_aggregation_within_regions(self):

        sut = SUT(U=np.arange(54).reshape((3*3, 3*2)), regions=3)

        Uout = sut.aggregate_within_regions(sut.U, axis=0)
        U0 = np.array([[  18.,   21.,   24.,   27.,   30.,   33.],
                       [  72.,   75.,   78.,   81.,   84.,   87.],
                       [ 126.,  129.,  132.,  135.,  138.,  141.]])
        npt.assert_array_equal(U0, Uout)


        Uout = sut.aggregate_within_regions(sut.U, axis=1)
        U1 = np.array([[   1.,    5.,    9.],
                       [  13.,   17.,   21.],
                       [  25.,   29.,   33.],
                       [  37.,   41.,   45.],
                       [  49.,   53.,   57.],
                       [  61.,   65.,   69.],
                       [  73.,   77.,   81.],
                       [  85.,   89.,   93.],
                       [  97.,  101.,  105.]])
        npt.assert_array_equal(U1, Uout)


        Uout = sut.aggregate_within_regions(sut.U)
        U2 = np.array([[  39.,   51.,   63.],
                       [ 147.,  159.,  171.],
                       [ 255.,  267.,  279.]])
        npt.assert_array_equal(U2, Uout)

    def test_primary_market_shares_of_regions(self):

        V = np.array([[10.,  0.,  0.,  0.1  ],
                      [0.,   20., 0.,  0.   ],
                      [0.,   0.,  5.,  10.  ],
                      [0.1,  0.,  0.,  0.   ]])

        E_bar = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 1],
                          [0, 0, 0, 0]])

        sut = SUT(V=V, E_bar=E_bar, regions=2)

        D = sut.primary_market_shares_of_regions()

        D0 = np.array([[ 0.4,  1. ],
                       [ 0.6,  0. ]])

        npt.assert_array_equal(D0,D)

    def test_generate_Xi_square3regions(self):

                        #i  j    i  j       i  j
        Xi0 = np.array([[1, 0,   0, 0,      0, 0],       #i
                        [0, 1,   0, 3/5,    0, 0],       #j
                                                         #
                        [0, 0,   1, 0,      0, 0],       #i
                        [0, 0,   0, 0,      0, 0],       #j
                                                         #
                        [0, 0,   0, 0,      1, 0],       #i
                        [0, 0,   0, 2/5,    0, 1]])      #j

        sut = SUT(V=self.V_3r2i2p, E_bar=self.E_bar_3r2i2p, regions=3)
        sut.multiregion_Xi()

        npt.assert_allclose(Xi0, sut.Xi)

    def test_generate_Gamma_square3regions(self):

        Gamma0 = np.array(
                        #i  j    i    j      i  j
                       [[1, 0,   0,   0,     0, 0],     # I
                        [0, 1,   0,   3/5,   0, 0],     # J
                                                        #
                        [0, 0,   0.5, 0,     0, 0],     # I
                        [0, 0,   0.5, 0,     0, 0],     # J
                                                        #
                        [0, 0,   0,   0,     1, 0],     # I
                        [0, 0,   0,   2/5,   0, 1]])    # J

        sut = SUT(V=self.V_3r2i2p, E_bar=self.E_bar_3r2i2p, regions=3)
        sut.build_multiregion_Gamma()

        npt.assert_allclose(Gamma0, sut.Gamma)






if __name__ == '__main__':
    unittest.main()
