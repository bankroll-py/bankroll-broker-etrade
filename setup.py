from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bankroll-broker-etrade",
    version="0.1.0",
    author="Bryan Hansen",
    author_email="bryanehansen@gmail.com",
    description="ETrade support for bankroll",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/bankroll-py/bankroll-broker-etrade",
    packages=["bankroll.brokers.etrade"],
    package_data={"bankroll.brokers.etrade": ["py.typed"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3",
        "Topic :: Office/Business :: Financial :: Investment",
        "Typing :: Typed",
    ],
    install_requires=["bankroll_broker ~= 0.4.0", "bankroll_model ~= 0.4.0"],
    keywords="trading investing finance portfolio etrade",
)

