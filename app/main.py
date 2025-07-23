from app.config import load_config


def main():
    config = load_config()
    print("Document Processing System Started.")
    print(f"Loaded config: {config}")

    print("Main application logic goes here.")

    # TODO 1: take file from user

    # TODO 2: check if file is pdf or image

    # TODO 3: if pdf, extract text from pdf

    # TODO 4: if image, extract text from image

    # TODO 5: tokenize extracted text

    # TODO 6: store tokens in database

    # TODO 7: return tokens to user


if __name__ == "__main__":
    main()
