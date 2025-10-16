# app.py (wrapper)
from app_server import main  # or correct import
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", default=5001)
    args = parser.parse_args()
    main(host=args.host, port=args.port)
