from setuptools import setup, find_packages

setup(
    name='face_detector',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'opencv-python>=4.5.5',
        'numpy>=1.21'
    ],
    entry_points={
        'console_scripts': [
            'face-detect=face_detector.detector:main',
        ],
    },
)
