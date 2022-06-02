
# Hashing

This program uses python language to hash the string taken as input
from the user. The string is incremented by numbers till its hash value is
lower than: 0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

Along with this time library is imported to calculate the time taken 
to find the 1st hash value for the string increment system. 

I had imported hashlib to use SHA 256 which was used to produce the required hashing value.
I had run the program on google colab.


Expected output from string input:


Input string: iitk
required string: iitk1217060

hash value: 00000bde24704b17d1531816354d01810b1e6f01b1ea38e0c53d5fc5f3bfd70a

nonce value: 1217060

time=5.233118295669556 (may differ from system to system)
