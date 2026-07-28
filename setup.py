from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="investing-navigator",
    version="1.0.0",
    author="GetOnInvesting.com",
    author_email="info@getoninvesting.com",
    description="Investing Navigator is an intelligent investing assistant that helps users explore investment opportunities, understand financial concepts, and navigate the markets with greater confidence.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://getoninvesting.com",
    project_urls={
        "Homepage": "https://getoninvesting.com",
        "GitHub": "https://github.com/get-on-investing/Investing-Navigator",
        "Documentation": "https://investing-navigator.readthedocs.io",
        "PyPI": "https://pypi.org/project/investing-navigator",
    },
    py_modules=["navigator"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "investing-navigator",
        "investment-assistant",
        "portfolio-planning",
        "financial-education",
        "market-navigation",
        "wealth-building",
        "getoninvesting",
    ],
    entry_points={
        "console_scripts": [
            "investing-navigator=navigator:main",
        ],
    },
)
