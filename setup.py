from distutils.core import setup, Command
from ltsv import __version__, __license__

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys, subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(
    name='ltsv',
    version=__version__,
    description='Labeled Tab-separated Values parser',
    author='hekyou',
    author_email='hekyolabs@gmail.com',
    url='https://github.com/hekyou/python-ltsv',
    keywords='ltsv',
    license=__license__,
    packages=['ltsv'],
    cmdclass = {'test': PyTest},
)
