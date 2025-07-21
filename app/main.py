from app.config import load_config

def main():
    config = load_config()
    print("Document Processing System Started.")
    print(f"Loaded config: {config}")

if __name__ == "__main__":
    main()

