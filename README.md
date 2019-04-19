# diginucleic-acid

This is a personal project that allows the creation and editing of files that store nucleotides in two bits. These nucleotides can either belong to DNA or RNA.

When editing the sequence of nucleotides, only the A, C, G, T and U keys will work (although T and U will replace eachother depending on whether the file is storing DNA (T) or RNA (U)).

The file will also allow for storing a description of the sequence in a Markdown-compatible format.

The initial version will be a Python 3 script using tkinter for the GUI (if you're using a Linux distro like Manjaro, you may need to install Tk and/or Python 3 before it will work.)

Eventually, I plan on creating a C/C++ version, but sadly my skills with that language aren't that good yet (and I don't know what the GUI libraries are for Linux and Windows).

This project is open source and licensed under GPLv2 (reason for that specific version being that I'm okay with contributors wanting to rescind their code).