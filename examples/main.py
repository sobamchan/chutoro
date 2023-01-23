from chutoro.main import PDFDocument


def clf(sent: str) -> str | bool:
    if "BERT" in sent:
        return "model"
    elif "fine" in sent:
        return "train"
    return False


if __name__ == "__main__":
    type2color = {"model": "lightblue", "train": "maroon"}
    opath = "./test.pdf"
    document = PDFDocument("./examples/bert.pdf")
    document.run_highlighting(clf, type2color)
    document.save(opath)
