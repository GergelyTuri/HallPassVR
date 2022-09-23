EESchema Schematic File Version 4
LIBS:position_controller-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Label 650  7500 2    50   ~ 0
Ac
Text Label 650  6900 2    50   ~ 0
An
Text Label 650  7000 2    50   ~ 0
Bc
Text Label 650  7600 2    50   ~ 0
Bn
$Comp
L 74xGxx:74LVC2G86 U13
U 1 1 5D152FB4
P 950 6950
F 0 "U13" V 1000 6900 50  0000 C CNN
F 1 "74_2G86" V 900 6950 50  0000 C CNN
F 2 "Housings_SSOP:VSSOP-8_3.0x3.0mm_Pitch0.65mm" H 950 6950 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 950 6950 50  0001 C CNN
F 4 "296-13274-1-ND" H 950 6950 50  0001 C CNN "digikey"
	1    950  6950
	1    0    0    -1  
$EndComp
Wire Wire Line
	1200 6650 1200 6950
Wire Wire Line
	1200 7550 1200 7700
Wire Wire Line
	1200 6650 2000 6650
Wire Wire Line
	1750 6950 1900 6950
Text Label 2600 7050 0    50   ~ 0
UP
Text Label 2600 7550 0    50   ~ 0
DOWN
$Comp
L 74xx:74LS193 U20
U 1 1 5D1871A8
P 6550 5400
F 0 "U20" V 6450 5400 50  0000 C CNN
F 1 "74_193" V 6550 5400 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 6550 5400 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS193" H 6550 5400 50  0001 C CNN
F 4 "1727-7974-1-ND" H 6550 5400 50  0001 C CNN "digikey"
	1    6550 5400
	1    0    0    -1  
$EndComp
$Comp
L 74xGxx:74LVC2G86 U13
U 2 1 5D15393D
P 950 7550
F 0 "U13" V 1000 7550 50  0000 C CNN
F 1 "74_2G86" V 900 7550 50  0000 C CNN
F 2 "Housings_SSOP:VSSOP-8_3.0x3.0mm_Pitch0.65mm" H 950 7550 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 950 7550 50  0001 C CNN
F 4 "296-13274-1-ND" H 950 7550 50  0001 C CNN "digikey"
	2    950  7550
	1    0    0    -1  
$EndComp
$Comp
L 74xGxx:74LVC2G04 U14
U 1 1 5D1546CD
P 1500 6950
F 0 "U14" H 1450 6950 50  0000 C CNN
F 1 "74_2G04" H 1500 7100 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-363_SC-70-6" H 1500 6950 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 1500 6950 50  0001 C CNN
F 4 "296-13262-1-ND" H 1500 6950 50  0001 C CNN "digikey"
	1    1500 6950
	1    0    0    -1  
$EndComp
Connection ~ 1200 6950
$Comp
L 74xx:74LS193 U21
U 1 1 5D15A360
P 5400 3550
F 0 "U21" V 5300 3550 50  0000 C CNN
F 1 "74_193" V 5400 3550 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 5400 3550 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS193" H 5400 3550 50  0001 C CNN
F 4 "1727-7974-1-ND" H 5400 3550 50  0001 C CNN "digikey"
	1    5400 3550
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS193 U22
U 1 1 5D15C737
P 7250 3150
F 0 "U22" V 7150 3150 50  0000 C CNN
F 1 "74_193" V 7250 3150 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 7250 3150 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS193" H 7250 3150 50  0001 C CNN
F 4 "1727-7974-1-ND" H 7250 3150 50  0001 C CNN "digikey"
	1    7250 3150
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS193 U23
U 1 1 5D15E550
P 5900 1300
F 0 "U23" V 5800 1300 50  0000 C CNN
F 1 "74_193" V 5900 1300 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 5900 1300 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS193" H 5900 1300 50  0001 C CNN
F 4 "1727-7974-1-ND" H 5900 1300 50  0001 C CNN "digikey"
	1    5900 1300
	1    0    0    -1  
$EndComp
Text Label 6050 5700 2    50   ~ 0
UP
Text Label 6050 5800 2    50   ~ 0
DOWN
Text Label 7050 5500 0    50   ~ 0
UPT1
Text Label 7050 5700 0    50   ~ 0
DWT1
Text Label 4900 3850 2    50   ~ 0
UPT1
Text Label 4900 3950 2    50   ~ 0
DWT1
Text Label 5900 3650 0    50   ~ 0
UPT2
Text Label 5900 3850 0    50   ~ 0
DWT2
Text Label 6750 3450 2    50   ~ 0
UPT2
Text Label 6750 3550 2    50   ~ 0
DWT2
Text Label 7750 3250 0    50   ~ 0
UPT3
Text Label 7750 3450 0    50   ~ 0
DWT3
Text Label 5400 1600 2    50   ~ 0
UPT3
Text Label 5400 1700 2    50   ~ 0
DWT3
$Comp
L 74xx:74LS573 U25
U 1 1 5D1619A1
P 7600 1350
F 0 "U25" V 7550 1400 50  0000 C CNN
F 1 "74_573" V 7650 1400 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-20_4.4x6.5mm_Pitch0.65mm" H 7600 1350 50  0001 C CNN
F 3 "74xx/74hc573.pdf" H 7600 1350 50  0001 C CNN
F 4 "296-3840-1-ND" H 7600 1350 50  0001 C CNN "digikey"
	1    7600 1350
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS573 U24
U 1 1 5D16673E
P 8900 3200
F 0 "U24" V 8850 3200 50  0000 C CNN
F 1 "74_573" V 8950 3200 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-20_4.4x6.5mm_Pitch0.65mm" H 8900 3200 50  0001 C CNN
F 3 "74xx/74hc573.pdf" H 8900 3200 50  0001 C CNN
F 4 "296-3840-1-ND" H 8900 3200 50  0001 C CNN "digikey"
	1    8900 3200
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74CBTLV3257 U41
U 1 1 5D170641
P 8000 6300
F 0 "U41" V 8000 6300 50  0000 C CNN
F 1 "74_3257" H 8000 6049 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 7950 6300 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74cbtlv3257.pdf" H 7950 6300 50  0001 C CNN
F 4 "74FST3257DTR2GOSCT-ND" H 8000 6300 50  0001 C CNN "digikey"
	1    8000 6300
	-1   0    0    1   
$EndComp
$Comp
L 74xx:74CBTLV3257 U41
U 2 1 5D199068
P 8000 5750
F 0 "U41" V 8000 5750 50  0000 C CNN
F 1 "74_3257" H 8000 5499 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 7950 5750 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74cbtlv3257.pdf" H 7950 5750 50  0001 C CNN
F 4 "74FST3257DTR2GOSCT-ND" H 8000 5750 50  0001 C CNN "digikey"
	2    8000 5750
	-1   0    0    1   
$EndComp
$Comp
L 74xx:74CBTLV3257 U41
U 3 1 5D19AEED
P 8800 5750
F 0 "U41" V 8800 5750 50  0000 C CNN
F 1 "74_3257" H 8800 5499 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 8750 5750 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74cbtlv3257.pdf" H 8750 5750 50  0001 C CNN
F 4 "74FST3257DTR2GOSCT-ND" H 8800 5750 50  0001 C CNN "digikey"
	3    8800 5750
	-1   0    0    1   
$EndComp
$Comp
L 74xx:74CBTLV3257 U41
U 4 1 5D19CA72
P 8800 6300
F 0 "U41" V 8800 6300 50  0000 C CNN
F 1 "74_3257" H 8800 6049 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 8750 6300 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74cbtlv3257.pdf" H 8750 6300 50  0001 C CNN
F 4 "74FST3257DTR2GOSCT-ND" H 8800 6300 50  0001 C CNN "digikey"
	4    8800 6300
	-1   0    0    1   
$EndComp
$Comp
L 74xx:74CBTLV3257 U40
U 5 1 5D19E5AF
P 4550 7300
F 0 "U40" H 4450 7300 50  0000 L CNN
F 1 "74_3257" V 4750 7050 50  0000 L CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 4500 7300 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74cbtlv3257.pdf" H 4500 7300 50  0001 C CNN
F 4 "74FST3257DTR2GOSCT-ND" H 4550 7300 50  0001 C CNN "digikey"
	5    4550 7300
	-1   0    0    1   
$EndComp
$Comp
L 74xx:74CBTLV3257 U40
U 1 1 5D1AB50D
P 5800 7550
F 0 "U40" V 5800 7550 50  0000 C CNN
F 1 "74_3257" H 5800 7299 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 5750 7550 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74cbtlv3257.pdf" H 5750 7550 50  0001 C CNN
F 4 "74FST3257DTR2GOSCT-ND" H 5800 7550 50  0001 C CNN "digikey"
	1    5800 7550
	-1   0    0    1   
$EndComp
$Comp
L 74xx:74CBTLV3257 U40
U 2 1 5D1AD1FA
P 5800 7050
F 0 "U40" V 5800 7050 50  0000 C CNN
F 1 "74_3257" H 5800 6799 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 5750 7050 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74cbtlv3257.pdf" H 5750 7050 50  0001 C CNN
F 4 "74FST3257DTR2GOSCT-ND" H 5800 7050 50  0001 C CNN "digikey"
	2    5800 7050
	-1   0    0    1   
$EndComp
$Comp
L 74xx:74CBTLV3257 U40
U 3 1 5D1AEA2B
P 6600 7050
F 0 "U40" V 6600 7050 50  0000 C CNN
F 1 "74_3257" H 6600 6799 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 6550 7050 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74cbtlv3257.pdf" H 6550 7050 50  0001 C CNN
F 4 "74FST3257DTR2GOSCT-ND" H 6600 7050 50  0001 C CNN "digikey"
	3    6600 7050
	-1   0    0    1   
$EndComp
$Comp
L 74xx:74CBTLV3257 U40
U 4 1 5D1AFEEA
P 6600 7550
F 0 "U40" V 6600 7550 50  0000 C CNN
F 1 "74_3257" H 6600 7300 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 6550 7550 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74cbtlv3257.pdf" H 6550 7550 50  0001 C CNN
F 4 "74FST3257DTR2GOSCT-ND" H 6600 7550 50  0001 C CNN "digikey"
	4    6600 7550
	-1   0    0    1   
$EndComp
$Comp
L 74xx:74CBTLV3257 U41
U 5 1 5D1B0DD3
P 4550 6300
F 0 "U41" H 4450 6300 50  0000 L CNN
F 1 "74_3257" V 4750 6050 50  0000 L CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 4500 6300 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/sn74cbtlv3257.pdf" H 4500 6300 50  0001 C CNN
F 4 "74FST3257DTR2GOSCT-ND" H 4550 6300 50  0001 C CNN "digikey"
	5    4550 6300
	-1   0    0    1   
$EndComp
$Comp
L 74xGxx:74LVC1G79 U1
U 1 1 5D164927
P 800 850
F 0 "U1" H 800 1050 50  0000 C CNN
F 1 "74_1G79" H 800 850 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-353_SC-70-5" H 800 850 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 800 850 50  0001 C CNN
F 4 "1727-4215-1-ND" H 800 850 50  0001 C CNN "digikey"
	1    800  850 
	1    0    0    -1  
$EndComp
Text Label 550  750  2    50   ~ 0
A
Text Label 550  950  3    50   ~ 0
CLK
$Comp
L 74xGxx:74LVC1G79 U2
U 1 1 5D16FAA2
P 1300 850
F 0 "U2" H 1300 1050 50  0000 C CNN
F 1 "74_1G79" H 1300 850 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-353_SC-70-5" H 1300 850 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 1300 850 50  0001 C CNN
F 4 "1727-4215-1-ND" H 1300 850 50  0001 C CNN "digikey"
	1    1300 850 
	1    0    0    -1  
$EndComp
Text Label 1050 950  3    50   ~ 0
CLK
$Comp
L 74xGxx:74LVC1G79 U3
U 1 1 5D170818
P 800 1500
F 0 "U3" H 800 1700 50  0000 C CNN
F 1 "74_1G79" H 800 1500 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-353_SC-70-5" H 800 1500 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 800 1500 50  0001 C CNN
F 4 "1727-4215-1-ND" H 800 1500 50  0001 C CNN "digikey"
	1    800  1500
	1    0    0    -1  
$EndComp
$Comp
L 74xGxx:74LVC1G79 U4
U 1 1 5D1719AB
P 1300 1500
F 0 "U4" H 1300 1700 50  0000 C CNN
F 1 "74_1G79" H 1300 1500 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-353_SC-70-5" H 1300 1500 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 1300 1500 50  0001 C CNN
F 4 "1727-4215-1-ND" H 1300 1500 50  0001 C CNN "digikey"
	1    1300 1500
	1    0    0    -1  
$EndComp
Text Label 1050 1600 3    50   ~ 0
CLK
Text Label 550  1600 3    50   ~ 0
CLK
Text Label 550  1400 2    50   ~ 0
B
Text Label 1550 750  0    50   ~ 0
Async
Text Label 1550 1400 0    50   ~ 0
Bsync
$Comp
L 74xx:74LS574 U5
U 1 1 5D17833D
P 1350 2550
F 0 "U5" V 1300 2550 50  0000 C CNN
F 1 "74_574" V 1400 2550 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-20_4.4x6.5mm_Pitch0.65mm" H 1350 2550 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS574" H 1350 2550 50  0001 C CNN
F 4 "296-12285-1-ND" H 1350 2550 50  0001 C CNN "digikey"
	1    1350 2550
	0    -1   -1   0   
$EndComp
Text Label 1750 3050 3    50   ~ 0
CLK
Text Label 1250 3050 3    50   ~ 0
Async
Text Label 850  3050 3    50   ~ 0
Bsync
Text Label 1250 2050 1    50   ~ 0
AQ0
Text Label 1350 3050 3    50   ~ 0
AQ0
Text Label 1350 2050 1    50   ~ 0
AQ1
Text Label 1450 3050 3    50   ~ 0
AQ1
Text Label 1450 2050 1    50   ~ 0
AQ2
Text Label 850  2050 1    50   ~ 0
BQ0
Text Label 950  3050 3    50   ~ 0
BQ0
Text Label 950  2050 1    50   ~ 0
BQ1
Text Label 1050 3050 3    50   ~ 0
BQ1
Text Label 1050 2050 1    50   ~ 0
BQ2
NoConn ~ 1150 2050
NoConn ~ 1150 3050
NoConn ~ 1550 3050
NoConn ~ 1550 2050
$Comp
L 74xx:74LS112 U10
U 1 1 5D1820DB
P 1600 3950
F 0 "U10" H 1600 3950 50  0000 C CNN
F 1 "74_112" H 1800 4200 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 1600 3950 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS112" H 1600 3950 50  0001 C CNN
F 4 " 74VHC112MTCXCT-ND" H 1600 3950 50  0001 C CNN "digikey"
	1    1600 3950
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS112 U10
U 2 1 5D183BA1
P 1600 5850
F 0 "U10" H 1600 5850 50  0000 C CNN
F 1 "74_112" H 1750 6100 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 1600 5850 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS112" H 1600 5850 50  0001 C CNN
F 4 " 74VHC112MTCXCT-ND" H 1600 5850 50  0001 C CNN "digikey"
	2    1600 5850
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS112 U10
U 3 1 5D18490E
P 2450 5900
F 0 "U10" V 2350 5800 50  0000 L CNN
F 1 "74_112" V 2550 5750 50  0000 L CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 2450 5900 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS112" H 2450 5900 50  0001 C CNN
F 4 " 74VHC112MTCXCT-ND" H 2450 5900 50  0001 C CNN "digikey"
	3    2450 5900
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS21 U6
U 1 1 5D1EAB86
P 1000 3650
F 0 "U6" H 950 3700 50  0000 C CNN
F 1 "74_21" H 1000 3600 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-14_4.4x5mm_Pitch0.65mm" H 1000 3650 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS21" H 1000 3650 50  0001 C CNN
F 4 "296-3800-1-ND" H 1000 3650 50  0001 C CNN "digikey"
	1    1000 3650
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS21 U6
U 2 1 5D21FCE3
P 1000 5550
F 0 "U6" H 950 5600 50  0000 C CNN
F 1 "74_21" H 1000 5450 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-14_4.4x5mm_Pitch0.65mm" H 1000 5550 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS21" H 1000 5550 50  0001 C CNN
F 4 "296-3800-1-ND" H 1000 5550 50  0001 C CNN "digikey"
	2    1000 5550
	1    0    0    -1  
$EndComp
$Comp
L 74xx:74LS21 U6
U 3 1 5D2223C5
P 2150 5050
F 0 "U6" V 2250 5050 50  0000 C CNN
F 1 "74_21" V 2050 5050 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-14_4.4x5mm_Pitch0.65mm" H 2150 5050 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS21" H 2150 5050 50  0001 C CNN
F 4 "296-3800-1-ND" H 2150 5050 50  0001 C CNN "digikey"
	3    2150 5050
	0    -1   -1   0   
$EndComp
Text Label 700  3800 2    50   ~ 0
AQ0
Text Label 700  3700 2    50   ~ 0
AQ1
Text Label 700  3600 2    50   ~ 0
AQ2
Text Label 700  5600 2    50   ~ 0
BQ0
Text Label 700  5500 2    50   ~ 0
BQ1
Text Label 700  5400 2    50   ~ 0
BQ2
Wire Wire Line
	1300 4250 1300 4050
Wire Wire Line
	1300 3650 1300 3850
Wire Wire Line
	1300 5750 1300 5550
Wire Wire Line
	1300 5950 1300 6150
Text Label 1300 3950 2    50   ~ 0
CLK
Text Label 1300 5850 2    50   ~ 0
CLK
NoConn ~ 1900 5950
NoConn ~ 1900 4050
Text Label 1900 3850 0    50   ~ 0
An
Text Label 1900 5750 0    50   ~ 0
Bn
$Comp
L 74xGxx:74LVC1G79 U11
U 1 1 5D23E344
P 3300 4650
F 0 "U11" H 3300 4850 50  0000 C CNN
F 1 "74_1G79" H 3300 4650 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-353_SC-70-5" H 3300 4650 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 3300 4650 50  0001 C CNN
F 4 "1727-4215-1-ND" H 3300 4650 50  0001 C CNN "digikey"
	1    3300 4650
	1    0    0    -1  
$EndComp
$Comp
L 74xGxx:74LVC1G79 U12
U 1 1 5D23FBEA
P 3300 5200
F 0 "U12" H 3300 5400 50  0000 C CNN
F 1 "74_1G79" H 3300 5200 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-353_SC-70-5" H 3300 5200 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 3300 5200 50  0001 C CNN
F 4 "1727-4215-1-ND" H 3300 5200 50  0001 C CNN "digikey"
	1    3300 5200
	1    0    0    -1  
$EndComp
Text Label 3050 4750 2    50   ~ 0
CLK
Text Label 3050 5300 2    50   ~ 0
CLK
Text Label 3050 4550 2    50   ~ 0
An
Text Label 3050 5100 2    50   ~ 0
Bn
Text Label 3550 4550 0    50   ~ 0
Ac
Text Label 3550 5100 0    50   ~ 0
Bc
$Comp
L 74xGxx:74LVC2G00 U15
U 1 1 5D16AF96
P 2350 7050
F 0 "U15" H 2300 7050 50  0000 C CNN
F 1 "74_2G00" H 2350 7200 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-8_3x3mm_Pitch0.65mm" H 2350 7050 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 2350 7050 50  0001 C CNN
F 4 "296-13257-1-ND" H 2350 7050 50  0001 C CNN "digikey"
	1    2350 7050
	1    0    0    -1  
$EndComp
$Comp
L 74xGxx:74LVC2G00 U15
U 2 1 5D173F00
P 2350 7550
F 0 "U15" H 2300 7550 50  0000 C CNN
F 1 "74_2G00" H 2350 7700 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-8_3x3mm_Pitch0.65mm" H 2350 7550 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 2350 7550 50  0001 C CNN
F 4 "296-13257-1-ND" H 2350 7550 50  0001 C CNN "digikey"
	2    2350 7550
	1    0    0    -1  
$EndComp
$Comp
L 74xGxx:74LVC1G27 U7
U 1 1 5D1B456B
P 1000 4250
F 0 "U7" V 1050 4250 50  0000 C CNN
F 1 "74_1G27" V 950 4250 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-363_SC-70-6" H 1000 4250 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 1000 4250 50  0001 C CNN
F 4 "296-18764-1-ND" H 1000 4250 50  0001 C CNN "digikey"
	1    1000 4250
	1    0    0    -1  
$EndComp
Text Label 700  4150 2    50   ~ 0
AQ0
Text Label 700  4350 2    50   ~ 0
AQ1
Text Label 700  4250 2    50   ~ 0
AQ2
$Comp
L 74xGxx:74LVC1G27 U8
U 1 1 5D1B5D7A
P 1000 6150
F 0 "U8" V 1050 6100 50  0000 C CNN
F 1 "74_1G27" V 950 6150 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-363_SC-70-6" H 1000 6150 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 1000 6150 50  0001 C CNN
F 4 "296-18764-1-ND" H 1000 6150 50  0001 C CNN "digikey"
	1    1000 6150
	1    0    0    -1  
$EndComp
Text Label 700  6050 2    50   ~ 0
BQ0
Text Label 700  6250 2    50   ~ 0
BQ1
Text Label 700  6150 2    50   ~ 0
BQ2
Text Label 8850 4750 0    50   ~ 0
latch
$Comp
L 74xGxx:74LVC2G04 U14
U 2 1 5D17E546
P 1500 7550
F 0 "U14" H 1450 7550 50  0000 C CNN
F 1 "74_2G04" H 1500 7700 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-363_SC-70-6" H 1500 7550 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 1500 7550 50  0001 C CNN
F 4 "296-13262-1-ND" H 1500 7550 50  0001 C CNN "digikey"
	2    1500 7550
	1    0    0    -1  
$EndComp
Connection ~ 1200 7550
$Comp
L Connector_Generic:Conn_01x15 J1
U 1 1 5D2C325D
P 9400 1300
F 0 "J1" H 9350 500 50  0000 L CNN
F 1 "NANO_L" V 9500 1600 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x15_Pitch2.54mm" H 9400 1300 50  0001 C CNN
F 3 "~" H 9400 1300 50  0001 C CNN
	1    9400 1300
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x15 J2
U 1 1 5D2C74A6
P 10050 1300
F 0 "J2" H 10000 500 50  0000 L CNN
F 1 "NANO_R" V 10150 1600 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x15_Pitch2.54mm" H 10050 1300 50  0001 C CNN
F 3 "~" H 10050 1300 50  0001 C CNN
	1    10050 1300
	1    0    0    -1  
$EndComp
Text Label 9200 600  2    50   ~ 0
SCK
Text Label 9200 900  2    50   ~ 0
D01L
Text Label 9200 1000 2    50   ~ 0
D23L
Text Label 9200 1100 2    50   ~ 0
D54L
Text Label 9200 1200 2    50   ~ 0
D76L
Text Label 9200 1300 2    50   ~ 0
D01H
Text Label 9200 1400 2    50   ~ 0
D23H
$Comp
L power:VCC #PWR0101
U 1 1 5D2CDB22
P 9200 1700
F 0 "#PWR0101" H 9200 1550 50  0001 C CNN
F 1 "VCC" H 9150 1850 50  0000 L CNN
F 2 "" H 9200 1700 50  0001 C CNN
F 3 "" H 9200 1700 50  0001 C CNN
	1    9200 1700
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 5D2CEDB3
P 9200 1900
F 0 "#PWR0102" H 9200 1650 50  0001 C CNN
F 1 "GND" H 9250 1750 50  0000 R CNN
F 2 "" H 9200 1900 50  0001 C CNN
F 3 "" H 9200 1900 50  0001 C CNN
	1    9200 1900
	0    1    1    0   
$EndComp
Text Label 9850 700  2    50   ~ 0
MOSI
Text Label 9850 600  2    50   ~ 0
MISO
Text Label 9850 800  2    50   ~ 0
SPISS
Text Label 9850 900  2    50   ~ 0
rSel
Text Label 9850 1000 2    50   ~ 0
read
Text Label 9850 1100 2    50   ~ 0
D76H
Text Label 9850 1200 2    50   ~ 0
D54H
Text Label 9850 1400 2    50   ~ 0
ORIN
Text Label 9850 1300 2    50   ~ 0
ORCLR
Text Label 9850 1800 2    50   ~ 0
RST
NoConn ~ 9850 2000
NoConn ~ 9850 1900
NoConn ~ 9850 1700
NoConn ~ 9850 1600
NoConn ~ 9200 1500
NoConn ~ 9200 700 
NoConn ~ 9200 800 
NoConn ~ 9200 1600
NoConn ~ 9200 1800
NoConn ~ 9200 2000
$Comp
L power:VCC #PWR0103
U 1 1 5D2E8A62
P 550 2550
F 0 "#PWR0103" H 550 2400 50  0001 C CNN
F 1 "VCC" H 450 2700 50  0000 L CNN
F 2 "" H 550 2550 50  0001 C CNN
F 3 "" H 550 2550 50  0001 C CNN
	1    550  2550
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0104
U 1 1 5D2EFC04
P 2150 2550
F 0 "#PWR0104" H 2150 2300 50  0001 C CNN
F 1 "GND" H 2200 2400 50  0000 R CNN
F 2 "" H 2150 2550 50  0001 C CNN
F 3 "" H 2150 2550 50  0001 C CNN
	1    2150 2550
	1    0    0    -1  
$EndComp
Text Label 4000 1600 0    50   ~ 0
CLK
$Comp
L Oscillator:ASE-xxxMHz UX1
U 1 1 5D301C32
P 3350 900
F 0 "UX1" H 3400 1150 50  0000 L CNN
F 1 "CTX10M" H 3400 650 50  0000 L CNN
F 2 "Oscillators:Oscillator_SMD_Abracon_ASV-4pin_7.0x5.1mm_HandSoldering" H 4050 550 50  0001 C CNN
F 3 "http://www.abracon.com/Oscillators/ASV.pdf" H 3250 900 50  0001 C CNN
F 4 "CTX265CT-ND" H 3350 900 50  0001 C CNN "digikey"
	1    3350 900 
	1    0    0    -1  
$EndComp
Text Label 3650 900  0    50   ~ 0
OSC
Text Label 3000 2550 2    50   ~ 0
OSC
NoConn ~ 4000 1850
NoConn ~ 4000 1950
NoConn ~ 4000 2050
NoConn ~ 4000 2250
NoConn ~ 3000 1750
NoConn ~ 3000 1850
NoConn ~ 3000 1950
NoConn ~ 3000 2050
$Comp
L power:VCC #PWR0105
U 1 1 5D30A8A2
P 3000 2750
F 0 "#PWR0105" H 3000 2600 50  0001 C CNN
F 1 "VCC" H 2950 2900 50  0000 L CNN
F 2 "" H 3000 2750 50  0001 C CNN
F 3 "" H 3000 2750 50  0001 C CNN
	1    3000 2750
	-1   0    0    1   
$EndComp
$Comp
L power:VCC #PWR0106
U 1 1 5D30BE00
P 3000 2250
F 0 "#PWR0106" H 3000 2100 50  0001 C CNN
F 1 "VCC" V 2900 2250 50  0000 L CNN
F 2 "" H 3000 2250 50  0001 C CNN
F 3 "" H 3000 2250 50  0001 C CNN
	1    3000 2250
	1    0    0    -1  
$EndComp
Wire Wire Line
	3000 2450 3000 2350
Wire Wire Line
	3000 2350 3000 2250
Connection ~ 3000 2350
Connection ~ 3000 2250
$Comp
L 74xx:74LS161 UX2
U 1 1 5D30E190
P 3500 2250
F 0 "UX2" V 3450 2250 50  0000 C CNN
F 1 "74_161" V 3550 2250 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-16_4.4x5mm_Pitch0.65mm" H 3500 2250 50  0001 C CNN
F 3 "http://www.ti.com/lit/gpn/sn74LS161" H 3500 2250 50  0001 C CNN
F 4 "296-12344-1-ND" H 3500 2250 50  0001 C CNN "digikey"
	1    3500 2250
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0107
U 1 1 5D30E26C
P 3500 1450
F 0 "#PWR0107" H 3500 1300 50  0001 C CNN
F 1 "VCC" V 3600 1500 50  0000 L CNN
F 2 "" H 3500 1450 50  0001 C CNN
F 3 "" H 3500 1450 50  0001 C CNN
	1    3500 1450
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0108
U 1 1 5D310657
P 3500 3050
F 0 "#PWR0108" H 3500 2800 50  0001 C CNN
F 1 "GND" V 3600 3000 50  0000 R CNN
F 2 "" H 3500 3050 50  0001 C CNN
F 3 "" H 3500 3050 50  0001 C CNN
	1    3500 3050
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0109
U 1 1 5D32F010
P 700 3500
F 0 "#PWR0109" H 700 3350 50  0001 C CNN
F 1 "VCC" V 800 3500 50  0000 L CNN
F 2 "" H 700 3500 50  0001 C CNN
F 3 "" H 700 3500 50  0001 C CNN
	1    700  3500
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0110
U 1 1 5D32FF6B
P 700 5700
F 0 "#PWR0110" H 700 5550 50  0001 C CNN
F 1 "VCC" V 600 5700 50  0000 L CNN
F 2 "" H 700 5700 50  0001 C CNN
F 3 "" H 700 5700 50  0001 C CNN
	1    700  5700
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_01x04 J10
U 1 1 5D332C2E
P 11000 900
F 0 "J10" H 10950 1100 50  0000 L CNN
F 1 "lap reset" V 11100 700 50  0000 L CNN
F 2 "additional_connectors:Connectors_JST_B4B-PH-K" H 11000 900 50  0001 C CNN
F 3 "~" H 11000 900 50  0001 C CNN
F 4 "455-1706-ND" H 11000 900 50  0001 C CNN "digikey"
F 5 "455-1721-ND" H 11000 900 50  0001 C CNN "digikey_alt"
F 6 "SPH-002T-P0.5S (455-1127-1-ND), PHR-4 (455-1164-ND)" H 11000 900 50  0001 C CNN "additional_parts"
	1    11000 900 
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x04 J11
U 1 1 5D33611B
P 11000 1650
F 0 "J11" H 10950 1850 50  0000 L CNN
F 1 "encoder" V 11100 1450 50  0000 L CNN
F 2 "additional_connectors:Connectors_JST_B4B-PH-K" H 11000 1650 50  0001 C CNN
F 3 "~" H 11000 1650 50  0001 C CNN
F 4 "455-1706-ND" H 11000 1650 50  0001 C CNN "digikey"
F 5 "455-1721-ND" H 11000 1650 50  0001 C CNN "digikey_alt"
F 6 "SPH-002T-P0.5S (455-1127-1-ND), PHR-4 (455-1164-ND)" H 11000 1650 50  0001 C CNN "additional_parts"
	1    11000 1650
	1    0    0    -1  
$EndComp
Text Label 10800 1550 2    50   ~ 0
B
Text Label 10800 1750 2    50   ~ 0
A
$Comp
L power:GND #PWR0111
U 1 1 5D337C89
P 10800 1650
F 0 "#PWR0111" H 10800 1400 50  0001 C CNN
F 1 "GND" V 10800 1550 50  0000 R CNN
F 2 "" H 10800 1650 50  0001 C CNN
F 3 "" H 10800 1650 50  0001 C CNN
	1    10800 1650
	0    1    1    0   
$EndComp
$Comp
L power:VCC #PWR0112
U 1 1 5D338C66
P 10800 1850
F 0 "#PWR0112" H 10800 1700 50  0001 C CNN
F 1 "VCC" H 10750 2000 50  0000 L CNN
F 2 "" H 10800 1850 50  0001 C CNN
F 3 "" H 10800 1850 50  0001 C CNN
	1    10800 1850
	0    -1   -1   0   
$EndComp
Text Label 10800 800  2    50   ~ 0
ORIN
Text Label 10800 1000 2    50   ~ 0
ORCLR
$Comp
L power:GND #PWR0113
U 1 1 5D3393F2
P 10550 900
F 0 "#PWR0113" H 10550 650 50  0001 C CNN
F 1 "GND" H 10650 750 50  0000 R CNN
F 2 "" H 10550 900 50  0001 C CNN
F 3 "" H 10550 900 50  0001 C CNN
	1    10550 900 
	0    1    1    0   
$EndComp
$Comp
L power:VCC #PWR0114
U 1 1 5D339C3B
P 10800 1100
F 0 "#PWR0114" H 10800 950 50  0001 C CNN
F 1 "VCC" V 10800 1200 50  0000 L CNN
F 2 "" H 10800 1100 50  0001 C CNN
F 3 "" H 10800 1100 50  0001 C CNN
	1    10800 1100
	0    -1   -1   0   
$EndComp
Wire Wire Line
	10800 900  10550 900 
$Comp
L Device:R R3
U 1 1 5D33E2EC
P 10550 750
F 0 "R3" V 10550 700 50  0000 L CNN
F 1 "100K" V 10450 650 50  0000 L CNN
F 2 "Resistors_SMD:R_0603" V 10480 750 50  0001 C CNN
F 3 "~" H 10550 750 50  0001 C CNN
	1    10550 750 
	1    0    0    -1  
$EndComp
Wire Wire Line
	10800 800  10800 600 
Wire Wire Line
	10800 600  10550 600 
$Comp
L Device:R R2
U 1 1 5D340AD5
P 11000 2300
F 0 "R2" V 11000 2250 50  0000 L CNN
F 1 "100K" V 10900 2200 50  0000 L CNN
F 2 "Resistors_SMD:R_0603" V 10930 2300 50  0001 C CNN
F 3 "~" H 11000 2300 50  0001 C CNN
	1    11000 2300
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5D342AD9
P 10800 2300
F 0 "R1" V 10800 2250 50  0000 L CNN
F 1 "100K" V 10700 2200 50  0000 L CNN
F 2 "Resistors_SMD:R_0603" V 10730 2300 50  0001 C CNN
F 3 "~" H 10800 2300 50  0001 C CNN
	1    10800 2300
	1    0    0    -1  
$EndComp
Text Label 10800 2150 2    50   ~ 0
B
Text Label 11000 2150 2    50   ~ 0
A
$Comp
L power:GND #PWR0115
U 1 1 5D342F7A
P 10800 2450
F 0 "#PWR0115" H 10800 2200 50  0001 C CNN
F 1 "GND" V 10900 2450 50  0000 R CNN
F 2 "" H 10800 2450 50  0001 C CNN
F 3 "" H 10800 2450 50  0001 C CNN
	1    10800 2450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0116
U 1 1 5D3434A5
P 11000 2450
F 0 "#PWR0116" H 11000 2200 50  0001 C CNN
F 1 "GND" V 11100 2450 50  0000 R CNN
F 2 "" H 11000 2450 50  0001 C CNN
F 3 "" H 11000 2450 50  0001 C CNN
	1    11000 2450
	1    0    0    -1  
$EndComp
$Comp
L Connector:USB3_A J6
U 1 1 5D344A59
P 10450 3350
F 0 "J6" H 10100 3950 50  0000 C CNN
F 1 "SPIOut" H 10700 3950 50  0000 C CNN
F 2 "additional_connectors:USB3_A_vertical_molex" H 10600 3450 50  0001 C CNN
F 3 "~" H 10600 3450 50  0001 C CNN
F 4 "WM10421-ND" H 10450 3350 50  0001 C CNN "digikey"
	1    10450 3350
	1    0    0    -1  
$EndComp
Connection ~ 10550 900 
$Comp
L Connector_Generic:Conn_01x05 J3
U 1 1 5D375141
P 10150 4750
F 0 "J3" H 10100 5050 50  0000 L CNN
F 1 "ENCL" V 10250 4500 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x05_Pitch2.54mm" H 10150 4750 50  0001 C CNN
F 3 "~" H 10150 4750 50  0001 C CNN
	1    10150 4750
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x05 J4
U 1 1 5D377735
P 10750 4750
F 0 "J4" H 10700 5050 50  0000 L CNN
F 1 "ENCR" V 10750 4550 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x05_Pitch2.54mm" H 10750 4750 50  0001 C CNN
F 3 "~" H 10750 4750 50  0001 C CNN
	1    10750 4750
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x05 J5
U 1 1 5D377D72
P 11050 4750
F 0 "J5" H 11000 5050 50  0000 L CNN
F 1 "ENCRW" V 11150 4500 50  0000 L CNN
F 2 "Pin_Headers:Pin_Header_Straight_1x05_Pitch2.54mm" H 11050 4750 50  0001 C CNN
F 3 "~" H 11050 4750 50  0001 C CNN
	1    11050 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	10550 4850 10850 4850
Wire Wire Line
	10550 4650 10850 4650
Wire Wire Line
	10550 4550 10850 4550
Text Label 9950 4550 2    50   ~ 0
SCK
Text Label 9950 4650 2    50   ~ 0
MOSI
Text Label 9950 4750 2    50   ~ 0
MISO
NoConn ~ 9950 4850
NoConn ~ 9950 4950
Wire Wire Line
	10850 4750 10550 4750
Text Label 10550 4750 2    50   ~ 0
RST
Text Label 10550 4850 2    50   ~ 0
SPISS
$Comp
L power:GND #PWR0117
U 1 1 5D387E2B
P 10550 4650
F 0 "#PWR0117" H 10550 4400 50  0001 C CNN
F 1 "GND" V 10550 4550 50  0000 R CNN
F 2 "" H 10550 4650 50  0001 C CNN
F 3 "" H 10550 4650 50  0001 C CNN
	1    10550 4650
	0    1    1    0   
$EndComp
Connection ~ 10550 4650
Connection ~ 10550 4550
$Comp
L power:VCC #PWR0118
U 1 1 5D39195B
P 10950 2950
F 0 "#PWR0118" H 10950 2800 50  0001 C CNN
F 1 "VCC" V 10850 2900 50  0000 L CNN
F 2 "" H 10950 2950 50  0001 C CNN
F 3 "" H 10950 2950 50  0001 C CNN
	1    10950 2950
	0    1    1    0   
$EndComp
Text Label 10950 3550 0    50   ~ 0
SPISS
Text Label 10950 3450 0    50   ~ 0
MISO
Text Label 10950 3150 0    50   ~ 0
MOSI
$Comp
L power:GND #PWR0119
U 1 1 5D393D63
P 10250 4050
F 0 "#PWR0119" H 10250 3800 50  0001 C CNN
F 1 "GND" H 10200 3950 50  0000 R CNN
F 2 "" H 10250 4050 50  0001 C CNN
F 3 "" H 10250 4050 50  0001 C CNN
	1    10250 4050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0120
U 1 1 5D3944C6
P 10450 4050
F 0 "#PWR0120" H 10450 3800 50  0001 C CNN
F 1 "GND" H 10650 3950 50  0000 R CNN
F 2 "" H 10450 4050 50  0001 C CNN
F 3 "" H 10450 4050 50  0001 C CNN
	1    10450 4050
	1    0    0    -1  
$EndComp
NoConn ~ 10350 4050
Text Label 10950 3750 0    50   ~ 0
RST
Text Label 10950 3850 0    50   ~ 0
SCK
NoConn ~ 10950 3250
$Comp
L Connector:USB_B_Micro J7
U 1 1 5D3A6F26
P 9800 5750
F 0 "J7" H 9650 6100 50  0000 C CNN
F 1 "PWR" V 9550 5800 50  0000 C CNN
F 2 "Connectors:USB_Micro-B" H 9950 5700 50  0001 C CNN
F 3 "~" H 9950 5700 50  0001 C CNN
F 4 "609-4618-1-ND" H 9800 5750 50  0001 C CNN "digikey"
	1    9800 5750
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0121
U 1 1 5D3B2285
P 10100 5550
F 0 "#PWR0121" H 10100 5400 50  0001 C CNN
F 1 "VCC" V 10000 5550 50  0000 L CNN
F 2 "" H 10100 5550 50  0001 C CNN
F 3 "" H 10100 5550 50  0001 C CNN
	1    10100 5550
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0122
U 1 1 5D3B2968
P 9800 6150
F 0 "#PWR0122" H 9800 5900 50  0001 C CNN
F 1 "GND" V 9900 6150 50  0000 R CNN
F 2 "" H 9800 6150 50  0001 C CNN
F 3 "" H 9800 6150 50  0001 C CNN
	1    9800 6150
	1    0    0    -1  
$EndComp
NoConn ~ 10100 5750
NoConn ~ 10100 5850
NoConn ~ 10100 5950
NoConn ~ 9700 6150
$Comp
L Regulator_Linear:AZ1117-3.3 U90
U 1 1 5D3B64D2
P 10750 6050
F 0 "U90" H 10850 5800 50  0000 C CNN
F 1 "AZ1117-3.3" H 10750 6201 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-223-3_TabPin2" H 10750 6300 50  0001 C CIN
F 3 "https://www.diodes.com/assets/Datasheets/AZ1117.pdf" H 10750 6050 50  0001 C CNN
F 4 "AZ1117EH-3.3TRG1DICT-ND" H 10750 6050 50  0001 C CNN "digikey"
	1    10750 6050
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0123
U 1 1 5D3B875C
P 10450 6050
F 0 "#PWR0123" H 10450 5900 50  0001 C CNN
F 1 "VCC" V 10450 6200 50  0000 L CNN
F 2 "" H 10450 6050 50  0001 C CNN
F 3 "" H 10450 6050 50  0001 C CNN
	1    10450 6050
	-1   0    0    1   
$EndComp
$Comp
L power:+3.3V #PWR0124
U 1 1 5D3B94B6
P 10550 4550
F 0 "#PWR0124" H 10550 4400 50  0001 C CNN
F 1 "+3.3V" V 10600 4550 50  0000 L CNN
F 2 "" H 10550 4550 50  0001 C CNN
F 3 "" H 10550 4550 50  0001 C CNN
	1    10550 4550
	0    -1   -1   0   
$EndComp
$Comp
L power:+3.3V #PWR0125
U 1 1 5D3B97B3
P 11050 6050
F 0 "#PWR0125" H 11050 5900 50  0001 C CNN
F 1 "+3.3V" V 11050 6200 50  0000 L CNN
F 2 "" H 11050 6050 50  0001 C CNN
F 3 "" H 11050 6050 50  0001 C CNN
	1    11050 6050
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0126
U 1 1 5D3BD398
P 10750 6350
F 0 "#PWR0126" H 10750 6100 50  0001 C CNN
F 1 "GND" H 10700 6250 50  0000 R CNN
F 2 "" H 10750 6350 50  0001 C CNN
F 3 "" H 10750 6350 50  0001 C CNN
	1    10750 6350
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small U90C1
U 1 1 5D3C381D
P 10450 5750
F 0 "U90C1" V 10550 5700 50  0000 L CNN
F 1 "1uF" V 10350 5700 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 10450 5750 50  0001 C CNN
F 3 "~" H 10450 5750 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 10450 5750 50  0001 C CNN "specs"
	1    10450 5750
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small U90C2
U 1 1 5D3C55C5
P 11050 5750
F 0 "U90C2" V 11150 5700 50  0000 L CNN
F 1 "1uF" V 10950 5700 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 11050 5750 50  0001 C CNN
F 3 "~" H 11050 5750 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 11050 5750 50  0001 C CNN "specs"
	1    11050 5750
	1    0    0    -1  
$EndComp
Wire Wire Line
	10450 5850 10450 6050
Connection ~ 10450 6050
Wire Wire Line
	11050 5850 11050 6050
Connection ~ 11050 6050
$Comp
L power:GND #PWR0127
U 1 1 5D3C7F71
P 10450 5650
F 0 "#PWR0127" H 10450 5400 50  0001 C CNN
F 1 "GND" H 10500 5500 50  0000 R CNN
F 2 "" H 10450 5650 50  0001 C CNN
F 3 "" H 10450 5650 50  0001 C CNN
	1    10450 5650
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0128
U 1 1 5D3C8523
P 11050 5650
F 0 "#PWR0128" H 11050 5400 50  0001 C CNN
F 1 "GND" H 11100 5500 50  0000 R CNN
F 2 "" H 11050 5650 50  0001 C CNN
F 3 "" H 11050 5650 50  0001 C CNN
	1    11050 5650
	-1   0    0    1   
$EndComp
Text Label 6100 7050 3    50   ~ 0
D54L
Text Label 6100 7550 3    50   ~ 0
D76L
Text Label 6900 7550 3    50   ~ 0
D01L
Text Label 6900 7050 3    50   ~ 0
D23L
Text Label 9100 6300 3    50   ~ 0
D01H
Text Label 9100 5750 3    50   ~ 0
D23H
Text Label 8300 5750 3    50   ~ 0
D54H
Text Label 8300 6300 3    50   ~ 0
D76H
Text Label 5500 6950 2    50   ~ 0
D4L
Text Label 7700 5650 2    50   ~ 0
D4H
Text Label 7700 6200 2    50   ~ 0
D6H
Text Label 5500 7450 2    50   ~ 0
D6L
Text Label 7700 5850 2    50   ~ 0
D5H
Text Label 5500 7150 2    50   ~ 0
D5L
Text Label 7700 6400 2    50   ~ 0
D7H
Text Label 5500 7650 2    50   ~ 0
D7L
Text Label 8500 6400 2    50   ~ 0
D0H
Text Label 6300 7650 2    50   ~ 0
D0L
Text Label 8500 6200 2    50   ~ 0
D1H
Text Label 6300 7450 2    50   ~ 0
D1L
Text Label 8500 5850 2    50   ~ 0
D2H
Text Label 6300 7150 2    50   ~ 0
D2L
Text Label 8500 5650 2    50   ~ 0
D3H
Text Label 6300 6950 2    50   ~ 0
D3L
Text Label 9400 2700 0    50   ~ 0
D0L
Text Label 9400 2800 0    50   ~ 0
D1L
Text Label 9400 2900 0    50   ~ 0
D2L
Text Label 9400 3000 0    50   ~ 0
D3L
Text Label 9400 3100 0    50   ~ 0
D4L
Text Label 9400 3200 0    50   ~ 0
D5L
Text Label 9400 3300 0    50   ~ 0
D6L
Text Label 9400 3400 0    50   ~ 0
D7L
Text Label 8100 850  0    50   ~ 0
D0H
Text Label 8100 950  0    50   ~ 0
D1H
Text Label 8100 1050 0    50   ~ 0
D2H
Text Label 8100 1150 0    50   ~ 0
D3H
Text Label 8100 1250 0    50   ~ 0
D4H
Text Label 8100 1350 0    50   ~ 0
D5H
Text Label 8100 1450 0    50   ~ 0
D6H
Text Label 8100 1550 0    50   ~ 0
D7H
Text Label 7100 950  2    50   ~ 0
C1H
Text Label 7100 1050 2    50   ~ 0
C2H
Text Label 7100 1150 2    50   ~ 0
C3H
Text Label 7100 1250 2    50   ~ 0
C4H
Text Label 7100 1350 2    50   ~ 0
C5H
Text Label 7100 1450 2    50   ~ 0
C6H
Text Label 7100 1550 2    50   ~ 0
C7H
Text Label 6400 900  0    50   ~ 0
C4H
Text Label 6400 1000 0    50   ~ 0
C5H
Text Label 6400 1100 0    50   ~ 0
C6H
Text Label 6400 1200 0    50   ~ 0
C7H
Text Label 7100 850  2    50   ~ 0
C0H
Text Label 7750 2750 0    50   ~ 0
C0H
Text Label 7750 2850 0    50   ~ 0
C1H
Text Label 7750 2950 0    50   ~ 0
C2H
Text Label 7750 3050 0    50   ~ 0
C3H
$Comp
L 74xGxx:74LVC1G79 U30
U 1 1 5D494339
P 8100 4850
F 0 "U30" H 8100 5050 50  0000 C CNN
F 1 "74_1G79" H 8100 4850 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-353_SC-70-5" H 8100 4850 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 8100 4850 50  0001 C CNN
F 4 "1727-4215-1-ND" H 8100 4850 50  0001 C CNN "digikey"
	1    8100 4850
	1    0    0    -1  
$EndComp
$Comp
L 74xGxx:74LVC1G79 U31
U 1 1 5D494342
P 8600 4850
F 0 "U31" H 8600 5050 50  0000 C CNN
F 1 "74_1G79" H 8600 4850 50  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-353_SC-70-5" H 8600 4850 50  0001 C CNN
F 3 "http://www.ti.com/lit/sg/scyt129e/scyt129e.pdf" H 8600 4850 50  0001 C CNN
F 4 "1727-4215-1-ND" H 8600 4850 50  0001 C CNN "digikey"
	1    8600 4850
	1    0    0    -1  
$EndComp
Text Label 7850 4750 2    50   ~ 0
read
Text Label 8400 2700 2    50   ~ 0
C0L
Text Label 8400 2800 2    50   ~ 0
C1L
Text Label 8400 2900 2    50   ~ 0
C2L
Text Label 8400 3000 2    50   ~ 0
C3L
Text Label 8400 3100 2    50   ~ 0
C4L
Text Label 8400 3200 2    50   ~ 0
C5L
Text Label 8400 3300 2    50   ~ 0
C6L
Text Label 8400 3400 2    50   ~ 0
C7L
Text Label 7050 5000 0    50   ~ 0
C0L
Text Label 7050 5100 0    50   ~ 0
C1L
Text Label 7050 5200 0    50   ~ 0
C2L
Text Label 7050 5300 0    50   ~ 0
C3L
Text Label 5900 3150 0    50   ~ 0
C4L
Text Label 5900 3250 0    50   ~ 0
C5L
Text Label 5900 3350 0    50   ~ 0
C6L
Text Label 5900 3450 0    50   ~ 0
C7L
Text Label 4950 6400 0    50   ~ 0
rSel
Text Label 4950 7400 0    50   ~ 0
rSel
$Comp
L power:GND #PWR0129
U 1 1 5D1B9C92
P 4550 5900
F 0 "#PWR0129" H 4550 5650 50  0001 C CNN
F 1 "GND" V 4550 5800 50  0000 R CNN
F 2 "" H 4550 5900 50  0001 C CNN
F 3 "" H 4550 5900 50  0001 C CNN
	1    4550 5900
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0130
U 1 1 5D1BA7BD
P 4550 6900
F 0 "#PWR0130" H 4550 6650 50  0001 C CNN
F 1 "GND" V 4550 6800 50  0000 R CNN
F 2 "" H 4550 6900 50  0001 C CNN
F 3 "" H 4550 6900 50  0001 C CNN
	1    4550 6900
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0131
U 1 1 5D1BAD8C
P 4550 7700
F 0 "#PWR0131" H 4550 7550 50  0001 C CNN
F 1 "VCC" V 4550 7800 50  0000 L CNN
F 2 "" H 4550 7700 50  0001 C CNN
F 3 "" H 4550 7700 50  0001 C CNN
	1    4550 7700
	0    1    1    0   
$EndComp
$Comp
L power:VCC #PWR0132
U 1 1 5D1BC54E
P 4550 6700
F 0 "#PWR0132" H 4550 6550 50  0001 C CNN
F 1 "VCC" V 4550 6800 50  0000 L CNN
F 2 "" H 4550 6700 50  0001 C CNN
F 3 "" H 4550 6700 50  0001 C CNN
	1    4550 6700
	0    1    1    0   
$EndComp
$Comp
L Device:C_Small U40C1
U 1 1 5D1BD7AE
P 4100 7400
F 0 "U40C1" V 4200 7350 50  0000 L CNN
F 1 "0.1uF" V 4000 7350 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 4100 7400 50  0001 C CNN
F 3 "~" H 4100 7400 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 4100 7400 50  0001 C CNN "specs"
	1    4100 7400
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small U41C1
U 1 1 5D1BFF81
P 4100 6350
F 0 "U41C1" V 4200 6300 50  0000 L CNN
F 1 "0.1uF" V 4000 6300 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 4100 6350 50  0001 C CNN
F 3 "~" H 4100 6350 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 4100 6350 50  0001 C CNN "specs"
	1    4100 6350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0133
U 1 1 5D1C0876
P 4100 6450
F 0 "#PWR0133" H 4100 6200 50  0001 C CNN
F 1 "GND" V 4100 6350 50  0000 R CNN
F 2 "" H 4100 6450 50  0001 C CNN
F 3 "" H 4100 6450 50  0001 C CNN
	1    4100 6450
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0134
U 1 1 5D1C0F5A
P 4100 6250
F 0 "#PWR0134" H 4100 6100 50  0001 C CNN
F 1 "VCC" V 4100 6350 50  0000 L CNN
F 2 "" H 4100 6250 50  0001 C CNN
F 3 "" H 4100 6250 50  0001 C CNN
	1    4100 6250
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0135
U 1 1 5D1D7E65
P 4100 7300
F 0 "#PWR0135" H 4100 7150 50  0001 C CNN
F 1 "VCC" V 4100 7400 50  0000 L CNN
F 2 "" H 4100 7300 50  0001 C CNN
F 3 "" H 4100 7300 50  0001 C CNN
	1    4100 7300
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0136
U 1 1 5D1D83AB
P 4100 7500
F 0 "#PWR0136" H 4100 7250 50  0001 C CNN
F 1 "GND" V 4100 7400 50  0000 R CNN
F 2 "" H 4100 7500 50  0001 C CNN
F 3 "" H 4100 7500 50  0001 C CNN
	1    4100 7500
	1    0    0    -1  
$EndComp
Text Label 8400 3600 2    50   ~ 0
latch
Text Label 7100 1750 2    50   ~ 0
latch
Text Label 9650 3750 0    50   ~ 0
read
$Comp
L Device:R R4
U 1 1 5D20CBEE
P 9650 3900
F 0 "R4" V 9650 3850 50  0000 L CNN
F 1 "100K" V 9750 3800 50  0000 L CNN
F 2 "Resistors_SMD:R_0603" V 9580 3900 50  0001 C CNN
F 3 "~" H 9650 3900 50  0001 C CNN
	1    9650 3900
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0137
U 1 1 5D20D32C
P 9650 4050
F 0 "#PWR0137" H 9650 3900 50  0001 C CNN
F 1 "VCC" V 9550 4050 50  0000 L CNN
F 2 "" H 9650 4050 50  0001 C CNN
F 3 "" H 9650 4050 50  0001 C CNN
	1    9650 4050
	-1   0    0    1   
$EndComp
$Comp
L power:VCC #PWR0138
U 1 1 5D20FE78
P 8900 2400
F 0 "#PWR0138" H 8900 2250 50  0001 C CNN
F 1 "VCC" V 9000 2450 50  0000 L CNN
F 2 "" H 8900 2400 50  0001 C CNN
F 3 "" H 8900 2400 50  0001 C CNN
	1    8900 2400
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0139
U 1 1 5D210B57
P 8900 4000
F 0 "#PWR0139" H 8900 3750 50  0001 C CNN
F 1 "GND" V 9000 3950 50  0000 R CNN
F 2 "" H 8900 4000 50  0001 C CNN
F 3 "" H 8900 4000 50  0001 C CNN
	1    8900 4000
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small U24C1
U 1 1 5D215462
P 9750 3150
F 0 "U24C1" V 9850 3100 50  0000 L CNN
F 1 "0.1uF" V 9650 3100 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 9750 3150 50  0001 C CNN
F 3 "~" H 9750 3150 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 9750 3150 50  0001 C CNN "specs"
	1    9750 3150
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0140
U 1 1 5D215468
P 9750 3050
F 0 "#PWR0140" H 9750 2900 50  0001 C CNN
F 1 "VCC" V 9750 3150 50  0000 L CNN
F 2 "" H 9750 3050 50  0001 C CNN
F 3 "" H 9750 3050 50  0001 C CNN
	1    9750 3050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0141
U 1 1 5D21546E
P 9750 3250
F 0 "#PWR0141" H 9750 3000 50  0001 C CNN
F 1 "GND" V 9750 3150 50  0000 R CNN
F 2 "" H 9750 3250 50  0001 C CNN
F 3 "" H 9750 3250 50  0001 C CNN
	1    9750 3250
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small U25C1
U 1 1 5D21D374
P 8500 1200
F 0 "U25C1" V 8600 1150 50  0000 L CNN
F 1 "0.1uF" V 8400 1150 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 8500 1200 50  0001 C CNN
F 3 "~" H 8500 1200 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 8500 1200 50  0001 C CNN "specs"
	1    8500 1200
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0142
U 1 1 5D21D37A
P 8500 1100
F 0 "#PWR0142" H 8500 950 50  0001 C CNN
F 1 "VCC" V 8500 1200 50  0000 L CNN
F 2 "" H 8500 1100 50  0001 C CNN
F 3 "" H 8500 1100 50  0001 C CNN
	1    8500 1100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0143
U 1 1 5D21D380
P 8500 1300
F 0 "#PWR0143" H 8500 1050 50  0001 C CNN
F 1 "GND" V 8500 1200 50  0000 R CNN
F 2 "" H 8500 1300 50  0001 C CNN
F 3 "" H 8500 1300 50  0001 C CNN
	1    8500 1300
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0144
U 1 1 5D21ED47
P 7600 550
F 0 "#PWR0144" H 7600 400 50  0001 C CNN
F 1 "VCC" V 7700 600 50  0000 L CNN
F 2 "" H 7600 550 50  0001 C CNN
F 3 "" H 7600 550 50  0001 C CNN
	1    7600 550 
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0145
U 1 1 5D21F3DF
P 7600 2150
F 0 "#PWR0145" H 7600 1900 50  0001 C CNN
F 1 "GND" V 7700 2100 50  0000 R CNN
F 2 "" H 7600 2150 50  0001 C CNN
F 3 "" H 7600 2150 50  0001 C CNN
	1    7600 2150
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small U3XC1
U 1 1 5D2246C1
P 8350 4450
F 0 "U3XC1" V 8450 4400 50  0000 L CNN
F 1 "0.1uF" V 8250 4400 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 8350 4450 50  0001 C CNN
F 3 "~" H 8350 4450 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 8350 4450 50  0001 C CNN "specs"
	1    8350 4450
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0146
U 1 1 5D2246C7
P 8250 4450
F 0 "#PWR0146" H 8250 4300 50  0001 C CNN
F 1 "VCC" V 8250 4550 50  0000 L CNN
F 2 "" H 8250 4450 50  0001 C CNN
F 3 "" H 8250 4450 50  0001 C CNN
	1    8250 4450
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0147
U 1 1 5D2246CD
P 8450 4450
F 0 "#PWR0147" H 8450 4200 50  0001 C CNN
F 1 "GND" V 8450 4350 50  0000 R CNN
F 2 "" H 8450 4450 50  0001 C CNN
F 3 "" H 8450 4450 50  0001 C CNN
	1    8450 4450
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small U1C1
U 1 1 5D235D07
P 2000 1150
F 0 "U1C1" V 2100 1100 50  0000 L CNN
F 1 "0.1uF" V 1900 1100 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 2000 1150 50  0001 C CNN
F 3 "~" H 2000 1150 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 2000 1150 50  0001 C CNN "specs"
	1    2000 1150
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0148
U 1 1 5D235D0D
P 2000 1050
F 0 "#PWR0148" H 2000 900 50  0001 C CNN
F 1 "VCC" V 2000 1150 50  0000 L CNN
F 2 "" H 2000 1050 50  0001 C CNN
F 3 "" H 2000 1050 50  0001 C CNN
	1    2000 1050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0149
U 1 1 5D235D13
P 2000 1250
F 0 "#PWR0149" H 2000 1000 50  0001 C CNN
F 1 "GND" V 2000 1150 50  0000 R CNN
F 2 "" H 2000 1250 50  0001 C CNN
F 3 "" H 2000 1250 50  0001 C CNN
	1    2000 1250
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small U3C1
U 1 1 5D238202
P 2350 1150
F 0 "U3C1" V 2450 1100 50  0000 L CNN
F 1 "0.1uF" V 2250 1100 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 2350 1150 50  0001 C CNN
F 3 "~" H 2350 1150 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 2350 1150 50  0001 C CNN "specs"
	1    2350 1150
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0150
U 1 1 5D238208
P 2350 1050
F 0 "#PWR0150" H 2350 900 50  0001 C CNN
F 1 "VCC" V 2350 1150 50  0000 L CNN
F 2 "" H 2350 1050 50  0001 C CNN
F 3 "" H 2350 1050 50  0001 C CNN
	1    2350 1050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0151
U 1 1 5D23820E
P 2350 1250
F 0 "#PWR0151" H 2350 1000 50  0001 C CNN
F 1 "GND" V 2350 1150 50  0000 R CNN
F 2 "" H 2350 1250 50  0001 C CNN
F 3 "" H 2350 1250 50  0001 C CNN
	1    2350 1250
	1    0    0    -1  
$EndComp
NoConn ~ 6400 1400
NoConn ~ 6400 1600
NoConn ~ 5400 1200
NoConn ~ 5400 1100
NoConn ~ 5400 1000
NoConn ~ 5400 900 
Text Label 5400 1800 2    50   ~ 0
cntRST
Text Label 4900 4050 2    50   ~ 0
cntRST
Text Label 6750 3650 2    50   ~ 0
cntRST
Text Label 6050 5900 2    50   ~ 0
cntRST
NoConn ~ 6050 5300
NoConn ~ 6050 5200
NoConn ~ 6050 5100
NoConn ~ 6050 5000
$Comp
L power:VCC #PWR0152
U 1 1 5D1A875E
P 6550 4700
F 0 "#PWR0152" H 6550 4550 50  0001 C CNN
F 1 "VCC" V 6650 4750 50  0000 L CNN
F 2 "" H 6550 4700 50  0001 C CNN
F 3 "" H 6550 4700 50  0001 C CNN
	1    6550 4700
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0153
U 1 1 5D1A9451
P 6550 6200
F 0 "#PWR0153" H 6550 5950 50  0001 C CNN
F 1 "GND" V 6650 6150 50  0000 R CNN
F 2 "" H 6550 6200 50  0001 C CNN
F 3 "" H 6550 6200 50  0001 C CNN
	1    6550 6200
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0154
U 1 1 5D1AA123
P 6050 5500
F 0 "#PWR0154" H 6050 5350 50  0001 C CNN
F 1 "VCC" V 6150 5500 50  0000 L CNN
F 2 "" H 6050 5500 50  0001 C CNN
F 3 "" H 6050 5500 50  0001 C CNN
	1    6050 5500
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small U20C1
U 1 1 5D1AEFCE
P 5650 5400
F 0 "U20C1" V 5750 5350 50  0000 L CNN
F 1 "0.1uF" V 5550 5350 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 5650 5400 50  0001 C CNN
F 3 "~" H 5650 5400 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 5650 5400 50  0001 C CNN "specs"
	1    5650 5400
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0155
U 1 1 5D1AEFD4
P 5650 5300
F 0 "#PWR0155" H 5650 5150 50  0001 C CNN
F 1 "VCC" V 5650 5400 50  0000 L CNN
F 2 "" H 5650 5300 50  0001 C CNN
F 3 "" H 5650 5300 50  0001 C CNN
	1    5650 5300
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0156
U 1 1 5D1AEFDA
P 5650 5500
F 0 "#PWR0156" H 5650 5250 50  0001 C CNN
F 1 "GND" V 5650 5400 50  0000 R CNN
F 2 "" H 5650 5500 50  0001 C CNN
F 3 "" H 5650 5500 50  0001 C CNN
	1    5650 5500
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small U22C1
U 1 1 5D1B420D
P 6450 3050
F 0 "U22C1" V 6550 3000 50  0000 L CNN
F 1 "0.1uF" V 6350 3000 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 6450 3050 50  0001 C CNN
F 3 "~" H 6450 3050 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 6450 3050 50  0001 C CNN "specs"
	1    6450 3050
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0157
U 1 1 5D1B4213
P 6450 2950
F 0 "#PWR0157" H 6450 2800 50  0001 C CNN
F 1 "VCC" V 6450 3050 50  0000 L CNN
F 2 "" H 6450 2950 50  0001 C CNN
F 3 "" H 6450 2950 50  0001 C CNN
	1    6450 2950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0158
U 1 1 5D1B4219
P 6450 3150
F 0 "#PWR0158" H 6450 2900 50  0001 C CNN
F 1 "GND" V 6450 3050 50  0000 R CNN
F 2 "" H 6450 3150 50  0001 C CNN
F 3 "" H 6450 3150 50  0001 C CNN
	1    6450 3150
	1    0    0    -1  
$EndComp
NoConn ~ 6750 3050
NoConn ~ 6750 2950
NoConn ~ 6750 2850
NoConn ~ 6750 2750
$Comp
L power:VCC #PWR0159
U 1 1 5D1B7BE9
P 7250 2450
F 0 "#PWR0159" H 7250 2300 50  0001 C CNN
F 1 "VCC" V 7350 2500 50  0000 L CNN
F 2 "" H 7250 2450 50  0001 C CNN
F 3 "" H 7250 2450 50  0001 C CNN
	1    7250 2450
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0160
U 1 1 5D1B8399
P 7250 3950
F 0 "#PWR0160" H 7250 3700 50  0001 C CNN
F 1 "GND" V 7350 3900 50  0000 R CNN
F 2 "" H 7250 3950 50  0001 C CNN
F 3 "" H 7250 3950 50  0001 C CNN
	1    7250 3950
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0161
U 1 1 5D1BB058
P 6750 3250
F 0 "#PWR0161" H 6750 3100 50  0001 C CNN
F 1 "VCC" V 6850 3250 50  0000 L CNN
F 2 "" H 6750 3250 50  0001 C CNN
F 3 "" H 6750 3250 50  0001 C CNN
	1    6750 3250
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0162
U 1 1 5D1C97A6
P 4900 3650
F 0 "#PWR0162" H 4900 3500 50  0001 C CNN
F 1 "VCC" V 5000 3650 50  0000 L CNN
F 2 "" H 4900 3650 50  0001 C CNN
F 3 "" H 4900 3650 50  0001 C CNN
	1    4900 3650
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0163
U 1 1 5D1CA17E
P 5400 1400
F 0 "#PWR0163" H 5400 1250 50  0001 C CNN
F 1 "VCC" V 5500 1400 50  0000 L CNN
F 2 "" H 5400 1400 50  0001 C CNN
F 3 "" H 5400 1400 50  0001 C CNN
	1    5400 1400
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0164
U 1 1 5D1CBF14
P 5900 600
F 0 "#PWR0164" H 5900 450 50  0001 C CNN
F 1 "VCC" V 6000 650 50  0000 L CNN
F 2 "" H 5900 600 50  0001 C CNN
F 3 "" H 5900 600 50  0001 C CNN
	1    5900 600 
	0    1    1    0   
$EndComp
$Comp
L power:VCC #PWR0165
U 1 1 5D1CC53E
P 5400 2850
F 0 "#PWR0165" H 5400 2700 50  0001 C CNN
F 1 "VCC" V 5500 2900 50  0000 L CNN
F 2 "" H 5400 2850 50  0001 C CNN
F 3 "" H 5400 2850 50  0001 C CNN
	1    5400 2850
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0166
U 1 1 5D1CD45F
P 5400 4350
F 0 "#PWR0166" H 5400 4100 50  0001 C CNN
F 1 "GND" V 5500 4300 50  0000 R CNN
F 2 "" H 5400 4350 50  0001 C CNN
F 3 "" H 5400 4350 50  0001 C CNN
	1    5400 4350
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0167
U 1 1 5D1CDA4A
P 5900 2100
F 0 "#PWR0167" H 5900 1850 50  0001 C CNN
F 1 "GND" V 6000 2050 50  0000 R CNN
F 2 "" H 5900 2100 50  0001 C CNN
F 3 "" H 5900 2100 50  0001 C CNN
	1    5900 2100
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small U23C1
U 1 1 5D1D779C
P 4950 1250
F 0 "U23C1" V 5050 1200 50  0000 L CNN
F 1 "0.1uF" V 4850 1200 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 4950 1250 50  0001 C CNN
F 3 "~" H 4950 1250 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 4950 1250 50  0001 C CNN "specs"
	1    4950 1250
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0168
U 1 1 5D1D77A2
P 4950 1150
F 0 "#PWR0168" H 4950 1000 50  0001 C CNN
F 1 "VCC" V 4950 1250 50  0000 L CNN
F 2 "" H 4950 1150 50  0001 C CNN
F 3 "" H 4950 1150 50  0001 C CNN
	1    4950 1150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0169
U 1 1 5D1D77A8
P 4950 1350
F 0 "#PWR0169" H 4950 1100 50  0001 C CNN
F 1 "GND" V 4950 1250 50  0000 R CNN
F 2 "" H 4950 1350 50  0001 C CNN
F 3 "" H 4950 1350 50  0001 C CNN
	1    4950 1350
	1    0    0    -1  
$EndComp
NoConn ~ 4900 3450
NoConn ~ 4900 3350
NoConn ~ 4900 3250
NoConn ~ 4900 3150
$Comp
L Device:C_Small U21C1
U 1 1 5D1DE6CB
P 4550 3400
F 0 "U21C1" V 4650 3350 50  0000 L CNN
F 1 "0.1uF" V 4450 3350 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 4550 3400 50  0001 C CNN
F 3 "~" H 4550 3400 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 4550 3400 50  0001 C CNN "specs"
	1    4550 3400
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0170
U 1 1 5D1DE6D1
P 4550 3300
F 0 "#PWR0170" H 4550 3150 50  0001 C CNN
F 1 "VCC" V 4550 3400 50  0000 L CNN
F 2 "" H 4550 3300 50  0001 C CNN
F 3 "" H 4550 3300 50  0001 C CNN
	1    4550 3300
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0171
U 1 1 5D1DE6D7
P 4550 3500
F 0 "#PWR0171" H 4550 3250 50  0001 C CNN
F 1 "GND" V 4550 3400 50  0000 R CNN
F 2 "" H 4550 3500 50  0001 C CNN
F 3 "" H 4550 3500 50  0001 C CNN
	1    4550 3500
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small U15C1
U 1 1 5D1EA741
P 3300 7600
F 0 "U15C1" V 3400 7550 50  0000 L CNN
F 1 "0.1uF" V 3200 7550 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 3300 7600 50  0001 C CNN
F 3 "~" H 3300 7600 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 3300 7600 50  0001 C CNN "specs"
	1    3300 7600
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0172
U 1 1 5D1EA747
P 3200 7600
F 0 "#PWR0172" H 3200 7450 50  0001 C CNN
F 1 "VCC" V 3200 7700 50  0000 L CNN
F 2 "" H 3200 7600 50  0001 C CNN
F 3 "" H 3200 7600 50  0001 C CNN
	1    3200 7600
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0173
U 1 1 5D1EA74D
P 3400 7600
F 0 "#PWR0173" H 3400 7350 50  0001 C CNN
F 1 "GND" V 3400 7500 50  0000 R CNN
F 2 "" H 3400 7600 50  0001 C CNN
F 3 "" H 3400 7600 50  0001 C CNN
	1    3400 7600
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small U14C1
U 1 1 5D1ED454
P 3300 7250
F 0 "U14C1" V 3400 7200 50  0000 L CNN
F 1 "0.1uF" V 3200 7200 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 3300 7250 50  0001 C CNN
F 3 "~" H 3300 7250 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 3300 7250 50  0001 C CNN "specs"
	1    3300 7250
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0174
U 1 1 5D1ED45A
P 3200 7250
F 0 "#PWR0174" H 3200 7100 50  0001 C CNN
F 1 "VCC" V 3200 7350 50  0000 L CNN
F 2 "" H 3200 7250 50  0001 C CNN
F 3 "" H 3200 7250 50  0001 C CNN
	1    3200 7250
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0175
U 1 1 5D1ED460
P 3400 7250
F 0 "#PWR0175" H 3400 7000 50  0001 C CNN
F 1 "GND" V 3400 7150 50  0000 R CNN
F 2 "" H 3400 7250 50  0001 C CNN
F 3 "" H 3400 7250 50  0001 C CNN
	1    3400 7250
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small U13C1
U 1 1 5D1EF93D
P 3300 6900
F 0 "U13C1" V 3400 6850 50  0000 L CNN
F 1 "0.1uF" V 3200 6850 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 3300 6900 50  0001 C CNN
F 3 "~" H 3300 6900 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 3300 6900 50  0001 C CNN "specs"
	1    3300 6900
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0176
U 1 1 5D1EF943
P 3200 6900
F 0 "#PWR0176" H 3200 6750 50  0001 C CNN
F 1 "VCC" V 3200 7000 50  0000 L CNN
F 2 "" H 3200 6900 50  0001 C CNN
F 3 "" H 3200 6900 50  0001 C CNN
	1    3200 6900
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0177
U 1 1 5D1EF949
P 3400 6900
F 0 "#PWR0177" H 3400 6650 50  0001 C CNN
F 1 "GND" V 3400 6800 50  0000 R CNN
F 2 "" H 3400 6900 50  0001 C CNN
F 3 "" H 3400 6900 50  0001 C CNN
	1    3400 6900
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0178
U 1 1 5D1F29A8
P 2450 5500
F 0 "#PWR0178" H 2450 5350 50  0001 C CNN
F 1 "VCC" V 2450 5600 50  0000 L CNN
F 2 "" H 2450 5500 50  0001 C CNN
F 3 "" H 2450 5500 50  0001 C CNN
	1    2450 5500
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0179
U 1 1 5D1F2DAB
P 2450 6300
F 0 "#PWR0179" H 2450 6050 50  0001 C CNN
F 1 "GND" V 2450 6200 50  0000 R CNN
F 2 "" H 2450 6300 50  0001 C CNN
F 3 "" H 2450 6300 50  0001 C CNN
	1    2450 6300
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0180
U 1 1 5D1F4E9B
P 1600 5550
F 0 "#PWR0180" H 1600 5400 50  0001 C CNN
F 1 "VCC" V 1500 5550 50  0000 L CNN
F 2 "" H 1600 5550 50  0001 C CNN
F 3 "" H 1600 5550 50  0001 C CNN
	1    1600 5550
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0181
U 1 1 5D1F6A16
P 1600 3650
F 0 "#PWR0181" H 1600 3500 50  0001 C CNN
F 1 "VCC" V 1500 3650 50  0000 L CNN
F 2 "" H 1600 3650 50  0001 C CNN
F 3 "" H 1600 3650 50  0001 C CNN
	1    1600 3650
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0182
U 1 1 5D1F93D4
P 1600 6150
F 0 "#PWR0182" H 1600 6000 50  0001 C CNN
F 1 "VCC" V 1600 6250 50  0000 L CNN
F 2 "" H 1600 6150 50  0001 C CNN
F 3 "" H 1600 6150 50  0001 C CNN
	1    1600 6150
	0    1    1    0   
$EndComp
$Comp
L power:VCC #PWR0183
U 1 1 5D1F9FEF
P 1600 4250
F 0 "#PWR0183" H 1600 4100 50  0001 C CNN
F 1 "VCC" V 1600 4350 50  0000 L CNN
F 2 "" H 1600 4250 50  0001 C CNN
F 3 "" H 1600 4250 50  0001 C CNN
	1    1600 4250
	0    1    1    0   
$EndComp
$Comp
L Device:C_Small U10C1
U 1 1 5D1FEF80
P 2850 5900
F 0 "U10C1" V 2950 5850 50  0000 L CNN
F 1 "0.1uF" V 2750 5850 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 2850 5900 50  0001 C CNN
F 3 "~" H 2850 5900 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 2850 5900 50  0001 C CNN "specs"
	1    2850 5900
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0184
U 1 1 5D1FEF86
P 2850 5800
F 0 "#PWR0184" H 2850 5650 50  0001 C CNN
F 1 "VCC" V 2850 5900 50  0000 L CNN
F 2 "" H 2850 5800 50  0001 C CNN
F 3 "" H 2850 5800 50  0001 C CNN
	1    2850 5800
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0185
U 1 1 5D1FEF8C
P 2850 6000
F 0 "#PWR0185" H 2850 5750 50  0001 C CNN
F 1 "GND" V 2850 5900 50  0000 R CNN
F 2 "" H 2850 6000 50  0001 C CNN
F 3 "" H 2850 6000 50  0001 C CNN
	1    2850 6000
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small U11C1
U 1 1 5D212321
P 3850 4900
F 0 "U11C1" V 3950 4850 50  0000 L CNN
F 1 "0.1uF" V 3750 4850 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 3850 4900 50  0001 C CNN
F 3 "~" H 3850 4900 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 3850 4900 50  0001 C CNN "specs"
	1    3850 4900
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0186
U 1 1 5D212327
P 3850 4800
F 0 "#PWR0186" H 3850 4650 50  0001 C CNN
F 1 "VCC" V 3850 4900 50  0000 L CNN
F 2 "" H 3850 4800 50  0001 C CNN
F 3 "" H 3850 4800 50  0001 C CNN
	1    3850 4800
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0187
U 1 1 5D21232D
P 3850 5000
F 0 "#PWR0187" H 3850 4750 50  0001 C CNN
F 1 "GND" V 3850 4900 50  0000 R CNN
F 2 "" H 3850 5000 50  0001 C CNN
F 3 "" H 3850 5000 50  0001 C CNN
	1    3850 5000
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0188
U 1 1 5D21D06B
P 1650 5050
F 0 "#PWR0188" H 1650 4900 50  0001 C CNN
F 1 "VCC" H 1600 5000 50  0000 L CNN
F 2 "" H 1650 5050 50  0001 C CNN
F 3 "" H 1650 5050 50  0001 C CNN
	1    1650 5050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0189
U 1 1 5D21DA3E
P 2650 5050
F 0 "#PWR0189" H 2650 4800 50  0001 C CNN
F 1 "GND" H 2750 5100 50  0000 R CNN
F 2 "" H 2650 5050 50  0001 C CNN
F 3 "" H 2650 5050 50  0001 C CNN
	1    2650 5050
	-1   0    0    1   
$EndComp
$Comp
L Device:C_Small U6C1
U 1 1 5D223666
P 2150 4700
F 0 "U6C1" V 2250 4650 50  0000 L CNN
F 1 "0.1uF" V 2050 4650 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 2150 4700 50  0001 C CNN
F 3 "~" H 2150 4700 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 2150 4700 50  0001 C CNN "specs"
	1    2150 4700
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0190
U 1 1 5D22366C
P 2050 4700
F 0 "#PWR0190" H 2050 4550 50  0001 C CNN
F 1 "VCC" V 2050 4800 50  0000 L CNN
F 2 "" H 2050 4700 50  0001 C CNN
F 3 "" H 2050 4700 50  0001 C CNN
	1    2050 4700
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0191
U 1 1 5D223672
P 2250 4700
F 0 "#PWR0191" H 2250 4450 50  0001 C CNN
F 1 "GND" V 2250 4600 50  0000 R CNN
F 2 "" H 2250 4700 50  0001 C CNN
F 3 "" H 2250 4700 50  0001 C CNN
	1    2250 4700
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small U7C1
U 1 1 5D22D56F
P 900 4750
F 0 "U7C1" V 1000 4700 50  0000 L CNN
F 1 "0.1uF" V 800 4700 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 900 4750 50  0001 C CNN
F 3 "~" H 900 4750 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 900 4750 50  0001 C CNN "specs"
	1    900  4750
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0192
U 1 1 5D22D575
P 800 4750
F 0 "#PWR0192" H 800 4600 50  0001 C CNN
F 1 "VCC" V 800 4850 50  0000 L CNN
F 2 "" H 800 4750 50  0001 C CNN
F 3 "" H 800 4750 50  0001 C CNN
	1    800  4750
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0193
U 1 1 5D22D57B
P 1000 4750
F 0 "#PWR0193" H 1000 4500 50  0001 C CNN
F 1 "GND" V 1000 4650 50  0000 R CNN
F 2 "" H 1000 4750 50  0001 C CNN
F 3 "" H 1000 4750 50  0001 C CNN
	1    1000 4750
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0194
U 1 1 5D237652
P 1850 3050
F 0 "#PWR0194" H 1850 2800 50  0001 C CNN
F 1 "GND" V 1950 3100 50  0000 R CNN
F 2 "" H 1850 3050 50  0001 C CNN
F 3 "" H 1850 3050 50  0001 C CNN
	1    1850 3050
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small U5C1
U 1 1 5D2402A9
P 2400 2650
F 0 "U5C1" V 2500 2600 50  0000 L CNN
F 1 "0.1uF" V 2300 2600 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 2400 2650 50  0001 C CNN
F 3 "~" H 2400 2650 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 2400 2650 50  0001 C CNN "specs"
	1    2400 2650
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0195
U 1 1 5D2402AF
P 2400 2550
F 0 "#PWR0195" H 2400 2400 50  0001 C CNN
F 1 "VCC" V 2400 2650 50  0000 L CNN
F 2 "" H 2400 2550 50  0001 C CNN
F 3 "" H 2400 2550 50  0001 C CNN
	1    2400 2550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0196
U 1 1 5D2402B5
P 2400 2750
F 0 "#PWR0196" H 2400 2500 50  0001 C CNN
F 1 "GND" V 2400 2650 50  0000 R CNN
F 2 "" H 2400 2750 50  0001 C CNN
F 3 "" H 2400 2750 50  0001 C CNN
	1    2400 2750
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0197
U 1 1 5D2521B9
P 3350 600
F 0 "#PWR0197" H 3350 450 50  0001 C CNN
F 1 "VCC" V 3350 700 50  0000 L CNN
F 2 "" H 3350 600 50  0001 C CNN
F 3 "" H 3350 600 50  0001 C CNN
	1    3350 600 
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0198
U 1 1 5D252CCB
P 3350 1200
F 0 "#PWR0198" H 3350 950 50  0001 C CNN
F 1 "GND" V 3350 1100 50  0000 R CNN
F 2 "" H 3350 1200 50  0001 C CNN
F 3 "" H 3350 1200 50  0001 C CNN
	1    3350 1200
	0    1    1    0   
$EndComp
$Comp
L power:VCC #PWR0199
U 1 1 5D254E4E
P 3050 900
F 0 "#PWR0199" H 3050 750 50  0001 C CNN
F 1 "VCC" V 3050 750 50  0000 L CNN
F 2 "" H 3050 900 50  0001 C CNN
F 3 "" H 3050 900 50  0001 C CNN
	1    3050 900 
	-1   0    0    1   
$EndComp
$Comp
L Device:C_Small UX1C1
U 1 1 5D25F2B9
P 4150 900
F 0 "UX1C1" V 4250 850 50  0000 L CNN
F 1 "0.1uF" V 4050 850 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 4150 900 50  0001 C CNN
F 3 "~" H 4150 900 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 4150 900 50  0001 C CNN "specs"
	1    4150 900 
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0200
U 1 1 5D25F2BF
P 4150 800
F 0 "#PWR0200" H 4150 650 50  0001 C CNN
F 1 "VCC" V 4150 900 50  0000 L CNN
F 2 "" H 4150 800 50  0001 C CNN
F 3 "" H 4150 800 50  0001 C CNN
	1    4150 800 
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0201
U 1 1 5D25F2C5
P 4150 1000
F 0 "#PWR0201" H 4150 750 50  0001 C CNN
F 1 "GND" V 4150 900 50  0000 R CNN
F 2 "" H 4150 1000 50  0001 C CNN
F 3 "" H 4150 1000 50  0001 C CNN
	1    4150 1000
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small UX2C1
U 1 1 5D281C9C
P 4350 2250
F 0 "UX2C1" V 4450 2200 50  0000 L CNN
F 1 "0.1uF" V 4250 2200 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 4350 2250 50  0001 C CNN
F 3 "~" H 4350 2250 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 4350 2250 50  0001 C CNN "specs"
	1    4350 2250
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0202
U 1 1 5D281CA2
P 4350 2150
F 0 "#PWR0202" H 4350 2000 50  0001 C CNN
F 1 "VCC" V 4350 2250 50  0000 L CNN
F 2 "" H 4350 2150 50  0001 C CNN
F 3 "" H 4350 2150 50  0001 C CNN
	1    4350 2150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0203
U 1 1 5D281CA8
P 4350 2350
F 0 "#PWR0203" H 4350 2100 50  0001 C CNN
F 1 "GND" V 4350 2250 50  0000 R CNN
F 2 "" H 4350 2350 50  0001 C CNN
F 3 "" H 4350 2350 50  0001 C CNN
	1    4350 2350
	1    0    0    -1  
$EndComp
NoConn ~ 10550 4950
NoConn ~ 10850 4950
Wire Wire Line
	1750 7000 2050 7000
Wire Wire Line
	1750 7000 1750 7550
Wire Wire Line
	2000 6650 2000 7100
Wire Wire Line
	2000 7100 2050 7100
Wire Wire Line
	1900 7600 2050 7600
Wire Wire Line
	1900 6950 1900 7600
Wire Wire Line
	1200 7700 2000 7700
Wire Wire Line
	2000 7700 2000 7500
Wire Wire Line
	2000 7500 2050 7500
Text Label 9850 1500 2    50   ~ 0
cntRST
Text Label 6650 4150 2    50   ~ 0
cntRST
$Comp
L Device:R R5
U 1 1 5D3D6D3A
P 6800 4150
F 0 "R5" V 6800 4100 50  0000 L CNN
F 1 "100K" V 6900 4050 50  0000 L CNN
F 2 "Resistors_SMD:R_0603" V 6730 4150 50  0001 C CNN
F 3 "~" H 6800 4150 50  0001 C CNN
	1    6800 4150
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR0208
U 1 1 5D3D72F0
P 6950 4150
F 0 "#PWR0208" H 6950 3900 50  0001 C CNN
F 1 "GND" V 6950 4000 50  0000 R CNN
F 2 "" H 6950 4150 50  0001 C CNN
F 3 "" H 6950 4150 50  0001 C CNN
	1    6950 4150
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small U8C1
U 1 1 5D1EA9A9
P 900 5050
F 0 "U8C1" V 1000 5000 50  0000 L CNN
F 1 "0.1uF" V 800 5000 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 900 5050 50  0001 C CNN
F 3 "~" H 900 5050 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 900 5050 50  0001 C CNN "specs"
	1    900  5050
	0    -1   -1   0   
$EndComp
$Comp
L power:VCC #PWR0209
U 1 1 5D1EA9AF
P 800 5050
F 0 "#PWR0209" H 800 4900 50  0001 C CNN
F 1 "VCC" V 800 5150 50  0000 L CNN
F 2 "" H 800 5050 50  0001 C CNN
F 3 "" H 800 5050 50  0001 C CNN
	1    800  5050
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0210
U 1 1 5D1EA9B5
P 1000 5050
F 0 "#PWR0210" H 1000 4800 50  0001 C CNN
F 1 "GND" V 1000 4950 50  0000 R CNN
F 2 "" H 1000 5050 50  0001 C CNN
F 3 "" H 1000 5050 50  0001 C CNN
	1    1000 5050
	0    -1   -1   0   
$EndComp
$Comp
L Device:C_Small U12C1
U 1 1 5D1EF8BA
P 4150 4900
F 0 "U12C1" V 4250 4850 50  0000 L CNN
F 1 "0.1uF" V 4050 4850 50  0000 L CNN
F 2 "Capacitors_SMD:C_0603" H 4150 4900 50  0001 C CNN
F 3 "~" H 4150 4900 50  0001 C CNN
F 4 "X5R, X7R, 10V minimum" H 4150 4900 50  0001 C CNN "specs"
	1    4150 4900
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0211
U 1 1 5D1EF8C0
P 4150 4800
F 0 "#PWR0211" H 4150 4650 50  0001 C CNN
F 1 "VCC" V 4150 4900 50  0000 L CNN
F 2 "" H 4150 4800 50  0001 C CNN
F 3 "" H 4150 4800 50  0001 C CNN
	1    4150 4800
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0212
U 1 1 5D1EF8C6
P 4150 5000
F 0 "#PWR0212" H 4150 4750 50  0001 C CNN
F 1 "GND" V 4150 4900 50  0000 R CNN
F 2 "" H 4150 5000 50  0001 C CNN
F 3 "" H 4150 5000 50  0001 C CNN
	1    4150 5000
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint_Probe TAn1
U 1 1 5D234B91
P 2000 3950
F 0 "TAn1" H 2152 4051 50  0000 L CNN
F 1 "An" H 2152 3960 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-SMD-Pad_Small" H 2200 3950 50  0001 C CNN
F 3 "~" H 2200 3950 50  0001 C CNN
	1    2000 3950
	1    0    0    -1  
$EndComp
Wire Wire Line
	1900 5750 1900 5500
$Comp
L Connector:TestPoint_Probe TBn1
U 1 1 5D259C2A
P 1900 5500
F 0 "TBn1" H 2053 5601 50  0000 L CNN
F 1 "Bn" H 2053 5510 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-SMD-Pad_Small" H 2100 5500 50  0001 C CNN
F 3 "~" H 2100 5500 50  0001 C CNN
	1    1900 5500
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint_Probe TAc1
U 1 1 5D25B495
P 3550 4400
F 0 "TAc1" H 3703 4501 50  0000 L CNN
F 1 "Ac" H 3703 4410 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-SMD-Pad_Small" H 3750 4400 50  0001 C CNN
F 3 "~" H 3750 4400 50  0001 C CNN
	1    3550 4400
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint_Probe TBc1
U 1 1 5D25C1E8
P 3550 5500
F 0 "TBc1" H 3703 5601 50  0000 L CNN
F 1 "Bc" H 3703 5510 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-SMD-Pad_Small" H 3750 5500 50  0001 C CNN
F 3 "~" H 3750 5500 50  0001 C CNN
	1    3550 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3550 4550 3550 4400
Wire Wire Line
	3550 5100 3550 5500
$Comp
L Connector:TestPoint_Probe TCLK1
U 1 1 5D261AC5
P 4000 1750
F 0 "TCLK1" H 4152 1851 50  0000 L CNN
F 1 "CLK" H 4152 1760 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-SMD-Pad_Small" H 4200 1750 50  0001 C CNN
F 3 "~" H 4200 1750 50  0001 C CNN
	1    4000 1750
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint_Probe TUP1
U 1 1 5D268445
P 2550 6950
F 0 "TUP1" H 2702 7051 50  0000 L CNN
F 1 "UP" H 2702 6960 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-SMD-Pad_Small" H 2750 6950 50  0001 C CNN
F 3 "~" H 2750 6950 50  0001 C CNN
	1    2550 6950
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint_Probe TDN1
U 1 1 5D268F8B
P 2550 7450
F 0 "TDN1" H 2702 7551 50  0000 L CNN
F 1 "DOWN" H 2702 7460 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-SMD-Pad_Small" H 2750 7450 50  0001 C CNN
F 3 "~" H 2750 7450 50  0001 C CNN
	1    2550 7450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2600 7050 2600 6950
Wire Wire Line
	2600 6950 2550 6950
Wire Wire Line
	2600 7550 2600 7450
Wire Wire Line
	2600 7450 2550 7450
$Comp
L Connector:TestPoint_Probe TAnXBc1
U 1 1 5D26F221
P 1200 6550
F 0 "TAnXBc1" H 1352 6651 50  0000 L CNN
F 1 "AnXBc" H 1352 6560 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-SMD-Pad_Small" H 1400 6550 50  0001 C CNN
F 3 "~" H 1400 6550 50  0001 C CNN
	1    1200 6550
	1    0    0    -1  
$EndComp
Wire Wire Line
	1200 6550 1200 6650
Connection ~ 1200 6650
$Comp
L Connector:TestPoint_Probe TAcXBn1
U 1 1 5D2715D5
P 1200 7250
F 0 "TAcXBn1" H 1352 7351 50  0000 L CNN
F 1 "AcXBn" H 1352 7260 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-SMD-Pad_Small" H 1400 7250 50  0001 C CNN
F 3 "~" H 1400 7250 50  0001 C CNN
	1    1200 7250
	1    0    0    -1  
$EndComp
Wire Wire Line
	1200 7250 1200 7550
$Comp
L Connector:TestPoint_Probe TRead1
U 1 1 5D27760A
P 7650 4650
F 0 "TRead1" H 7803 4751 50  0000 L CNN
F 1 "read" H 7803 4660 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-SMD-Pad_Small" H 7850 4650 50  0001 C CNN
F 3 "~" H 7850 4650 50  0001 C CNN
	1    7650 4650
	1    0    0    -1  
$EndComp
$Comp
L Connector:TestPoint_Probe TLatch1
U 1 1 5D278D7D
P 8800 4650
F 0 "TLatch1" H 8952 4751 50  0000 L CNN
F 1 "latch" H 8952 4660 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-SMD-Pad_Small" H 9000 4650 50  0001 C CNN
F 3 "~" H 9000 4650 50  0001 C CNN
	1    8800 4650
	1    0    0    -1  
$EndComp
Wire Wire Line
	7850 4750 7850 4650
Wire Wire Line
	7850 4650 7650 4650
Wire Wire Line
	8850 4750 8850 4650
Wire Wire Line
	8850 4650 8800 4650
$Comp
L Connector:TestPoint TPGND1
U 1 1 5D3A97FC
P 10650 4050
F 0 "TPGND1" V 10604 4238 50  0000 L CNN
F 1 "GND" V 10695 4238 50  0000 L CNN
F 2 "Measurement_Points:Measurement_Point_Round-TH_Big" H 10850 4050 50  0001 C CNN
F 3 "~" H 10850 4050 50  0001 C CNN
	1    10650 4050
	0    1    1    0   
$EndComp
Wire Wire Line
	10650 4050 10450 4050
Connection ~ 10450 4050
Wire Wire Line
	1900 3850 1900 3950
Wire Wire Line
	1900 3950 2000 3950
$Comp
L Device:R RIMP1
U 1 1 5D27D3BC
P 4700 2150
F 0 "RIMP1" V 4600 2050 50  0000 L CNN
F 1 "1K" V 4700 2100 50  0000 L CNN
F 2 "Resistors_SMD:R_0603" V 4630 2150 50  0001 C CNN
F 3 "~" H 4700 2150 50  0001 C CNN
	1    4700 2150
	-1   0    0    1   
$EndComp
Wire Wire Line
	4000 1750 4000 1600
Connection ~ 4000 1750
Text Label 4700 2000 0    50   ~ 0
CLK
$Comp
L power:GND #PWR0213
U 1 1 5D28AF46
P 4700 2300
F 0 "#PWR0213" H 4700 2050 50  0001 C CNN
F 1 "GND" V 4700 2200 50  0000 R CNN
F 2 "" H 4700 2300 50  0001 C CNN
F 3 "" H 4700 2300 50  0001 C CNN
	1    4700 2300
	1    0    0    -1  
$EndComp
Text Label 7850 4950 3    50   ~ 0
CLK
Text Label 8350 4950 3    50   ~ 0
CLK
$Comp
L power:GND #PWR0204
U 1 1 5D42109B
P 4950 7200
F 0 "#PWR0204" H 4950 6950 50  0001 C CNN
F 1 "GND" V 4950 7100 50  0000 R CNN
F 2 "" H 4950 7200 50  0001 C CNN
F 3 "" H 4950 7200 50  0001 C CNN
	1    4950 7200
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR0205
U 1 1 5D4215AF
P 4950 6200
F 0 "#PWR0205" H 4950 5950 50  0001 C CNN
F 1 "GND" V 4950 6100 50  0000 R CNN
F 2 "" H 4950 6200 50  0001 C CNN
F 3 "" H 4950 6200 50  0001 C CNN
	1    4950 6200
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR03
U 1 1 5D435F70
P 8400 3700
F 0 "#PWR03" H 8400 3450 50  0001 C CNN
F 1 "GND" V 8500 3650 50  0000 R CNN
F 2 "" H 8400 3700 50  0001 C CNN
F 3 "" H 8400 3700 50  0001 C CNN
	1    8400 3700
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR01
U 1 1 5D4367E7
P 7100 1850
F 0 "#PWR01" H 7100 1600 50  0001 C CNN
F 1 "GND" V 7200 1800 50  0000 R CNN
F 2 "" H 7100 1850 50  0001 C CNN
F 3 "" H 7100 1850 50  0001 C CNN
	1    7100 1850
	1    0    0    -1  
$EndComp
Text Label 9950 2450 3    50   ~ 0
RST
$Comp
L power:GND #PWR02
U 1 1 5D44B03A
P 10050 2450
F 0 "#PWR02" H 10050 2200 50  0001 C CNN
F 1 "GND" H 10100 2300 50  0000 R CNN
F 2 "" H 10050 2450 50  0001 C CNN
F 3 "" H 10050 2450 50  0001 C CNN
	1    10050 2450
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J8
U 1 1 5D44CDC9
P 9950 2250
F 0 "J8" V 9914 2062 50  0000 R CNN
F 1 "RESET" V 9823 2062 50  0000 R CNN
F 2 "additional_connectors:Connectors_JST_B2B-PH-K" H 9950 2250 50  0001 C CNN
F 3 "~" H 9950 2250 50  0001 C CNN
F 4 "455-1704-ND" V 9950 2250 50  0001 C CNN "digikey"
F 5 "455-1719-ND" V 9950 2250 50  0001 C CNN "digikey_alt"
F 6 "SPH-002T-P0.5S (455-1127-1-ND), PHR-2 (455-1165-ND)" V 9950 2250 50  0001 C CNN "additional parts"
	1    9950 2250
	0    -1   -1   0   
$EndComp
$Comp
L Mechanical:Fiducial FID1
U 1 1 5D51D66B
P 2950 3450
F 0 "FID1" H 3035 3496 50  0000 L CNN
F 1 "Fiducial" H 3035 3405 50  0000 L CNN
F 2 "Fiducials:Fiducial_0.5mm_Dia_1mm_Outer" H 2950 3450 50  0001 C CNN
F 3 "~" H 2950 3450 50  0001 C CNN
	1    2950 3450
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:Fiducial FID3
U 1 1 5D51DA7F
P 2950 3650
F 0 "FID3" H 3035 3696 50  0000 L CNN
F 1 "Fiducial" H 3035 3605 50  0000 L CNN
F 2 "Fiducials:Fiducial_0.5mm_Dia_1mm_Outer" H 2950 3650 50  0001 C CNN
F 3 "~" H 2950 3650 50  0001 C CNN
	1    2950 3650
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:Fiducial FID5
U 1 1 5D51DCD0
P 2950 3850
F 0 "FID5" H 3035 3896 50  0000 L CNN
F 1 "Fiducial" H 3035 3805 50  0000 L CNN
F 2 "Fiducials:Fiducial_0.5mm_Dia_1mm_Outer" H 2950 3850 50  0001 C CNN
F 3 "~" H 2950 3850 50  0001 C CNN
	1    2950 3850
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:Fiducial FID2
U 1 1 5D51DF2B
P 3500 3450
F 0 "FID2" H 3585 3496 50  0000 L CNN
F 1 "Fiducial" H 3585 3405 50  0000 L CNN
F 2 "Fiducials:Fiducial_0.5mm_Dia_1mm_Outer" H 3500 3450 50  0001 C CNN
F 3 "~" H 3500 3450 50  0001 C CNN
	1    3500 3450
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:Fiducial FID4
U 1 1 5D51E157
P 3500 3650
F 0 "FID4" H 3585 3696 50  0000 L CNN
F 1 "Fiducial" H 3585 3605 50  0000 L CNN
F 2 "Fiducials:Fiducial_0.5mm_Dia_1mm_Outer" H 3500 3650 50  0001 C CNN
F 3 "~" H 3500 3650 50  0001 C CNN
	1    3500 3650
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:Fiducial FID6
U 1 1 5D51E4F2
P 3500 3850
F 0 "FID6" H 3585 3896 50  0000 L CNN
F 1 "Fiducial" H 3585 3805 50  0000 L CNN
F 2 "Fiducials:Fiducial_0.5mm_Dia_1mm_Outer" H 3500 3850 50  0001 C CNN
F 3 "~" H 3500 3850 50  0001 C CNN
	1    3500 3850
	1    0    0    -1  
$EndComp
$EndSCHEMATC
