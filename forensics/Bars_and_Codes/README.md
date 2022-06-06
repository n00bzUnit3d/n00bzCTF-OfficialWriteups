# Bars_and_Codes | Thxjxs

- Description: John and Sebastian are always arguing over one thing or another. This time round, John is of the opinion that a certain type of visual representation of files looks cooler while Sebastian argues that his favourite, QR Codes, look cooler. Unable to resolve this quarrel on their own, they went to their good friend Amaagah, who knew a fair bit about these topics. Amaagah, after giving it some thought, gave both of them a file which confused the two of them. Will you help John and Sebastian to settle their debate once and for all?

- Hint (can be made public later on): The visual representation that John perfers are spectograms.

QRCode.png:/attachments/Bars_and_codes/qrcode.png

# Write up

We are given a `.png` file which contains a QR code. Naturally one would assume then that Amaagah means to say that QR codes are better, and is in favour of Sebastian's opinion. However, on scanning the QR Code or using [zbarimg](https://manpages.ubuntu.com/manpages/bionic/man1/zbarimg.1.html), we get a link which provides us with a `.wav` file. The audio file makes no sense on playing it so naturally, we open it with Audacity or Sonic Visualiser and switch to the spectrogram to get the flag easily (this is also what the hint suggests); we just need to wrap the flag.

# Flag - n00bz{sp3ct09r4m5_4r3_c00l3r_th4n_b4rc0d35}
