# Hot Stuff | 0xBlue

- Description: The local Konica Minolta printer overheated. Can you find out why?

- Hint1: The point of the chall isn't to get the decoder working
- Hint2: https://github.com/koenkooi/foo2zjs/blob/master/lavadecode.c

corrupt.lava:/attachments/Hot_Stuff/corrupt.lava

# Write up

The attached file is a LAVAFLOW file for Konica Minolta printers. LAVAFLOW files use text to separate options for the printers - ```&l3X``` means make 3 copies, ```&u1200D``` means an ```X RESOLUTION``` of 1200(I assume that's 1200 DPI), etc. All of the 3-digit printer options in ```corrupt.lava``` are actually octal values that translate to ASCII letters. You can solve it with ```strings corrupt.lava``` and plugging the first 11 3-digit values you see into CyberChef with "To Octal"

# Flag - n00bz{floorislava}
