def parse_can_id(hex_id):
    """
    Parse a 29-bit CAN ID into Priority, PGN, and Source Address.
    """
    can_id = int(hex_id, 16)
    
    # In J1939, 29-bit ID structure:
    # 3 bits Priority | 1 bit Reserved | 1 bit Data Page | 8 bits PF | 8 bits PS | 8 bits SA
    
    priority = (can_id >> 26) & 0x07
    pgn = (can_id >> 8) & 0x3FFFF  # Extracting PF + PS
    source_address = can_id & 0xFF
    
    return priority, pgn, source_address

def decode_j1939_data(pgn, hex_data):
    """
    Basic decoder for specific J1939 PGNs.
    """
    data_bytes = bytes.fromhex(hex_data.replace(" ", ""))
    
    if pgn == 61444:  # EEC1
        # Engine Speed (SPN 190): Bytes 4-5, 0.125 RPM/bit
        raw_val = int.from_bytes(data_bytes[3:5], byteorder='little')
        rpm = raw_val * 0.125
        return f"Engine Speed: {rpm:.2f} RPM"
    
    elif pgn == 65262:  # ET1
        # Coolant Temp (SPN 110): Byte 1, -40 degC offset
        raw_val = data_bytes[0]
        temp = raw_val - 40
        return f"Coolant Temp: {temp} degC"
        
    elif pgn == 65265:  # CCVS
        # Wheel-Based Vehicle Speed (SPN 84): Bytes 2-3, 1/256 km/h/bit
        raw_val = int.from_bytes(data_bytes[1:3], byteorder='little')
        speed = raw_val / 256.0
        return f"Vehicle Speed: {speed:.2f} km/h"
        
    return "Unknown PGN / Data not implemented"

def main():
    # Sample Test Cases (Timestamp, CAN ID, Data)
    logs = [
        ("0CF00400", "F1 FF A9 C6 26 FF FF FF"),  # PGN 61444 (EEC1)
        ("18FEEE00", "D0 FF FF FF FF FF FF FF"),  # PGN 65262 (ET1)
        ("18FEF100", "7D 5B 1A FF FF FF FF FF")   # PGN 65265 (CCVS)
    ]
    
    print(f"{'CAN ID':<10} | {'PGN':<6} | {'SA':<4} | {'Decoded Value'}")
    print("-" * 55)
    
    for hex_id, hex_data in logs:
        prio, pgn, sa = parse_can_id(hex_id)
        value = decode_j1939_data(pgn, hex_data)
        print(f"{hex_id:<10} | {pgn:<6} | {sa:02X} | {value}")

if __name__ == "__main__":
    main()
