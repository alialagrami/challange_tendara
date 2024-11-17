from tendara_ai_challenge.matching.utils import load_notices
from tendara_ai_challenge.matching.Chroma import ChromaSingleton


def main():
    all_notices = load_notices()
    VD = ChromaSingleton()
    VD.add_batch_documents(documents=all_notices)


if __name__ == "__main__":
    main()
