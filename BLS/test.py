import hashlib
from blspy import PrivateKey, AugSchemeMPL, G1Element, G2Element

def generate_keys(seed):
    """Generate a BLS private and public key."""
    # Hash the seed to ensure it is 32 bytes long
    hashed_seed = hashlib.sha256(seed).digest()
    private_key = AugSchemeMPL.key_gen(hashed_seed)
    public_key = private_key.get_g1()
    return private_key, public_key

def sign_message(private_key, message):
    """Sign a message using the private key."""
    return AugSchemeMPL.sign(private_key, message)

def aggregate_signatures(signatures):
    """Aggregate multiple BLS signatures."""
    return AugSchemeMPL.aggregate(signatures)

def aggregate_public_keys(public_keys):
    """Aggregate multiple public keys."""
    # Aggregate G1 elements by summing them
    return sum(public_keys, G1Element())

def verify_aggregate_signature(aggregate_sig, agg_pub_key, messages, public_keys):
    """Verify an aggregated BLS signature."""
    return AugSchemeMPL.aggregate_verify(public_keys, messages, aggregate_sig)

# Example Usage
if __name__ == "__main__":
    # Example seeds and messages
    seeds = [b"seed1", b"seed2", b"seed3"]
    messages = [b"message1", b"message2", b"message3"]

    private_keys = []
    public_keys = []
    signatures = []

    # Generate keys and signatures for each participant
    for seed, message in zip(seeds, messages):
        priv_key, pub_key = generate_keys(seed)
        private_keys.append(priv_key)
        public_keys.append(pub_key)
        signatures.append(sign_message(priv_key, message))

    # Aggregate signatures and public keys
    agg_sig = aggregate_signatures(signatures)
    agg_pub_key = aggregate_public_keys(public_keys)

    # Verify the aggregated signature
    is_valid = AugSchemeMPL.aggregate_verify(public_keys, messages, agg_sig)
    print("Aggregate Signature Valid:", is_valid)
