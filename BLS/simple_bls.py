from blspy import PrivateKey, AugSchemeMPL
import os

# Generate a secure random seed of 32 bytes (or provide a custom 32-byte seed)
seed = os.urandom(32)  # Random secure seed
# Alternatively, use: seed = b"your_32_byte_seed________________"[:32]

# Generate a private key using the seed
private_key = AugSchemeMPL.key_gen(seed)

# Derive the corresponding public key
public_key = private_key.get_g1()

# Message to be signed
message = b"Hello, BLS!"

# Generate a signature
signature = AugSchemeMPL.sign(private_key, message)

# Display the results
print("Seed:", seed.hex())
print("Private Key:", private_key)
print("Public Key:", public_key)
print("Message:", message)
print("Signature:", signature)

# Verification
is_valid = AugSchemeMPL.verify(public_key, message, signature)
print("Signature Valid:", is_valid)
