from setuptools import setup

setup(
    name="text2im",
    packages=[
        "mk_text2im",
        "mk_text2im.clip",
        "mk_text2im.tokenizer",
    ],
    package_data={
        "mk_text2im.tokenizer": [
            "bpe_simple_vocab_16e6.txt.gz",
            "encoder.json.gz",
            "vocab.bpe.gz",
        ],
        "mk_text2im.clip": ["config.yaml"],
    },
    install_requires=[
        "Pillow",
        "attrs",
        "torch",
        "filelock",
        "requests",
        "tqdm",
        "ftfy",
        "regex",
        "numpy",
    ],
)
