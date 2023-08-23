# 1. Information Content and Entropy

---

A. Given an unknown 3-bit binary number, how much information is given, if you know the binary number contains exactly two 1's?

3 bits = 2^3 = 8 possible values

exactly two 1's = 011, 101, 110 = 3 possible states

log2(8/3) = 1.415 bits of information given

---

B. You are then given that the number is odd, how much total information have you been given?

since 011 and 101 are odd

log2(3/2) = 0.585 bits

---

C. Please give the entropy for the flipping of an unfair coin, where p(HEADS) = 0.6 .

H(X) = (1-0.6)*log2(1/(1-0.6)) + 0.6*log2(1/0.6) = 0.971 bits

---

D. A single decimal digit is chosen at random, with value of 0 when mod 3. How much info has been given?

from 10 possible values (0...9) to 4 (0,3,6,9)

log2(10/4) = 1.322 bits

---

E. X is an unknown 8-bit binary number. You are given another 8-bit binary number,
10101100, and told that the Hamming distance between X and 10101100 is one. How
many bits of information about X have you been given?

since the Hamming distance between X and 10101100 is one, that gives us the following choices:

8 bits = 2^8 = 256 choices

10101100 has 8 choices with Hamming distance 1

log2(256/8) = 5 bits

---

F. We wish to transmit messages comprised of the four symbols shown below with their
associated probabilities and 5-bit fixed-length encoding.

Symbol p(symbol) encoding
α 0.5 00000
β 0.125 11100
γ 0.25 11011
δ 0.125 10111

An unknown symbol is received and you are told it’s not δ. How much information have
you received?

p(not delta) = (1-0.125)

log2(1 / (1-0.125)) = 0.193 bits

---

G. When transmitting a message comprised of these four symbols with the probabilities as
given above, what is the expected amount information received when you are told the
next symbol in the message?

0.5*log2(1/0.5) + 2*0.125*log2(1/0.125 + 0.25*log2(1/0.25) = 1.75 bits

---

H. You are given an unknown 5-bit binary number. You are then told that the first and last
bits are the same. How much information have you been given?

5 bits = 2^5 = 32 possible choices

first and last bits are the same, leaving 3 bits unknown, 2^3 * 2 = 16 choices
1xxx1 and 0xxx0

log2(32/16) = 1 bit

---

I. I’ve randomly selected a letter from the alphabet and tell you that my selection is neither
“X”, “Y”, nor “Z”. How much information have I given you about my letter?

26 possible choices (A..Z) - 3 (not X,Y,Z) = 23 choices left

log2(26/23) = 0.177 bits

---

J. I make up a random 4-bit two’s complement number by flipping a fair coin to determine
each bit. You’re trying to guess the number. If I tell you that the number is positive (>
0), how many bits of information have I given you? Be precise; you may answer by a
formula or a number.

for positive numbers in two's complement, the leading bit is always 0 (since 0 * -2^n = 0)

xxxx -> 0xxx

we go from 4 bits, 2^4 = 16 choices
to 3 bits, 2^3 = 8
the number is greater than 0, we are left with 7 choices

log2(16/7) = 1.193 bits

---

# 2. Two’s Complement

---

A. What is the 6-bit two’s complement representation of the decimal number -21?

21 = 010101
     ------
     101010
         +1
   = ------
     101011 = -21

---

B. What is the hexadecimal representation for decimal -51 encoded as an 8-bit two’s
complement number?

51 = 00110011
     --------
     11001100
           +1
   = --------
     11001101 = -51 = 0xCD

---

C. The hexadecimal representation for an 8-bit two’s complement number is 0xD6. What is
its decimal representation?

0xD6 = 11010110 = -2^7 + 2^6 +2^4 + 2^2 + 2^1 = -42

---

D. Since the start of official pitching statistics in 1988, the highest number of pitches in a
single game has been 172. Assuming that remains the upper bound on pitch count, how
many bits would we need to record the pitch count for each game as a two’s complement
binary number?

log2(172) = 7.43 , at least 8 bits are needed.
To account for two's compliment, we add an extra bit, giving us 9 bits.

Highest positive value using two's complement in 8-bit is:

01111111 or 2^8 - 1 = 255

---

E. Can the value of the sum of two 2’s complement numbers 0xB3 + 0x47 be represented
using an 8-bit 2’s complement representation? If so, what is the sum in hex? If not, write
NO.

0xB3 = 10110011
0x47 = 01000111 +
       --------
       11111010 = 0xFA

---

F. Can the value of the sum of two 2’s complement numbers 0xB3 + 0xB1 be represented
using an 8-bit 2’s complement representation? If so, what is the sum in hex? If not, write
NO.

0xB3 = 10110011
0xB1 = 10110001 +
       --------
      101100100
      ^ OVERFLOW , so NO.

---

G. Please compute the value of the expression 0xBB – 8 using 8-bit two’s complement
arithmetic and give the result in decimal (base 10).

0xBB = 10111011
8 = 00001000
-8 = 11111000

0xBB + (-8) = 10111011
              11111000 +
              --------
           (1)10110011 = -77

---

H. What is the smallest (most negative) integer that can be represented as an 8-bit two’s-
complement integer? Give your answer as a decimal integer.

1000 0000 = -2**7 + 0 + ... + 0 = -128

---

I. The following operations are performed on an 8-bit adder. Give the 8-bit sum produced
for each, in hexadecimal.

0xF0 + 0x34 = 11110000
              00110100 +
              --------
           (1)00100100 = 0x24

0xF0 + 0x80 = 11110000
              10000000 +
              --------
           (1)01110000 = 0x70

---

J. Using a 5-bit two’s complement representation, what is the range of integers that can be
represented with a single 5-bit quantity?

-2^4 to 2^4 - 1 = [-16...15]

---

K. Consider the following subtraction problem where the operands are 5-bit two’s
complement numbers. Compute the result and give the answer as a decimal (base 10)
number.

10101 - 00011
01011         -> -11 - 3 = -14
=(-)11  = 3

---

# 3. Variable-length Encodings

---

A. Given a variable X that can take on one of four values A, B, C, or D with the following
probabilities.

Symbol Probability
A 0.5
B 0.3
C 0.1
D 0.1

If you encoded this variable using a Huffman encoding, how many bits would be in the
encoding of each of the symbols?

 /\    A = 1 bit
A /\   B = 2 bits
 B /\  C & D = 3 bits
  C  D

---

For each of the probability distributions for symbols A-E, select the Huffman encoding tree or
trees that could result from running Huffman’s algorithm on those probability distributions.

B. p(A) = 0.3, p(B) = 0.3, p(C) = 0.2, p(D) = 0.1, p(E) = 0.1. Tree(s): #2
C. p(A) = 0.6, p(B) = 0.1, p(C) = 0.1, p(D) = 0.1, p(E) = 0.1. Tree(s): #3
D. p(A) = 0.5, p(B) = 0.15, p(C) = 0.15, p(D) = 0.1, p(E) = 0.1. Tree(s): #2 and #3
E. p(A) = 0.5, p(B) = 0.2, p(C) = 0.15, p(D) = 0.05, p(E) = 0.1. Tree(s): #1

---

Baseball loves statistics! There are many different types of pitches that a pitcher can throw – the
table below shows the probability for each type of pitch during 2014.

Type of pitch Probability
Fastball 0.34
Change-up 0.14
Curveball 0.08
Slider 0.28
Other 0.16

F. How much information have you received when learning that
particular pitch was NOT a fastball? You can express your
answer as a formula if you wish.

log2(1/(1-0.34)) = 0.6 bits

G. To save on storage costs, Major League Baseball would like to use an optimal variable-
length code to record, one at a time, the type of each pitch (i.e., to record one of the 5
types shown in the table above). Use Huffman’s algorithm to derive such a code and list
the resulting binary encodings below.

    ____
   /    \     Fastball = 00
  /\    /\    Slider = 01
 /\ O  F  S   Other = 10
C cU          Curveball = 111
              Changeup = 110

---

H. The table below shows the 2012-13 enrollments in the various EECS majors. To save a
bit of space in their database the department would like to use a variable-length Huffman
code to encode a student’s choice of major. For each of the four majors, please give the
encoding the department should use.

Major Count p p log2(1/p)
6-1 74 0.09 0.30
6-2 387 0.44 0.52
6-3 360 0.41 0.53
6-7 54 0.06 0.25
Total 875 1.00 1.60


    /\     6-2 = 0
   /\6-2   6-3 = 10
  /\6-3    6-7 = 111
6-7 6-1    6-1 = 110

---

I. We wish to transmit messages comprised of the four symbols shown below with their
associated probabilities and 5-bit fixed-length encoding

Symbol p(symbol) encoding
α 0.5 00000
β 0.125 11100
γ 0.25 11011
δ 0.125 10111

Huffman’s algorithm is used to construct a variable-length code for the four symbols for
transmitting a single symbol at a time. The resulting encoding could be

(1) α: 00, β: 01, γ: 10, δ: 10
(2) α: 00, β: 01, γ: 100, δ: 101
(3) α: 1, β: 01, γ: 000, δ: 001
(4) α: 0, β: 110, γ: 01, δ: 111
(5) none of the above

    /\   a = 0
   /\ a  V = 10
  /\ V   d = 110
 B  d    B = 111

The answer is (5), the closest is (4) but V shares a path with a, making it ambiguous.

---

NerdLink is a new web-based startup that aims to keep MIT EECS students in touch with their
parents. NerdLink streamlines parental communication by providing each student with an online
choice of one of the five messages, then automatically fills in boilerplate and emails the parent a
long and charming version of the message. The five messages, and their relative probabilities, are
listed below:

Message # Message to parents p(Message)
M1 Send money! 60%
M2 I love this course called 6.004 8%
M3 I’m changing my major to Poetry 2%
M4 I’m getting a 5.0 this term! 1%
M5 Nothing much is new… (none of the above) 29%

NerdLink’s initial implementation conveyed each message using a fixed-length code.

J. What is the average number of bits needed to convey a message, using a fixed-length code?

for 5 messages, log2(5) = 2.322, so 3 bits is needed to encode

K. Given the probability distribution of the messages, what is the actual amount of information
conveyed by message M5? Your answer may be a formula.

using the formula for information -> log2(1/0.29) = 1.79 bits

L. To enable error correction, the fixed-length code for a given message is sent five times.
Using the five copies of the received message, in the worst case how many bit errors can be
corrected at the receiver?

Since each message is replicated 5 times, (5-1)/2 = 2 errors can be corrected

NerdLink, wanting to economize on communication costs, has hired you as a consultant to design
a Huffman code for sending the messages.

M. Give the number of bits sent by your Huffman code for each message (M1 though M5), and
the average number of bits transmitted per message using your code (a formula will be fine).


     /\    M1 = 0 -> 1 bit
    /\ M1  M2 = 110 -> 3 bits
   /\ M5   M3 = 1110 -> 4 bits
  /\ M2    M4 = 1111 -> 4 bits
 M4 M3     M5 = 10 -> 2 bits

0.6*1 + 0.08*3 + 0.02*4 + 0.01*4 + 0.29*2 = 1.54 bits

---

The Registrar’s office would like to encode the letter grades (A, B, C, D, F) from a large GIR
with 1000 students. They plan to encode each grade separately using a variable-length code. An
analysis of previous terms has produced the following table of grade probabilities. In case it’s
useful, a thoughtful former 6.004 student has augmented the table by computing p*log2(1/p) for
each grade.

Grade p p*log2(1/p)
A 0.24 0.49
B 0.35 0.53
C 0.21 0.47
D 0.13 0.38
F 0.07 0.27
Totals 1.00 2.14

N. Use Huffman’s algorithm to construct an optimal variable-length encoding.

     _._      A = 00
    /   \     B = 01
   /\   /\    C = 10
  /\ C B  A   D = 110
 F  D         F = 111


O. Two 6.004 students have proposed competing variable-length codes. Alice says that
encoding 1000 grades using her code will, on the average, produce messages of 2200 bits.
Bob says that encoding 1000 grades using his code will, on the average, produce messages
of 1950 bits. Which of the following is your best response when the Registrar asks your
opinion?

(A) Choose Bob’s: it has the shorter average length
(B) Choose Alice’s: more bits means more information is transmitted
(C) Choose Bob’s: Bob’s average message length is less than the information entropy
(D) Choose Alice’s: Bob’s average message length is less than the information entropy
(E) Choose neither: a fixed-length code will have lower average message size

Best Choice (A through E): (D)

---

# 4. Error Detection and Correction

---

A. A message about the suit of a card is sent using the encoding shown at
the right. Using this encoding, how many bit errors can be detected?
How many bit errors can be corrected?

Club: 000
Diamond: 011
Heart: 101
Spade: 110

None. The min Hamming distance is 2. Detected bits are 2-1 = 1, bits corrected are (2-1)/2 = 0

---

B. A message about the suit of a card is sent using the encoding shown at
the right. Give an example of a 5-bit received message with an
uncorrectable single-bit error or write NONE if all single-bit errors can
be corrected.

Heart: 00000
Diamond: 11001
Spade: 10111
Club: 01011

Diamond and Club have a Hamming distance of 2. Therefore, if a bit error occurs, it cannot be corrected.

---

C. The MIT baseball coach likes to record the umpire’s call for each pitch (one of “strike”,
“ball” or “other”). Worried that bit errors might corrupt the records archive, he proposes
using the following 5-bit binary encoding for each of the three possible entries:

Strike 11111
Ball 01101
Other 00000

Using this encoding what is the largest number of bit errors that be detected when
examining a particular record? The largest number of bit errors that can be corrected?

The min Hamming distance is 2 (compare Strike to Ball encoding).
Therefore, we can detect 2-1 = 1 bit errors, and correct (2-1)/2 = 0 bit errors.

---

D. When transmitting the information about EECS majors over a noisy
communication link, the department has chosen to use the 7-bit
encoding shown on the right in the hopes that they’ll be able to correct
multiple-bit errors during transmission. Using this code, how many bit
errors in a message about a single major will the receiver be able to
correct?

6-1: 0101010
6-2: 1001100
6-3: 0110001
6-7: 1010010

The min Hamming distance is 4. They can correct (4-1)/2 = 1 bit error

---

E. We wish to transmit messages comprised of the four symbols shown below with their
associated probabilities and 5-bit fixed-length encoding

Symbol p(symbol) encoding
α 0.5 00000
β 0.125 11100
γ 0.25 11011
δ 0.125 10111

If we transmit messages using the 5-bit fixed-length encoding shown above, will it be
possible to perform single-bit error detection and correction at the receiver?

Since the min Hamming distance is 2, 1 bit error detection would be possible, but correction would not be. 

---

F. What is the Hamming distance between the encodings for A and B?
Using an encoding scheme with this Hamming distance, how many bits
of error can be detected? How many bits of error can be corrected?

A: 010010
B: 110101

The min Hamming distance is 4. 4-1 = 3 bit errors can be detected, and (4-1)/2 = 1 bit errors can be corrected.

---

An internet Sudoku gaming site transmits messages containing nine data bits and seven parity
bits, arranged in a rectangle as follows:

D00 D01 D02 P0x
D10 D11 D12 P1x
D20 D21 D22 P2x
Px0 Px1 Px2 Pxx

Each Dij in the above diagram indicates a data bit, equally likely to be a 0 or 1. Each Pux and Pxj is an odd parity bit chosen to make the total number of 1s in the ith row or jth column, respectively, odd. Pxx is an odd parity bit chosen to make the total number of 1s in the entire transmission odd. Thus in an error-free transmission, the total number of 1s in 4-bit columns 0 thru 2 and 4-bit rows
0 thru 2, as well as in the entire 16-bit transmission, is odd.

Note that each 9-bit data word determines a unique 16-bit valid codeword to be transmitted.

G. What is the minimum Hamming distance between valid codewords? [Hint: flipping one
bit of the data word changes how many bits of the codeword?]

If any one of Dij 1's were flipped to being even, then there would be 3 parity bits to make sure it goes odd, which makes me think that the min Hamming distance is 4.

Each of the following represents a transmission received, with at most a single-bit error. For each
message, circle the bit, if any, that was changed due to a transmission error.

H. 1 0 1 1    I. 1 0 1 1    J.(0)1 0 1    K. 0 1 0 0
   0 1 1 1       1 1 0 1       0 0 1 0       1 0 1 1
   1 1 0 1       0 1 1 1       1 1 0 1       0 1 1 1
   1 1 1 1       1(0)1 1       1 1 0 0       0 1 1(1)

    VALID        PARITY         DATA      UNIVERSAL PARITY
                  ERROR         ERROR         ERROR
