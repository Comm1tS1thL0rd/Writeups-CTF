from scapy.all import rdpcap

def extract_hex_from_pcap(a):
    packets = rdpcap(a)
    hex_data = []

    for packet in packets:
        raw_bytes = bytes(packet)
        hex_data.append(raw_bytes.hex())

    return hex_data

if __name__ == "__main__":
    pcap_file = "ur_a.pcap"
    b  = "bulbasaur.txt"

    hex_output = extract_hex_from_pcap(pcap_file)

    with open(b , "w") as f:
        for hex_str in hex_output:
            f.write(f"{hex_str}\n")
