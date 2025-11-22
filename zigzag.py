import time, sys, random

indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not

# FITUR 1: Daftar Kode Warna ANSI (Untuk terminal)
colors = [
    '\033[91m', # Merah
    '\033[92m', # Hijau
    '\033[93m', # Kuning
    '\033[94m', # Biru
    '\033[95m', # Ungu
    '\033[96m'  # Cyan
]
RESET_COLOR = '\033[0m' # Reset warna ke default

# FITUR 2: Daftar variasi simbol
symbols = ['********', '########', '@@@@@@@@', '~~~~~~~~', '<><><><>', '========']
current_symbol = symbols[0]

try:
    while True: # The main program loop
        
        # Memilih warna berdasarkan posisi indentasi (menciptakan efek pelangi bergerak)
        current_color = colors[indent % len(colors)]
        
        print(' ' * indent, end='')
        # Mencetak dengan Warna + Simbol + Reset Warna
        print(current_color + current_symbol + RESET_COLOR)
        
        time.sleep(0.1) # Pause for 1/10th of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False
                # Ganti simbol secara acak saat mentok kanan
                current_symbol = random.choice(symbols) 
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
                # Ganti simbol secara acak saat mentok kiri
                current_symbol = random.choice(symbols)

except KeyboardInterrupt:
    sys.exit()