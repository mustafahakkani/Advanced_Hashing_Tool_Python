import hashlib
import sys
import argparse

# Supported hash algorithms
ALGORITHMS = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

def compute_hashes(message=None, file=None):
    if message:
        input_bytes = message.encode('utf-8')
    elif file:
        with open(file, 'rb') as f:
            input_bytes = f.read()
    else:
        print("No input provided")
        return

    for algorithm in ALGORITHMS:
        h = hashlib.new(algorithm)
        h.update(input_bytes)
        print(f"{algorithm.upper()}: ", h.hexdigest())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--message', help='Message to hash')
    parser.add_argument('-f', '--file', help='File to hash')
    args = parser.parse_args()

    if args.message:
        compute_hashes(message=args.message)
    elif args.file:
        compute_hashes(file=args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
