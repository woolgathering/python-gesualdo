try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="gesualdo",
    version="0.6.0",
    description="Gesualdo is a basic pedagogical music theory library for Python",
    long_description="""Better than everything else except abjad.
""",
    author="Jacob Sundstrom",
    author_email="jacobsundstrom@gmail.com",
    url="https://github.com/woolgathering/python-gesualdo",
    packages=[
        "gesualdo",
        "gesualdo.core"
    ],
    # install_requires=["six",],
    # extras_require={
    #     "fft": ["numpy"],
    #     "fluidsynth": ["numpy"],
    # },
    license="GPLv3",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Artistic Software",
        "Topic :: Education",
        "Topic :: Multimedia",
        "Topic :: Multimedia :: Graphics :: Presentation",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
