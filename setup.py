from setuptools import setup, find_packages


setup(
    name='src',
    version='1.0',
    license='MIT',
    author="Krzysztof Kotowski",
    author_email='kotowski.polsl@gmail.com',
    packages=find_packages(),
    package_dir={'src': 'src'},
    url='https://github.com/Kotrix/resperm',
    keywords='changepoint, breakpoint, piecewise, broken-line, broken-stick, segmented, regression, permutation',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy'],
    python_requires='>=3, <4'
)
