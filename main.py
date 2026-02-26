from ring_network import RingNetwork

def main():
    # Create Ring Network object
    ring = RingNetwork()

    # Add IoT Nodes
    node_ids = [10, 25, 5, 40, 15]

    for node_id in node_ids:
        ring.add_node(node_id)

    # Display Ring Structure
    print("\nRing Structure:")
    ring.display_ring()

    # Start Leader Election
    print("\nStarting Leader Election...")
    ring.elect_leader(25)


if __name__ == "__main__":
    main()