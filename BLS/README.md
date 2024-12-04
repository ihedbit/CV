# BLS Signature Aggregation Example

This repository demonstrates the implementation of BLS (Boneh–Lynn–Shacham) signature generation, aggregation, and verification using the `blspy` Python library. The example includes the generation of private and public keys, signing individual messages, and verifying both individual and aggregated signatures.

## Features
- **Key Generation**: Generate deterministic private and public keys from a seed.
- **Message Signing**: Sign messages using private keys.
- **Signature Aggregation**: Combine multiple signatures into a single aggregated signature.
- **Public Key Aggregation**: Aggregate multiple public keys.
- **Verification**: Verify aggregated signatures and their associated public keys and messages.

## Prerequisites
- Python 3.8 or later.
- Install the `blspy` library:

```bash
pip install blspy
```

## Code Overview

### 1. Key Generation
Keys are generated deterministically using a hashed seed to ensure a fixed length of 32 bytes:
```python
private_key = AugSchemeMPL.key_gen(hashed_seed)
public_key = private_key.get_g1()
```

### 2. Message Signing
Messages are signed using the private key:
```python
signature = AugSchemeMPL.sign(private_key, message)
```

### 3. Aggregation
- Signatures are aggregated using:
  ```python
  aggregated_signature = AugSchemeMPL.aggregate(signatures)
  ```
- Public keys are aggregated using summation:
  ```python
  aggregated_public_key = sum(public_keys, G1Element())
  ```

### 4. Verification
Both individual and aggregated signatures can be verified:
```python
is_valid = AugSchemeMPL.aggregate_verify(public_keys, messages, aggregated_signature)
```

## Example Usage

```python
# Example seeds and messages
seeds = [b"seed1", b"seed2", b"seed3"]
messages = [b"message1", b"message2", b"message3"]

private_keys = []
public_keys = []
signatures = []

# Generate keys and signatures
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
```

## Output
If everything is set up correctly, the script will output:
```plaintext
Aggregate Signature Valid: True
```

## License
This project is open source under the MIT License.

## Acknowledgements
- Uses the [`blspy`](https://github.com/Chia-Network/bls-signatures) library by the Chia Network.
