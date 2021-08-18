import pefile

pe = pefile.PE("C://Program Files (x86)//Audacity//audacity.exe")

pe.print_info() 